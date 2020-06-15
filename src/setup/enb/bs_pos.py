import json


class Cell:
    def __init__(self, cell_name, id, system_subtype, pci, earfcn,
                 max_rsrp, direction, bandwidth, uplink_freq,
                 downlink_freq, frequency_band, notes=None):
        self.cell_name = cell_name
        self.id = id
        self.system_subtype = system_subtype
        self.pci = pci
        self.earfcn = earfcn
        self.max_rsrp = max_rsrp
        self.direction = direction
        self.bandwidth = bandwidth
        self.uplink_freq = uplink_freq
        self.downlink_freq = downlink_freq
        self.notes = notes


class Enb:
    def __init__(self, enb_id, mcc, mnc, region, bands, lat, long):
        self.cell_list = []
        self.enb_id = enb_id
        self.mcc = mcc
        self.mnc = mnc
        self.region = region
        self.bands = bands
        self.long = long
        self.lat = lat

    def add_cell(self, cell):
        self.cell_list.append(cell)


# list of eNBs
enb_list = []

# First eNB
enb_id = 12117
mcc = 234 
mnc =  30 
region =  10612
bands = [3]
lat = 55.8694031
long = -4.3065054

enb_1 = Enb(enb_id, mcc, mnc, region, bands, lat, long)
enb_list.append(enb_1)

# Cells of eNB 1
cell_name = 'Cell 0'
id = 3101952
system_subtype = 'LTE'
pci = '382 (127/1)'
earfcn = 1617
max_rsrp = '-70 dBm'
direction = 'NW (316°)'
bandwidth = '20 MHz'
uplink_freq = '1751.7 MHz'
downlink_freq = '1846.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_1.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 1'
id = 3101953
system_subtype = 'LTE'
pci = '381 (127/0)'
earfcn = 1617
max_rsrp = '-71 dBm'
direction = 'S (164°)'
bandwidth = '20 MHz'
uplink_freq = '1751.7 MHz'
downlink_freq = '1846.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_1.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 2'
id = 3101954
system_subtype = 'LTE'
pci = '383 (127/2)'
earfcn = 1617
max_rsrp = '-81 dBm'
direction = 'W (254°)'
bandwidth = '20 MHz'
uplink_freq = '1751.7 MHz'
downlink_freq = '1846.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_1.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 3'
id = 3101955
system_subtype = 'LTE'
pci = '382 (127/1)'
earfcn = 1761
max_rsrp = '-88 dBm'
direction = 'NW (303°)'
bandwidth = '10 MHz'
uplink_freq = '1766.1 MHz'
downlink_freq = '1861.1 MHz'
frequency_band = 'DCS (B3 FDD)'

notes = 'Second Carrier'
enb_1.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band, notes))

cell_name = 'Cell 4'
id = 3101956
system_subtype = 'LTE'
pci = '381 (127/0)'
earfcn = 1761
max_rsrp = '-73 dBm'
direction = 'E (93°)'
bandwidth = '10 MHz'
uplink_freq = '1766.1 MHz'
downlink_freq = '1861.1 MHz'
frequency_band = 'DCS (B3 FDD)'

notes = 'Second Carrier'
enb_1.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band, notes))

cell_name = 'Cell 5'
id = 3101957
system_subtype = 'LTE'
pci = '383 (127/2)'
earfcn = 1761
max_rsrp = '-70 dBm'
direction = 'W (273°)'
bandwidth = '10 MHz'
uplink_freq = '1766.1 MHz'
downlink_freq = '1861.1 MHz'
frequency_band = 'DCS (B3 FDD)'

notes = 'Second Carrier'
enb_1.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band, notes))

# Second eNB
enb_id = 12043
mcc = 234 
mnc =  30 
region =  10612
bands = [3]
lat = 55.8787402
long = -4.2918999

enb_2 = Enb(enb_id, mcc, mnc, region, bands, lat, long)

# Cells of second eNB

cell_name = 'Cell 0'
id = 3083008
system_subtype = 'LTE-A'
pci = '322 (107/1)'
earfcn = 1667
max_rsrp = '-68 dBm'
direction = 'N (344°)'
bandwidth = '20 MHz'
uplink_freq = '1756.7 MHz'
downlink_freq = '1851.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_2.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 1'
id = 3083009
system_subtype = 'LTE'
pci = '321 (107/0)'
earfcn = 1617
max_rsrp = '-63 dBm'
direction = 'SE (118°)'
bandwidth = '20 MHz'
uplink_freq = '1751.7 MHz'
downlink_freq = '1846.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_2.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))


cell_name = 'Cell 2'
id = 3083010
system_subtype = 'LTE'
pci = '323 (107/2)'
earfcn = 1617
max_rsrp = '-63 dBm'
direction = 'SW (203°)'
bandwidth = '20 MHz'
uplink_freq = '1751.7 MHz'
downlink_freq = '1846.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_2.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 3'
id = 3083011
system_subtype = 'LTE-A'
pci = '322 (107/1)'
earfcn = 1811
max_rsrp = '-81 dBm'
direction = 'S (164°)'
bandwidth = '10 MHz'
uplink_freq = '1771.1 MHz'
downlink_freq = '1866.1 MHz'
frequency_band = 'DCS (B3 FDD)'
notes = 'Second Carrier'
enb_2.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band, notes))

cell_name = 'Cell 4'
id = 3083012
system_subtype = 'LTE'
pci = '321 (107/0)'
earfcn = 1761
max_rsrp = '-73 dBm'
direction = 'SE (118°)'
bandwidth = '10 MHz'
uplink_freq = '1766.1 MHz'
downlink_freq = '1861.1 MHz'
frequency_band = 'DCS (B3 FDD)'
notes = 'Second Carrier'

enb_2.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band, notes))

cell_name = 'Cell 5'
id = 3083013
system_subtype = 'LTE'
pci = '323 (107/2)'
earfcn = 1761
max_rsrp = '-74 dBm'
direction = 'SW (207°)'
bandwidth = '10 MHz'
uplink_freq = '1766.1 MHz'
downlink_freq = '1861.1 MHz'
frequency_band = 'DCS (B3 FDD)'
notes = 'Second Carrier'

enb_2.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band, notes))
enb_list.append(enb_2)

# Third eNB

enb_id = 15141
mcc = 234 
mnc =  30 
region =  10612
bands = [3, 7]
lat = 55.87328706629074
long = -4.288381646948608

enb_3 = Enb(enb_id, mcc, mnc, region, bands, lat, long)

# Cells of third eNB
cell_name = 'Cell 0'
id = 3876096
system_subtype = 'LTE'
pci = '46 (15/1)'
earfcn = 1617
max_rsrp = '-74 dBm'
direction = 'W (282°)'
bandwidth = '20 MHz'
uplink_freq = '1751.7 MHz'
downlink_freq = '1846.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_3.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 1'
id = 3876097
system_subtype = 'LTE-A'
pci = '45 (15/0)'
earfcn = 1667
max_rsrp = '-68 dBm'
direction = 'E (91°)'
bandwidth = '20 MHz'
uplink_freq = '1756.7 MHz'
downlink_freq = '1851.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_3.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 2'
id = 3876098
system_subtype = 'LTE'
pci = '47 (15/2)'
earfcn = 1617
max_rsrp = '-71 dBm'
direction = 'W (251°)'
bandwidth = '20 MHz'
uplink_freq = '1751.7 MHz'
downlink_freq = '1846.7 MHz'
frequency_band = 'DCS (B3 FDD)'
enb_3.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 3'
id = 3876099
system_subtype = 'LTE'
pci = '46 (15/1)'
earfcn = 1788
max_rsrp = '-67 dBm'
direction = 'W (287°)'
bandwidth = '10 MHz'
uplink_freq = '1768.8 MHz'
downlink_freq = '1863.8 MHz'
frequency_band = 'DCS (B3 FDD)'
notes = 'Second Carrier'

enb_3.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band, notes))

cell_name = 'Cell 4'
id = 3876100
system_subtype = 'LTE-A'
pci = '45 (15/0)'
earfcn = 1811
max_rsrp = '-67 dBm'
direction = 'E (102°)'
bandwidth = '10 MHz'
uplink_freq = '1771.1 MHz'
downlink_freq = '1866.1 MHz'
frequency_band = 'DCS (B3 FDD)'
notes = 'Second Carrier'

enb_3.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band, notes))

cell_name = 'Cell 5'
id = 3876101
system_subtype = 'LTE'
pci = '47 (15/2)'
earfcn = 1788
max_rsrp = '-70 dBm'
direction = 'SW (239°)'
bandwidth = '10 MHz'
uplink_freq = '1768.8 MHz'
downlink_freq = '1863.8 MHz'
frequency_band = 'DCS (B3 FDD)'
notes = 'Second Carrier'

enb_3.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band, notes))

cell_name = 'Cell 7'
id = 3876103
system_subtype = 'LTE'
pci = '45 (15/0)'
earfcn = 3350
max_rsrp = '-90 dBm'
direction = 'S (165°)'
bandwidth = '20 MHz'
uplink_freq = '2560 MHz'
downlink_freq = '2680 MHz'
frequency_band = 'IMT-E (B7 FDD)'

enb_3.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))
cell_name = 'Cell 8'
id = 3876104
system_subtype = 'LTE'
pci = '47 (15/2)'
earfcn = 3350
max_rsrp = '-96 dBm'
direction = 'W (280°)'
bandwidth = '20 MHz'
uplink_freq = '2560 MHz'
downlink_freq = '2680 MHz'
frequency_band = 'IMT-E (B7 FDD)'

enb_3.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

enb_list.append(enb_3)

enb_id = 14527
mcc = 234 
mnc =  30 
region =  10612
bands = [3]
lat = 55.8676093130332
long = -4.2831586371283565

enb_4 = Enb(enb_id, mcc, mnc, region, bands, lat, long)

cell_name = 'Cell 1'
id = 3718913
system_subtype = 'LTE'
pci = '169 (56/1)'
earfcn = 1667
max_rsrp = '-98 dBm'
direction = 'E (105°)'
bandwidth = '20 MHz'
uplink_freq = '1756.7 MHz'
downlink_freq = '1851.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_4.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 2'
id = 3718914
system_subtype = 'LTE-A'
pci = '168 (56/0)'
earfcn = 1667
max_rsrp = '-79 dBm'
direction = 'W (285°)'
bandwidth = '20 MHz'
uplink_freq = '1756.7 MHz'
downlink_freq = '1851.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_4.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

enb_list.append(enb_4)

enb_id = 10933
mcc = 234 
mnc =  30 
region =  10612
bands = [3]
lat = 55.873388810569935
long = -4.274888871579623

enb_5 = Enb(enb_id, mcc, mnc, region, bands, lat, long)

cell_name = 'Cell 0'
id = 2798848
system_subtype = 'LTE-A'
pci = '182 (60/2)'
earfcn = 1667
max_rsrp = '-65 dBm'
direction = 'NW (293°)'
bandwidth = '20 MHz'
uplink_freq = '1756.7 MHz'
downlink_freq = '1851.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_5.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 1'
id = 2798849
system_subtype = 'LTE'
pci = '180 (60/0)'
earfcn = 1617
max_rsrp = '-58 dBm'
direction = 'E (112°)'
bandwidth = '20 MHz'
uplink_freq = '1751.7 MHz'
downlink_freq = '1846.7 MHz'
frequency_band = 'DCS (B3 FDD)'
enb_5.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 2'
id = 2798850
system_subtype = 'LTE-A'
pci = '181 (60/1)'
earfcn = 1667
max_rsrp = '-72 dBm'
direction = 'W (289°)'
bandwidth = '20 MHz'
uplink_freq = '1756.7 MHz'
downlink_freq = '1851.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_5.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 3'
id = 2798851
system_subtype = 'LTE-A'
pci = '182 (60/2)'
earfcn = 1811
max_rsrp = '-68 dBm'
direction = 'W (289°)'
bandwidth = '10 MHz'
uplink_freq = '1771.1 MHz'
downlink_freq = '1866.1 MHz'
frequency_band = 'DCS (B3 FDD)'
notes = 'Second Carrier'

enb_5.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band, notes))

cell_name = 'Cell 4'
id = 2798852
system_subtype = 'LTE-A'
pci = '180 (60/0)'
earfcn = 1811
max_rsrp = '-68 dBm'
direction = 'E (111°)'
bandwidth = '10 MHz'
uplink_freq = '1771.1 MHz'
downlink_freq = '1866.1 MHz'
frequency_band = 'DCS (B3 FDD)'
notes = 'Second Carrier'

enb_5.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band, notes))

cell_name = 'Cell 5'
id = 2798853
system_subtype = 'LTE'
pci = '181 (60/1)'
earfcn = 1811
max_rsrp = '-73 dBm'
direction = 'W (250°)'
bandwidth = '10 MHz'
uplink_freq = '1771.1 MHz'
downlink_freq = '1866.1 MHz'
frequency_band = 'DCS (B3 FDD)'
notes = 'Second Carrier'

enb_5.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band, notes))

enb_list.append(enb_5)

enb_id = 12044
mcc = 234 
mnc =  30 
region =  10612
bands = [3, 7, 20]
lat = 55.8638644
long = -4.2936047

enb_6 = Enb(enb_id, mcc, mnc, region, bands, lat, long)

cell_name = 'Cell 0'
id = 3083264
system_subtype = 'LTE'
pci = '246 (82/0)'
earfcn = 1617
max_rsrp = '-81 dBm'
direction = 'E (81°)'
bandwidth = '20 MHz'
uplink_freq = '1751.7 MHz'
downlink_freq = '1846.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_6.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 1'
id = 3083265
system_subtype = 'LTE'
pci = '247 (82/1)'
earfcn = 1617
max_rsrp = '-77 dBm'
direction = 'SW (213°)'
bandwidth = '20 MHz'
uplink_freq = '1751.7 MHz'
downlink_freq = '1846.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_6.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 2'
id = 3083266
system_subtype = 'LTE'
pci = '248 (82/2)'
earfcn = 1617
max_rsrp = '-84 dBm'
direction = 'SW (207°)'
bandwidth = '20 MHz'
uplink_freq = '1751.7 MHz'
downlink_freq = '1846.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_6.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 3'
id = 3083267
system_subtype = 'LTE'
pci = '246 (82/0)'
earfcn = 1761
max_rsrp = '-92 dBm'
direction = 'E (80°)'
bandwidth = '10 MHz'
uplink_freq = '1766.1 MHz'
downlink_freq = '1861.1 MHz'
frequency_band = 'DCS (B3 FDD)'
notes = 'Second Carrier'

enb_6.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band,notes))

cell_name = 'Cell 4'
id = 3083268
system_subtype = 'LTE'
pci = '247 (82/1)'
earfcn = 1761
max_rsrp = '-74 dBm'
direction = 'S (167°)'
bandwidth = '10 MHz'
uplink_freq = '1766.1 MHz'
downlink_freq = '1861.1 MHz'
frequency_band = 'DCS (B3 FDD)'
notes = 'Second Carrier'

enb_6.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band,notes))

cell_name = 'Cell 5'
id = 3083269
system_subtype = 'LTE'
pci = '248 (82/2)'
earfcn = 1761
max_rsrp = '-81 dBm'
direction = 'SW (227°)'
bandwidth = '10 MHz'
uplink_freq = '1766.1 MHz'
downlink_freq = '1861.1 MHz'
frequency_band = 'DCS (B3 FDD)'
notes = 'Second Carrier'

enb_6.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band,notes))

cell_name = 'Cell 6'
id = 3083270
system_subtype = 'LTE'
pci = '117 (39/0)'
earfcn = 6225
max_rsrp = '-86 dBm'
direction = 'E (86°)'
bandwidth = '20 MHz'
uplink_freq = '839.5 MHz'
downlink_freq = '798.5 MHz'
frequency_band = 'EU Digital Dividend (B20 FDD)'

enb_6.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 7'
id = 3083271
system_subtype = 'LTE'
pci = '433 (144/1)'
earfcn = 3350
max_rsrp = '-76 dBm'
direction = 'NE (62°)'
bandwidth = '20 MHz'
uplink_freq = '2560 MHz'
downlink_freq = '2680 MHz'
frequency_band = 'IMT-E (B7 FDD)'

enb_6.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 8'
id = 3083272
system_subtype = 'LTE'
pci = '434 (144/2)'
earfcn = 3350
max_rsrp = '-76 dBm'
direction = 'W (292°)'
bandwidth = '20 MHz'
uplink_freq = '2560 MHz'
downlink_freq = '2680 MHz'
frequency_band = 'IMT-E (B7 FDD)'

enb_6.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))
cell_name = 'Cell 9'
id = 3083273
system_subtype = 'LTE-A'
pci = '247 (82/1)'
earfcn = 3179
max_rsrp = '-91 dBm'
direction = 'N (341°)'
bandwidth = '15 MHz'
uplink_freq = '2542.9 MHz'
downlink_freq = '2662.9 MHz'
frequency_band = 'IMT-E (B7 FDD)'
notes = 'Second Carrier'

enb_6.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band,notes))

cell_name = 'Cell 10'
id = 3083274
system_subtype = 'LTE-A'
pci = '452 (150/2)'
earfcn = 3179
max_rsrp = '-73 dBm'
direction = 'SE (151°)'
bandwidth = '15 MHz'
uplink_freq = '2542.9 MHz'
downlink_freq = '2662.9 MHz'
frequency_band = 'IMT-E (B7 FDD)'
notes = 'Second Carrier'

enb_6.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band,notes))

cell_name = 'Cell 11'
id = 3083275
system_subtype = 'LTE-A'
pci = '248 (82/2)'
earfcn = 3179
max_rsrp = '-70 dBm'
direction = 'NW (294°)'
bandwidth = '15 MHz'
uplink_freq = '2542.9 MHz'
downlink_freq = '2662.9 MHz'
frequency_band = 'IMT-E (B7 FDD)'
notes = 'Second Carrier'

enb_6.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band,notes))

enb_list.append(enb_6)

enb_id = 31727
mcc = 234 
mnc =  30 
region =  10612
bands = [3]
lat = 55.8630048
long = -4.2960866

enb_7 = Enb(enb_id, mcc, mnc, region, bands, lat, long)

cell_name = 'Cell 1'
id = 8122113
system_subtype = 'LTE'
pci = '118 (39/1)'
earfcn = 1617
max_rsrp = '-88 dBm'
direction = 'SE (123°)'
bandwidth = '20 MHz'
uplink_freq = '1751.7 MHz'
downlink_freq = '1846.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_7.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 2'
id = 8122114
system_subtype = 'LTE'
pci = '119 (39/2)'
earfcn = 1617
max_rsrp = '-88 dBm'
direction = 'W (276°)'
bandwidth = '20 MHz'
uplink_freq = '1751.7 MHz'
downlink_freq = '1846.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_7.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 4'
id = 8122116
system_subtype = 'LTE'
pci = '118 (39/1)'
earfcn = 1761
max_rsrp = '-87 dBm'
direction = 'E (88°)'
bandwidth = '10 MHz'
uplink_freq = '1766.1 MHz'
downlink_freq = '1861.1 MHz'
frequency_band = 'DCS (B3 FDD)'
notes = 'Second Carrier'

enb_7.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band,notes))

cell_name = 'Cell 5'
id = 8122117
system_subtype = 'LTE'
pci = '119 (39/2)'
earfcn = 1761
max_rsrp = '-86 dBm'
direction = 'NW (303°)'
bandwidth = '10 MHz'
uplink_freq = '1766.1 MHz'
downlink_freq = '1861.1 MHz'
frequency_band = 'DCS (B3 FDD)'
notes = 'Second Carrier'

enb_7.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band,notes))

enb_list.append(enb_7)

enb_id = 34447
mcc = 234 
mnc =  30 
region =  10612
bands = [3]
lat = 55.865389
long = -4.2738135

enb_8 = Enb(enb_id, mcc, mnc, region, bands, lat, long)

cell_name = 'Cell 0'
id = 8818432
system_subtype = 'LTE'
pci = '127 (42/1)'
earfcn = 1667
max_rsrp = '-87 dBm'
direction = 'N (0°)'
bandwidth = '20 MHz'
uplink_freq = '1756.7 MHz'
downlink_freq = '1851.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_8.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

enb_list.append(enb_8)

enb_id = 10937
mcc = 234 
mnc =  30 
region =  10612
bands = [3, 7]
lat = 55.86813416030628
long = -4.271109824878555

enb_9 = Enb(enb_id, mcc, mnc, region, bands, lat, long)

cell_name = 'Cell 0'
id = 2799872
system_subtype = 'LTE'
pci = '139 (46/1)'
earfcn = 1617
max_rsrp = '-73 dBm'
direction = 'NE (59°)'
bandwidth = '20 MHz'
uplink_freq = '1751.7 MHz'
downlink_freq = '1846.7 MHz'
frequency_band = 'DCS (B3 FDD)'
enb_9.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 1'
id = 2799873
system_subtype = 'LTE'
pci = '140 (46/2)'
earfcn = 1617
max_rsrp = '-71 dBm'
direction = 'W (283°)'
bandwidth = '20 MHz'
uplink_freq = '1751.7 MHz'
downlink_freq = '1846.7 MHz'
frequency_band = 'DCS (B3 FDD)'
enb_9.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 2'
id = 2799874
system_subtype = 'LTE-A'
pci = '42 (14/0)'
earfcn = 1667
max_rsrp = '-85 dBm'
direction = 'W (254°)'
bandwidth = '20 MHz'
uplink_freq = '1756.7 MHz'
downlink_freq = '1851.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_9.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 3'
id = 2799875
system_subtype = 'LTE'
pci = '139 (46/1)'
earfcn = 1761
max_rsrp = '-75 dBm'
direction = 'NE (41°)'
bandwidth = '10 MHz'
uplink_freq = '1766.1 MHz'
downlink_freq = '1861.1 MHz'
frequency_band = 'DCS (B3 FDD)'
notes = 'Second Carrier'
enb_9.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band,notes))

cell_name = 'Cell 4'
id = 2799876
system_subtype = 'LTE'
pci = '140 (46/2)'
earfcn = 1761
max_rsrp = '-76 dBm'
direction = 'SW (228°)'
bandwidth = '10 MHz'
uplink_freq = '1766.1 MHz'
downlink_freq = '1861.1 MHz'
frequency_band = 'DCS (B3 FDD)'
notes = 'Second Carrier'
enb_9.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band,notes))

cell_name = 'Cell 6'
id = 2799878
system_subtype = 'LTE'
pci = '139 (46/1)'
earfcn = 3350
max_rsrp = '-74 dBm'
direction = 'NE (55°)'
bandwidth = '20 MHz'
uplink_freq = '2560 MHz'
downlink_freq = '2680 MHz'
frequency_band = 'IMT-E (B7 FDD)'

enb_9.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 7'
id = 2799879
system_subtype = 'LTE'
pci = '43 (14/1)'
earfcn = 3350
max_rsrp = '-79 dBm'
direction = 'SW (234°)'
bandwidth = '20 MHz'
uplink_freq = '2560 MHz'
downlink_freq = '2680 MHz'
frequency_band = 'IMT-E (B7 FDD)'
enb_9.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 8'
id = 2799880
system_subtype = 'LTE'
pci = '42 (14/0)'
earfcn = 3350
max_rsrp = '-92 dBm'
direction = 'SW (220°)'
bandwidth = '20 MHz'
uplink_freq = '2560 MHz'
downlink_freq = '2680 MHz'
frequency_band = 'IMT-E (B7 FDD)'

enb_9.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 9'
id = 2799881
system_subtype = 'LTE'
pci = '139 (46/1)'
earfcn = 3179
max_rsrp = '-84 dBm'
direction = 'NW (329°)'
bandwidth = '15 MHz'
uplink_freq = '2542.9 MHz'
downlink_freq = '2662.9 MHz'
frequency_band = 'IMT-E (B7 FDD)'
notes = 'Second Carrier'

enb_9.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band,notes))
cell_name = 'Cell 10'
id = 2799882
system_subtype = 'LTE'
pci = '140 (46/2)'
earfcn = 3179
max_rsrp = '-78 dBm'
direction = 'SW (236°)'
bandwidth = '15 MHz'
uplink_freq = '2542.9 MHz'
downlink_freq = '2662.9 MHz'
frequency_band = 'IMT-E (B7 FDD)'
notes = 'Second Carrier'
enb_9.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band,notes))
cell_name = 'Cell 11'
id = 2799883
system_subtype = 'LTE-A'
pci = '42 (14/0)'
earfcn = 3179
max_rsrp = '-97 dBm'
direction = 'SW (209°)'
bandwidth = '15 MHz'
uplink_freq = '2542.9 MHz'
downlink_freq = '2662.9 MHz'
frequency_band = 'IMT-E (B7 FDD)'
notes = 'Second Carrier'
enb_9.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band,notes))

enb_list.append(enb_9)

enb_id = 12042
mcc = 234 
mnc =  30 
region = 7186
bands = [3, 7]
enb_10 = Enb(enb_id, mcc, mnc, region, bands, lat, long)


cell_name = 'Cell 1'
id = 3082753
system_subtype = 'LTE'
pci = '363 (121/0)'
earfcn = 1617
max_rsrp = '-97 dBm'
direction = 'W (281°)'
bandwidth = '20 MHz'
uplink_freq = '1751.7 MHz'
downlink_freq = '1846.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_10.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))
cell_name = 'Cell 4'
id = 3082756
system_subtype = 'LTE'
pci = '363 (121/0)'
earfcn = 1761
max_rsrp = '-81 dBm'
direction = 'E (101°)'
bandwidth = '10 MHz'
uplink_freq = '1766.1 MHz'
downlink_freq = '1861.1 MHz'
frequency_band = 'DCS (B3 FDD)'
notes = 'Second Carrier'
enb_10.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band,notes))

cell_name = 'Cell 6'
id = 3082758
system_subtype = 'LTE'
pci = '318 (106/0)'
earfcn = 3350
max_rsrp = '-118 dBm'
direction = 'NE (49°)'
bandwidth = '20 MHz'
uplink_freq = '2560 MHz'
downlink_freq = '2680 MHz'
frequency_band = 'IMT-E (B7 FDD)'

enb_10.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

enb_list.append(enb_10)

enb_id = 12184
mcc = 234 
mnc =  30 
region =  10611
bands = [3]
lat = 55.8591924
long = -4.2993373

enb_11 = Enb(enb_id, mcc, mnc, region, bands, lat, long)

cell_name = 'Cell 0'
id = 3119104
system_subtype = 'LTE'
pci = '360 (120/0)'
earfcn = 1617
max_rsrp = '-64 dBm'
direction = 'SE (156°)'
bandwidth = '20 MHz'
uplink_freq = '1751.7 MHz'
downlink_freq = '1846.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_11.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 2'
id = 3119106
system_subtype = 'LTE'
pci = '362 (120/2)'
earfcn = 1617
max_rsrp = '-68 dBm'
direction = 'W (288°)'
bandwidth = '20 MHz'
uplink_freq = '1751.7 MHz'
downlink_freq = '1846.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_11.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 3'
id = 3119107
system_subtype = 'LTE'
pci = '360 (120/0)'
earfcn = 1761
max_rsrp = '-84 dBm'
direction = 'NE (52°)'
bandwidth = '10 MHz'
uplink_freq = '1766.1 MHz'
downlink_freq = '1861.1 MHz'
frequency_band = 'DCS (B3 FDD)'
notes = 'Second Carrier'
enb_11.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band, notes))

cell_name = 'Cell 5'
id = 3119109
system_subtype = 'LTE'
pci = '362 (120/2)'
earfcn = 1761
max_rsrp = '-85 dBm'
direction = 'NW (303°)'
bandwidth = '10 MHz'
uplink_freq = '1766.1 MHz'
downlink_freq = '1861.1 MHz'
frequency_band = 'DCS (B3 FDD)'
notes = 'Second Carrier'

enb_11.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band, notes))
enb_list.append(enb_11)


enb_id = 12042
mcc = 234 
mnc =  30 
region = 7186
bands = [3, 7]
lat = 55.860782
long = -4.2828578
enb_12 = Enb(enb_id, mcc, mnc, region, bands, lat, long)

cell_name = 'Cell 1'
id = 3082753
system_subtype = 'LTE'
pci = '363 (121/0)'
earfcn = 1617
max_rsrp = '-97 dBm'
direction = 'W (281°)'
bandwidth = '20 MHz'
uplink_freq = '1751.7 MHz'
downlink_freq = '1846.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_12.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 4'
id = 3082756
system_subtype = 'LTE'
pci = '363 (121/0)'
earfcn = 1761
max_rsrp = '-81 dBm'
direction = 'E (101°)'
bandwidth = '10 MHz'
uplink_freq = '1766.1 MHz'
downlink_freq = '1861.1 MHz'
frequency_band = 'DCS (B3 FDD)'
notes = 'Second Carrier'

enb_12.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band, notes))

cell_name = 'Cell 6'
id = 3082758
system_subtype = 'LTE'
pci = '318 (106/0)'
earfcn = 3350
max_rsrp = '-118 dBm'
direction = 'NE (49°)'
bandwidth = '20 MHz'
uplink_freq = '2560 MHz'
downlink_freq = '2680 MHz'
frequency_band = 'IMT-E (B7 FDD)'

enb_12.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

enb_list.append(enb_12)
enb_id = 27613
mcc = 234 
mnc =  30 
region =  10611
bands = [3, 7]
lat = 55.8567116
long = -4.2896814
enb_13 = Enb(enb_id, mcc, mnc, region, bands, lat, long)

cell_name = 'Cell 0'
id = 7068928
system_subtype = 'LTE'
pci = '470 (156/2)'
earfcn = 1667
max_rsrp = '-74 dBm'
direction = 'N (18°)'
bandwidth = '20 MHz'
uplink_freq = '1756.7 MHz'
downlink_freq = '1851.7 MHz'
frequency_band = 'DCS (B3 FDD)'
enb_13.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))
cell_name = 'Cell 1'
id = 7068929
system_subtype = 'LTE-A'
pci = '289 (96/1)'
earfcn = 1617
max_rsrp = '-74 dBm'
direction = 'E (100°)'
bandwidth = '20 MHz'
uplink_freq = '1751.7 MHz'
downlink_freq = '1846.7 MHz'
frequency_band = 'DCS (B3 FDD)'
enb_13.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 6'
id = 7068934
system_subtype = 'LTE-A'
pci = '290 (96/2)'
earfcn = 3350
max_rsrp = '-70 dBm'
direction = 'NW (295°)'
bandwidth = '20 MHz'
uplink_freq = '2560 MHz'
downlink_freq = '2680 MHz'
frequency_band = 'IMT-E (B7 FDD)'

enb_13.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))
cell_name = 'Cell 7'
id = 7068935
system_subtype = 'LTE-A'
pci = '289 (96/1)'
earfcn = 3350
max_rsrp = '-71 dBm'
direction = 'E (93°)'
bandwidth = '20 MHz'
uplink_freq = '2560 MHz'
downlink_freq = '2680 MHz'
frequency_band = 'IMT-E (B7 FDD)'
enb_13.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 8'
id = 7068936
system_subtype = 'LTE-A'
pci = '288 (96/0)'
earfcn = 3350
max_rsrp = '-71 dBm'
direction = 'W (268°)'
bandwidth = '20 MHz'
uplink_freq = '2560 MHz'
downlink_freq = '2680 MHz'
frequency_band = 'IMT-E (B7 FDD)'

enb_13.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 9'
id = 7068937
system_subtype = 'LTE-A'
pci = '290 (96/2)'
earfcn = 3179
max_rsrp = '-65 dBm'
direction = 'E (87°)'
bandwidth = '15 MHz'
uplink_freq = '2542.9 MHz'
downlink_freq = '2662.9 MHz'
frequency_band = 'IMT-E (B7 FDD)'
notes = 'Second Carrier'
enb_13.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band, notes))

cell_name = 'Cell 10'
id = 7068938
system_subtype = 'LTE-A'
pci = '289 (96/1)'
earfcn = 3179
max_rsrp = '-72 dBm'
direction = 'E (95°)'
bandwidth = '15 MHz'
uplink_freq = '2542.9 MHz'
downlink_freq = '2662.9 MHz'
frequency_band = 'IMT-E (B7 FDD)'
notes = 'Second Carrier'
enb_13.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band, notes))
cell_name = 'Cell 11'
id = 7068939
system_subtype = 'LTE-A'
pci = '288 (96/0)'
earfcn = 3179
max_rsrp = '-72 dBm'
direction = 'W (274°)'
bandwidth = '15 MHz'
uplink_freq = '2542.9 MHz'
downlink_freq = '2662.9 MHz'
frequency_band = 'IMT-E (B7 FDD)'
notes = 'Second Carrier'

enb_13.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band, notes))

enb_list.append(enb_13)

enb_id = 11319
mcc = 234 
mnc =  30 
region =  10611
bands = [3]
lat = 55.8556276
long = -4.2710132
enb_14 = Enb(enb_id, mcc, mnc, region, bands, lat, long)

cell_name = 'Cell 0'
id = 2897664
system_subtype = 'LTE'
pci = '168 (56/0)'
earfcn = 1667
max_rsrp = '-85 dBm'
direction = 'SE (140°)'
bandwidth = '20 MHz'
uplink_freq = '1756.7 MHz'
downlink_freq = '1851.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_14.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 1'
id = 2897665
system_subtype = 'LTE-A'
pci = '304 (101/1)'
earfcn = 1617
max_rsrp = '-90 dBm'
direction = 'S (188°)'
bandwidth = '20 MHz'
uplink_freq = '1751.7 MHz'
downlink_freq = '1846.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_14.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 2'
id = 2897666
system_subtype = 'LTE-A'
pci = '170 (56/2)'
earfcn = 1667
max_rsrp = '-102 dBm'
direction = 'SW (218°)'
bandwidth = '20 MHz'
uplink_freq = '1756.7 MHz'
downlink_freq = '1851.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_14.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 3'
id = 2897667
system_subtype = 'LTE'
pci = '305 (101/2)'
earfcn = 1761
max_rsrp = '-106 dBm'
direction = 'NW (320°)'
bandwidth = '10 MHz'
uplink_freq = '1766.1 MHz'
downlink_freq = '1861.1 MHz'
frequency_band = 'DCS (B3 FDD)'
notes = 'Second Carrier'

enb_14.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band, notes))

cell_name = 'Cell 3'
id = 2897669
system_subtype = 'LTE-A'
pci = '303 (101/0)'
earfcn = 1811
max_rsrp = '-95 dBm'
direction = 'SW (222°)'
bandwidth = '10 MHz'
uplink_freq = '1771.1 MHz'
downlink_freq = '1866.1 MHz'
frequency_band = 'DCS (B3 FDD)'
notes = 'Second Carrier'
enb_14.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band, notes))
enb_list.append(enb_14)

enb_id = 32334
mcc = 234 
mnc =  30 
region =  10611
bands = [1, 3, 7]
lat = 55.8581735
long =  -4.269335
enb_15 = Enb(enb_id, mcc, mnc, region, bands, lat, long)
cell_name = 'Cell 0'
id = 8277504
system_subtype = 'LTE'
pci = '227 (75/2)'
earfcn = 1617
max_rsrp = '-64 dBm'
direction = 'N (5°)'
bandwidth = '20 MHz'
uplink_freq = '1751.7 MHz'
downlink_freq = '1846.7 MHz'
frequency_band = 'DCS (B3 FDD)'
enb_15.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))
cell_name = 'Cell 1'
id = 8277505
system_subtype = 'LTE'
pci = '225 (75/0)'
earfcn = 1617
max_rsrp = '-64 dBm'
direction = 'N (2°)'
bandwidth = '20 MHz'
uplink_freq = '1751.7 MHz'
downlink_freq = '1846.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_15.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))
cell_name = 'Cell 2'
id = 8277506
system_subtype = 'LTE'
pci = '226 (75/1)'
earfcn = 1617
max_rsrp = '-71 dBm'
direction = 'N (8°)'
bandwidth = '20 MHz'
uplink_freq = '1751.7 MHz'
downlink_freq = '1846.7 MHz'
frequency_band = 'DCS (B3 FDD)'

enb_15.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 4'
id = 8277508
system_subtype = 'LTE-A'
pci = '78 (26/0)'
earfcn = 1811
max_rsrp = '-78 dBm'
direction = 'NE (55°)'
bandwidth = '10 MHz'
uplink_freq = '1771.1 MHz'
downlink_freq = '1866.1 MHz'
frequency_band = 'DCS (B3 FDD)'
notes = 'Second Carrier'
enb_15.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band, notes))

cell_name = 'Cell 5'
id = 8277509
system_subtype = 'LTE'
pci = '226 (75/1)'
earfcn = 1788
max_rsrp = '-81 dBm'
direction = 'N (339°)'
bandwidth = '10 MHz'
uplink_freq = '1768.8 MHz'
downlink_freq = '1863.8 MHz'
frequency_band = 'DCS (B3 FDD)'
notes = 'Second Carrier'

enb_15.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band, notes))
cell_name = 'Cell 6'
id = 8277510
system_subtype = 'LTE'
pci = '227 (75/2)'
earfcn = 3350
max_rsrp = '-73 dBm'
direction = 'N (3°)'
bandwidth = '20 MHz'
uplink_freq = '2560 MHz'
downlink_freq = '2680 MHz'
frequency_band = 'IMT-E (B7 FDD)'

enb_15.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 7'
id = 8277511
system_subtype = 'LTE'
pci = '225 (75/0)'
earfcn = 3350
max_rsrp = '-69 dBm'
direction = 'NE (65°)'
bandwidth = '20 MHz'
uplink_freq = '2560 MHz'
downlink_freq = '2680 MHz'
frequency_band = 'IMT-E (B7 FDD)'

enb_15.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 8'
id = 8277512
system_subtype = 'LTE'
pci = '226 (75/1)'
earfcn = 3350
max_rsrp = '-69 dBm'
direction = 'S (184°)'
bandwidth = '20 MHz'
uplink_freq = '2560 MHz'
downlink_freq = '2680 MHz'
frequency_band = 'IMT-E (B7 FDD)'

enb_15.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))
cell_name = 'Cell 9'
id = 8277513
system_subtype = 'LTE'
pci = '60 (20/0)'
earfcn = 3179
max_rsrp = '-61 dBm'
direction = 'N (21°)'
bandwidth = '15 MHz'
uplink_freq = '2542.9 MHz'
downlink_freq = '2662.9 MHz'
frequency_band = 'IMT-E (B7 FDD)'
notes = 'Second Carrier'
enb_15.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band, notes))
cell_name = 'Cell 10'
id = 8277514
system_subtype = 'LTE-A'
pci = '78 (26/0)'
earfcn = 3179
max_rsrp = '-65 dBm'
direction = 'N (14°)'
bandwidth = '15 MHz'
uplink_freq = '2542.9 MHz'
downlink_freq = '2662.9 MHz'
frequency_band = 'IMT-E (B7 FDD)'
notes = 'Second Carrier'

enb_15.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band, notes))

cell_name = 'Cell 11'
id = 8277515
system_subtype = 'LTE'
pci = '61 (20/1)'
earfcn = 3179
max_rsrp = '-71 dBm'
direction = 'S (186°)'
bandwidth = '15 MHz'
uplink_freq = '2542.9 MHz'
downlink_freq = '2662.9 MHz'
frequency_band = 'IMT-E (B7 FDD)'
notes = 'Second Carrier'

enb_15.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band, notes))

cell_name = 'Cell 18'
id = 8277522
system_subtype = 'LTE'
pci = '227 (75/2)'
earfcn = 522
max_rsrp = '-80 dBm'
direction = 'N (2°)'
bandwidth = '15 MHz'
uplink_freq = '1972.2 MHz'
downlink_freq = '2162.2 MHz'
frequency_band = 'IMT (B1 FDD)'

enb_15.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 19'
id = 8277523
system_subtype = 'LTE'
pci = '60 (20/0)'
earfcn = 522
max_rsrp = '-82 dBm'
direction = 'N (356°)'
bandwidth = '15 MHz'
uplink_freq = '1972.2 MHz'
downlink_freq = '2162.2 MHz'
frequency_band = 'IMT (B1 FDD)'

enb_15.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

cell_name = 'Cell 20'
id = 8277524
system_subtype = 'LTE'
pci = '226 (75/1)'
earfcn = 522
max_rsrp = '-84 dBm'
direction = 'S (181°)'
bandwidth = '15 MHz'
uplink_freq = '1972.2 MHz'
downlink_freq = '2162.2 MHz'
frequency_band = 'IMT (B1 FDD)'

enb_15.add_cell(Cell(cell_name, id, system_subtype, pci, earfcn, max_rsrp,
                    direction, bandwidth, uplink_freq, downlink_freq,
                    frequency_band))

enb_list.append(enb_15)

with open('./results/enb_data.json', 'w', encoding='utf8') as json_file:
    json.dump(enb_list, json_file, default=lambda x: x.__dict__, ensure_ascii=False, indent=2)
