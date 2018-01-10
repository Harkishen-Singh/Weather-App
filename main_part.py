import random
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Main_App:
    def __init__(self):
        self.temperature = 0
        self.city = ""
        self.state = ""
        self.pos_of_temp=0
        self.pos2 = 0

    def asking(self):
        #self.city = input("City name : ")
        self.city = "ludhiana"
        self.state = "lunjab"
        self.country = "india"
        # organising the input to avoid errors while using request library
        '''if self.city[0].islower():
            self.city2 = self.city[0].toupper() + self.city[1:]
            self.city = self.city2

        if self.state[0].islower():
            self.state2 = self.state[0].toupper() + self.state[1:]
            self.state = self.state2'''

        # url format design below

        #self.format = "https://www.msn.com/en-in/weather/today"+ self.city+self.state+"india/we-city?q="+self.city+self.state+"&form=PRWLAS&iso=IN&el"
        self.format = "https://www.msn.com/en-in/weather/today/"+ self.city+self.state+self.country+"/we-city?q="+self.city+"-"+self.state+"&form=PRWLAS&iso=IN&el"
        self.extracting_info_from_net(self.format)


    def extracting_info_from_net(self, url):
        self.response = urlopen(url)
        self.source = self.response.read()
        self.source_text = BeautifulSoup(self.source)
        self.temp = self.source_text.text
        self.source_text = self.temp
        self.length_source_text = len(self.source_text)
        print("len(self.source_text) : "+ str(self.length_source_text))
        search_class = 'class="curcond"'
        length_class = len(search_class)
        print(length_class)
        print(self.source_text)


        for i in range(0, self.length_source_text - length_class):
            sub = self.source_text[i:i+length_class]
            #print("tough part : " +sub)
            if sub == search_class :
                print('working')
                self.pos_of_temp = i + length_class
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

