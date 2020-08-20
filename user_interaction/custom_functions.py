import datetime,random
import csv
import qrcode


def ApplyEntry(serial_no):
        date = datetime.datetime.now()
        temp = format(random.randint(90,109) + random.random() , '.3f')
        if float(temp) >= 100.00 :
                status = False
        else:
                status = True
        
        datedict = {'Serial_No' : serial_no,'Year' : date.year ,'Month' : date.month ,'Day' : date.day ,'Hour' : date.hour ,'Minute' : date.minute,'Second' : date.second,'Temp' : float(temp),'Status' : status }
        return datedict

def generate_qr(codestring):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            border=1,
        )
        qr.add_data(str(codestring))
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        return img

def monthlyChart(data_list):
        today = datetime.date.today()
        today_month = today.month
    
        temp_day_list = []
        for d in data_list:
                day = []
                if d['Month'] == today_month:
                        day.append(d['Day'])
                        day.append(d['Temp'])
                        temp_day_list.append(day)

        return temp_day_list

def yearlyChart(data_list):
    today = datetime.date.today()
    current_year = today.year
  
    temp_sum =[0,0,0,0,0,0,0,0,0,0,0,0]
    count = [0,0,0,0,0,0,0,0,0,0,0,0]
    avg_temp = [0,0,0,0,0,0,0,0,0,0,0,0]

    for d in data_list:
        if d['Year'] == current_year:
            temp_sum[d['Month']-1] = temp_sum[d['Month']-1] + d['Temp']
            count[d['Month']-1] = count[d['Month']-1] + 1

    for i in range(12):
        if count[i] == 0:
            avg_temp[i] = temp_sum[i]
        else:
            avg_temp[i] = temp_sum[i]/count[i]
    return avg_temp

def pieChart(data_list):
    count_list = [0,0,0]
    for d in data_list:
        if d['Temp'] >=90 and d['Temp'] < 95:
            count_list[0] += 1
        elif d['Temp'] >=95 and d['Temp'] <100:
            count_list[1] += 1
        else:
            count_list[2] += 1
    return count_list

def get_total_average_temp(entries):
    sumtemp = 0
    for entry in entries:
        sumtemp += entry['Temp']
    length = len(entries)
    avg = format(sumtemp / length , '.3f')
    return avg
