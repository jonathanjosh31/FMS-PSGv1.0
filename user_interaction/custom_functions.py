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