#!/usr/bin/python
from datetime import datetime

class FilterModule(object):
    def filters(self):
        return {
            'year':self.year,
            'month':self.month,
            'day':self.day
        }

    def year(self, input, format):
        datetime_object = datetime.strptime(input, format)
        return datetime_object.year

    def month(self, input, format):
        datetime_object = datetime.strptime(input, format)
        return datetime_object.month

    def day(self, input, format):
        datetime_object = datetime.strptime(input, format)
        return datetime_object.day
