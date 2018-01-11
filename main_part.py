import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
# from __future__ import print_function

class Core_Base:
    def __init__(self):
        self.temperature = 0
        self.city = ""
        self.state = ""
        self.pos_of_temp=0
        self.pos2 = 0

    def asking(self):
        self.city = input("City name : ")
        self.city = self.city.lower()
        self.state = input("State name : ")
        self.state = self.state.lower()
        self.country = "india"
        # url format design below
        self.format = "https://www.msn.com/en-in/weather/today/"+ self.city+self.state+self.country+"/we-city?q="+self.city+"-"+self.state+"&form=PRWLAS&iso=IN&el"
        self.extracting_info_from_net(self.format)


    def is_float(self, input):
          try:
            num = float(input)
          except ValueError:
            return False
          return True

    def is_int(self, input):
          try:
            num = int(input)
          except ValueError:
            return False
          return True

    def extracting_info_from_net(self, url):
        self.response = urlopen(url)
        self.source = self.response.read()
        self.source_text = BeautifulSoup(self.source)
        self.temp = self.source_text.text
        self.source_text = self.temp
        self.length_source_text = len(self.source_text)
        search_class = "Places"
        print("search class = " + search_class)
        length_class = len(search_class)
        #print(self.source_text)
        c = 0
        for i in range(0, self.length_source_text - length_class):
            sub = self.source_text[i:i+length_class]
            if sub == search_class :
                # print('working')
                self.pos_of_temp = i + length_class

        print("self.pos_of_temp : "+ str(self.pos_of_temp))
        # finding the first number after the statename
        for i in range(0,30):
            if self.is_int(self.source_text[i+self.pos_of_temp]):
                self.pos2 = i+self.pos_of_temp
                break


        if self.source_text[self.pos2 + 1].isnumeric() :
            print("got it")
            self.temperature = int(self.source_text[self.pos2] + self.source_text[self.pos2 + 1])

        else :
            self.temperature = int(self.source_text[self.pos2])

    def further_info(self):
        # declaring and initializing

        self.feel = 0
        self.barometer = 0
        self.visibility = 0
        self.humidity = 0
        self.dew_point = 0
        l_feel = len("Feels") # where all l_<feature> represents the length of various parameters
        l_barometer = len("Barometer")
        l_visibility = len("Visibility")
        l_humidity = len("Humidity")
        l_dew_point = len("Dew Point")

        #working on these declared variables

    def displaying(self):
        print("The temperature of " + self.city +  " is : "+ str(self.temperature))


obj = Core_Base()
obj.asking()
obj.displaying()
