#Imports
from twilio.rest import Client
import schedule, time
import random

#Vars
cellphone = 123
twilio_number = 234

#List of messages
morning_messages = [
    "Good morning",
    "Have a great day!",
    "Be productive today",
    "Enjoy your day!"
]

#Functions
def send_message(quote):

    account = ""
    token = ""
    client = Client(account, token)
    

    client.messages.create(to=cellphone,from_=twilio_number,body=quote)
                           
                           
quote = morning_messages[random.randint(0, len(morning_messages)-1)]                          
schedule.every().day.at("07:00").do(send_message, morning_messages)
