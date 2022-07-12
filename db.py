from pymongo import MongoClient
from constants import *

class Database:
    def __init__(self, mongo_url):
        self.client = MongoClient(mongo_url)
        self.db = self.client.lifesim
        self.users = self.db.users
        self.locs = self.db.locs
        self.kvs = self.db.kvs

        self.initialize()

    def initialize(self):
        for street in streets:
            street = streets[street]
            if not self.locs.find_one({'code': street['code']}):
                self.locs.insert_one(street)

        for street in self.locs.find({}):
            for building in street['buildings']:
                building = street['buildings'][building]
                if building['type'] == 'shop':
                    for product in streets[street['code']]['buildings'][building['code']]['products']:
                        product = streets[street['code']]['buildings'][building['code']]['products'][product]
                        if product['code'] not in building['products']:
                            self.locs.update_one({'code': street['code']},
                                            {'$set': {f'buildings.{building["code"]}.products.{product["code"]}': product}})

