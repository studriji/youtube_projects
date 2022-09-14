import requests


# api key = 
# url for api = api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

city = input('Enter the city : ')
#city = "kolkata"
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid='
data = requests.get(url).json()

data_dict = {
            'city' : data['name'],
            'weather' : data['weather'][0]['main'],
            'temp_K' : data['main']['temp'],
            'temp_C' : int(data['main']['temp'] - 273),
            'pressure' : data['main']['pressure']
                }
result = {'data' : data_dict}
#print(result)
#print(data_dict['city'])
msg = ''
for i in data_dict:
    msg = msg + f'{i} : {data_dict[i]}' + '\n'
#print(msg)

import smtplib
import ssl
from email.message import EmailMessage
email_sender = ''
email_password = '16 digit password'    
email_receiver = ''

subject = 'Weather update'
body = msg

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

