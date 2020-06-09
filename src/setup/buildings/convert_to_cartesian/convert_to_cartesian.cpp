#include <GeographicLib/Geocentric.hpp>
#include <GeographicLib/LocalCartesian.hpp>
#include <string.h>
#include <json/writer.h>

#include <mongocxx/client.hpp>
#include <mongocxx/instance.hpp>

#include <bsoncxx/json.hpp>

using namespace mongocxx;
using namespace bsoncxx;

#include <fstream>
#include <iostream>
using namespace std;

void write_json_file(Json::Value json_data, std::string filename) {
  std::ofstream file;
  file.open(filename);
  file << json_data;
  file.close();
}

std::string usage_message(){
    return "Usage:\r\nconvert_to_cartesian centerLat centerLon databaseName";
}

int main(int argc, char** argv) {

    if (argc < 3) {
        cout << "Error, wrong number of input arguments." << endl << usage_message() << endl;
        return 0;
    }

    double centralLat, centralLon;
    double centralAlt = 0;

    try {
        centralLat = stod(argv[1]);
    } 
    catch (...) {
        cout << "Error converting latitude to double." << endl << "Are you sure you provided a real number as central latitude?" << endl << usage_message() << endl;
        return 0;
    }
    try {
        centralLon = stod(argv[2]);
    } 
    catch (...) {
        cout << "Error converting longitude to double." << endl << "Are you sure you provided a real number as central longitude?" << endl << usage_message() << endl;
        return 0;
    }

    std::string database_name = argv[3];

    // database stuff
    
    instance instance{};
    client client{uri{}};
    database db = client[database_name];
    collection buildings = db["buildings"];

    // Geographic lib setup

    GeographicLib::Geocentric m_earth;
    GeographicLib::LocalCartesian m_proj;

    m_earth = GeographicLib::Geocentric (GeographicLib::Constants::WGS84_a (), GeographicLib::Constants::WGS84_f ());
    m_proj = GeographicLib::LocalCartesian (centralLat, centralLon, centralAlt, m_earth);

    cursor blds = buildings.find({});

    Json::Value buildings_json;

    int i = 0;
    for (auto bld : blds) {
        // print the building data
        cout << to_json(bld) << endl;
        cout << "new building" << endl;
        if ( auto prop{bld["properties"]["building"]} ) {
            if ( bld["geometry"]["type"].get_utf8().value == "Polygon" ) {

                auto coordinates = bld["geometry"]["coordinates"][0];
                auto id = bld["id"];

                buildings_json["buildings"][i]["id"] = id.get_utf8().value.to_string();
                cout << id.get_utf8().value << endl;

                int j = 0;
                for (auto coordinate : coordinates.get_array().value) {

                    double x, y, z;

                    m_proj.Forward(coordinate[1].get_double().value, coordinate[0].get_double().value, 0.0, x, y, z);
                    cout << x << " " << y << endl;
                    buildings_json["buildings"][i]["coordinates"][j]["x"] = x;
                    buildings_json["buildings"][i]["coordinates"][j]["y"] = y;
                    j++;
                }
                i++;
            }
        }
    }
    write_json_file(buildings_json, "my_buildings.json");
        

    return 0;

}
