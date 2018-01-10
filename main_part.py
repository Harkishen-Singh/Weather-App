import random
import urllib
import requests
import urllib2

class Main_App:
    def __init__(self):
        self.temperature = 0
        self.city = ""
        self.state = ""
        self.pos_of_temp=0
        self.pos2 = 0

    def asking(self):
        #self.city = input("City name : ")
        self.city = "Ludhiana"
        self.state = "Punjab"
        self.country = "india"
        # organising the input to avoid errors while using request library
        if self.city[0].islower():
            self.city2 = self.city[0].toupper() + self.city[1:]
            self.city = self.city2

        if self.state[0].islower():
            self.state2 = self.state[0].toupper() + self.state[1:]
            self.state = self.state2

        # url format design below

        #self.format = "https://www.msn.com/en-in/weather/today"+ self.city+self.state+"india/we-city?q="+self.city+self.state+"&form=PRWLAS&iso=IN&el"
        self.format = "https://www.msn.com/en-in/weather/today"+ self.city+self.state+self.country+"/we-city?q="+self.city+self.state+"&form=PRWLAS&iso=IN&el"
        self.extracting_info_from_net(self.format)


    def extracting_info_from_net(self, url):
        self.response = urllib.urlopen(url)
        self.source_text = self.response.read()

        #       self.source_text = self.source.text

        self.length_source_text = len(self.source_text)
        print("len(self.source_text) : "+str(len(self.source_text)))
        get_span = 'span class="current" aria-label='
        length_get_span = len(get_span)
        print(length_get_span)


        for i in range(0, self.length_source_text - 32):
            sub = self.source_text[i:i+32]
            if sub == get_span :
                print('working')
                self.pos_of_temp = i + length_get_span
                break

        # finding the first " >" position after =
        print("self.pos_of_temp : " + str(self.pos_of_temp))
        for i in range(0,20):
            if self.source_text[ self.pos_of_temp + i ] == ">":
                #print(self.source_text[ self.pos_of_temp + i ])
                self.pos2 = i + self.pos_of_temp
                break
        print(self.pos2)
        print(self.source_text[self.pos2 + 1 : self.pos2+30 ])
        self.temperature = int(self.source_text[self.pos2 + 1 ])

    def displaying(self):
        print("The temperature of the city u entered is : "+ self.temperature)


obj = Main_App()
obj.asking()
obj.extracting_info_from_net()
obj.displaying()
