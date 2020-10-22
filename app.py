import config #add your credentials by creating config.py in same directory. 
import io
import os.path
import json
import re
import smtplib

from flask import Flask, request
from urllib.parse import unquote_plus
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

MY_ADDRESS = config.gmail #config sender ID 
PASSWORD = config.password #config sender Password

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """
    Go to localhost:5000 to see a message
    """
    return ('Welcome to Minnal-Murali Bot.', 200, None)


@app.route('/web', methods=['POST']) #webhook receiver
def parse_request():
    data = request.get_data()
    data_parser(data)
    return("OK",200)    #OK
    # need posted
 
def data_parser(data):  #function to extract data from json
   sort = json.loads(data)
   receipent_name = sort['form_response']['answers'][0]['text']
   receipent_email = sort['form_response']['answers'][1]['email']
   print(receipent_name)
   print(receipent_email)
   create_message(receipent_name,receipent_email)

def create_message(name,email): #to create message template
    message_template = read_template('message.txt')
    msg = MIMEMultipart()       # create a message
    message = message_template.substitute(PERSON_NAME=name.title())
    send_email(message,email)
   
def read_template(filename): #read message template 
    with io.open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def send_email(message,email): #send email

    msg = MIMEMultipart() 

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    msg['From']=MY_ADDRESS
    msg['To']=email
    msg['Subject']="Hacktoberfest invite"
    msg.attach(MIMEText(message, 'plain'))

    if(os.path.isfile('img.jpeg')): 
        img_data = open('img.jpeg', 'rb').read() #put attachment location
        image = MIMEImage(img_data, name=os.path.basename('img.jpeg'))
        msg.attach(image)
        # send the message via the server set up earlier.
    s.send_message(msg)
    print("sent!!")
    del msg
    s.quit()

if __name__ == '__main__':
    app.run(debug=False, port=8090, host="0.0.0.0")