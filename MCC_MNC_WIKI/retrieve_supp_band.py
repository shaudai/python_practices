import sqlite3
import re

conn = sqlite3.connect('mcc_mnc_db.sqlite')
cur = conn.cursor()

cur.execute('select id, name from COUNTRY ORDER by name limit 15')
countries = cur.fetchall()
print 'type of countries', type(countries)

all_support_band = list()
band_dict = dict()
for country in countries:
    all_support_band
    country_name= country[1]
    print '*****************'
    print country_name
    cur.execute('Select support_band from MCC_MNC where country_id = ?', (country[0], ))
    supported_bands_row_list = cur.fetchall()
    for support_band_row in supported_bands_row_list:
        # print support_band_row[0]
        support_band_list = (str(support_band_row[0])).split('/')
        # print support_band_list
        all_support_band += support_band_list
    # print len(all_support_band),'support bands in a country:', all_support_band
    for item in all_support_band:
        if item == 'Unknown' or not item: continue
        band_dict[item.strip()] = band_dict.get(item.strip(), 0) + 1
    print band_dict
    max_of_supp = 0
    def_band = None
    for key, value in band_dict.items():
        if re.search('^LTE', key) and value > max_of_supp:
            def_band = key
            max_of_supp = value
    print country_name, '; Default LTE band: ', def_band
    del all_support_band[:]
    band_dict.clear()