# -*- coding:utf-8 -*-
import json

def parase_city_word():
    word_list = []
    with open("level.json",'r') as f:
        temp = json.loads(f.read())
        for city in temp:
            for area in city["children"]:
                if "children" in area:
                    pre_area = "%s%s" % (city["name"], area["name"])
                    word_list.append([pre_area, "1000"])
                    for sub_area in area["children"]:
                        suf_area = "%s%s" % (area["name"], sub_area["name"])
                        word_list.append([suf_area,'1000'])
                else:
                    data = "%s%s" % (city["name"], area["name"])
                    word_list.append([data, "1000"])
    print(word_list)
    return word_list

def parase_wsxc_word():
    inputs = open('app_word.txt', 'r')
    word_list = []
    for line in inputs:
       values = line.strip('\n').split('	')
       if len(values) > 1:
           word_list.append(values)
    return word_list

def parse_food_word():
    inputs = open('THUOCL_food.txt', 'r')
    word_list = []
    for line in inputs:
       values = line.strip('\n').split('	')
       if len(values) > 1:
           word_list.append(values)
    return word_list

if __name__ == '__main__':
    parase_city_word()