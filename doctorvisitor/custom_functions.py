import datetime,random




# custom functions for populating:
def visitorstoday():
    today = datetime.datetime.now()
    temp = format(random.randint(90,109) + random.random() , '.3f')
    status = bool(random.getrandbits(1))
    entry = { 'name':'Nitish' , 'phoneno' : '9876545673' ,'Year' : today.year,'Month' : today.month,'Day' : today.day,'Hour' : today.hour,'Minute' : today.minute,'Second' : today.second,'temp':temp,'status':status}
    return entry