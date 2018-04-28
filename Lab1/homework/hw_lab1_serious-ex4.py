from pymongo import MongoClient

uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
client = MongoClient(uri)

db = client.get_default_database()

customers = db['customers']

customers_count = []

ref_list = ['events', 'wom', 'ads']
for ref in ref_list:
    count = customers.find({'ref': ref}).count()
    print('Count for', ref, ':', count)
    customers_count.append(count)

import matplotlib
matplotlib.use('TkAgg')

from matplotlib import pyplot

# print(customers_count)

pyplot.pie(customers_count, labels=ref_list, autopct='%.1f%%')
pyplot.title('Percentage of customer reference'.upper())
pyplot.axis('equal')

pyplot.show()
