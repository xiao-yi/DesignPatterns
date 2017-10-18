#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
Factory Method 工厂模式
'''


class ChinaGetter:
    def __init__(self):
        self.trans = dict(dog=u"小狗", cat=u"小猫")

    def get(self, msgid):
        try:
            return self.trans[msgid]
        except KeyError:
            return str(msgid)

class EnglishGetter:
    def get(self, msgid):
        return str(msgid)

def get_localizer(language="English"):
    """The factory method"""
    languages = dict(English=EnglishGetter, China=ChinaGetter)
    return languages[language]()


# Create our localizers
e, g = get_localizer("English"), get_localizer("China")
# Localize some text
for msgid in "dog parrot cat bear".split():
    print(e.get(msgid), g.get(msgid))
