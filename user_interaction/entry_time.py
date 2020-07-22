import datetime
import csv


import datetime
import csv


def ApplyEntry():
        date = datetime.datetime.now()
        datedict = {'Year' : date.year ,'Month' : date.month ,'Day' : date.day ,'Hour' : date.hour ,'Minute' : date.minute,'Second' : date.second  }
        return datedict