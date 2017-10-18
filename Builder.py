#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Builder 建造者
'''


class Director(object):
    def __init__(self):
        self.builder = None

    def construct_building(self):
        self.builder.new_building()
        self.builder.build_floor()
        self.builder.build_size()

    def get_building(self):
        return self.builder.building


class Builder(object):
    def __init__(self):
        self.building = None

    def new_building(self):
        self.building = Building()


class BuildHouse(Builder):
    def build_floor(self):
        self.building.floor = 'One'

    def build_size(self):
        self.building.size = 'Big'


class BuildFlat(Builder):
    def build_floor(self):
        self.building.floor = 'More than One'

    def build_size(self):
        self.building.size = 'Small'


class Building(object):
    def __init__(self):
        self.floor = None
        self.size = None

    def __repr__(self):
        return 'Floor:%s |Size:%s' % (self.floor, self.size)


if __name__ == '__main__':
    director = Director()
    director.builder = BuildHouse()
    director.construct_building()
    building = director.get_building()
    print(building)
    director.builder = BuildFlat()
    director.construct_building()
    building = director.get_building()
    print(building)
