#importing the necessary packages and libraries
import random
import pyjokes#used for generating the jokes
import phonenumbers#used for getting phonenumber information
from phonenumbers import carrier#used for getting the company of the number
from phonenumbers import geocoder#used for country of the phone number
from bs4 import BeautifulSoup as BS#used for world wide covid cases information
import requests#used for getting url
from covid import Covid#country wide covid cases information


#Welcome message
responses=[
    'Hi there! I am a chat bot. very nice to meet you. I can help you with the below things',
    'Wonderful, It is so nice to be in touch with you.I am a chat bot. And i can help you with the below things',
    'Warmest welcome! I am a chat bot. I can help you with the below things',
    'Having you here is really a great honour! I am a bot. I can help you with the below things',
    'I am very delighted to have you here. I am a chat bot. And i can help you with the below things'
]
w=random.choice(responses)
print(w)
print('-----------------')


#function for knowing the options
def welcome():
    print('1.One line jokes')
    print('2.Phone number information')
    print('3.Covid world cases information')
    print('4.Covid country cases information')
    print('5.Exit from here')
    print('-----------------')

#selecting the options
def select_from():

    try:
        return int(input('Enter your choice from above: '))
    except:
        print('Please enter choice from the above list')
        print('-----------------')
        return 0


#generating a one line joke
def one_line_joke():
    print(pyjokes.get_joke())
    print('-----------------')


#for knowing the phone number information
def phone_number():
    b=input('Enter a phone number with country code: ')
    ph=phonenumbers.parse(b)
    x='Hi '+geocoder.description_for_number(ph,'en')+'n! you are an '+carrier.name_for_number(ph,'en')+' user.'
    print(x)
    print('-----------------')


#for country covid cases information
def covid_country_cases():
    for i in range(3):
        m=input('Enter a country name: ')
        print('The present cases in {} are: '.format(m))
        covid=Covid()
        cases=covid.get_status_by_country_name(m)
        z=covid.list_countries()
        for x in cases:
            print(x,":",cases[x])
            print('            ')


#for world wide covid cases information
def covid_world_cases():
    print('The total covid cases in the world are: ')
    def get_info(url):
            data=requests.get(url)
            soup=BS(data.text,'html.parser')
            total=soup.find("div",class_="maincounter-number").text
            total=total[1:len(total)-2]
            other=soup.find_all("span",class_="number-table")
            recovered=other[2].text
            deaths=other[3].text
            deaths=deaths[1:]
            ans={'Total Cases':total,'Recovered Cases':recovered,'Total deaths':deaths}
            return ans
    url="https://www.worldometers.info/coronavirus/"
    ans=get_info(url)
    for i,j in ans.items():
         print(i+":"+j)
         print('     ')


#Designing the bot
def bot():
    welcome()
    option=select_from()


    while option!=5:
        if option==1:
            one_line_joke()
        elif option==2:
            phone_number()
        elif option==3:
            covid_world_cases()
        elif option==4:
            covid_country_cases()
        option=select_from()


bot()