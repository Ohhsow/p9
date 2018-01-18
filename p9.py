# -*- coding: utf-8 -*-
# Created by Andrei Kisel

import sys
import logging
from random import randint
from functools import reduce

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.addHandler(logging.FileHandler("flower_report.log"))



class Flower(object):

    def __init__(self, name, price, color='red', length=20, life_time=0):
        self.name = name
        self.price = price
        self.color = color
        self.length = length
        self.length = life_time

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def __str__(self):
        return self.color


class Bouquet(object):

    def __init__(self, name):
        self.name = name
        self.flowers = []

    def __str__(self):
        flowers = ' '
        for i in self.flowers:
            flowers += str(i.name) + ' '
        return self.name + ': '+ flowers

    def add_flower(self, flower):
        self.flowers.append(flower)

    def remove_flower(self, flower):
        self.flowers.remove(flower)

    def get_flowers(self):
        return self.flowers

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def calc_cost(self):
        return reduce(lambda x,y: x+y, [x.price for x in self.flowers])

    def get_nr(self):
        return len(self.flowers)


rose = Flower('Rose', 20, 'blue')
logger.info(rose)

tulip = Flower('Tulip', 60)
logger.info(tulip)

bouquet = Bouquet('First Bouquet')

bouquet.add_flower(rose)
bouquet.add_flower(rose)
bouquet.add_flower(tulip)
bouquet.add_flower(rose)
bouquet.add_flower(rose)

logger.info(bouquet)

bouquet.remove_flower(rose)

bouquet.add_flower(tulip)

logger.info(bouquet)

logger.info('Has {} flowers and costs {}'.format(bouquet.get_nr(), bouquet.calc_cost()))






