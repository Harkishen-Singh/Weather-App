from urllib.request import urlopen
import subprocess
import requests

class GetSource():
    def __init__(self):
        a=0
        # self.hindiArr=['जनवरी','फरवरी', 'मार्च' , 'अप्रैल', 'मई' ,'जून','जुलाई', 'अगस्त', 'सितंबर', 'अक्टूबर', 'नवंबर', 'दिसंबर' ,'सोमवार', 'मंगलवार', 'बुधवार','गुरुवार','शुक्रवार','शुक्रवार','शनिवार','रविवार']
        # self.englishArr = ['January','February','March','April','May','June','July','August','September','October','November','December','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']


    def actual(self,month,year,city2):
        url = 'https://www.timeanddate.com/weather/india/' + str(city2) + '/historic'
        # self.source = urlopen(url)
        # self.reader = str(self.source.read())
        para = {
            'month':str(month),
            'year':str(year)
        }
        page = requests.get(url, params=para)

        return page

    def getter(self,city,state):
        self.city=city
        self.state=state

        a2 = subprocess.call(['mkdir', self.city+'/'])
        k=0
        y=2016
        for i in range(1, 31) :
            k+=1

            self.content=self.actual(k,y,self.city)
            print('Building.. ' + self.city + '_' + str(i) + '.txt\t status : '+str(self.content.status_code))
            file = open(self.city+'/'+ self.city+'_'+str(i)+'.txt','w',encoding='utf-8')
            txtFor = self.content.text
            # txtFor.replace(self.hindiArr[0],self.englishArr[0])
            # txtFor.replace(self.hindiArr[1], self.englishArr[1])
            # txtFor.replace(self.hindiArr[2], self.englishArr[2])
            # txtFor.replace(self.hindiArr[3], self.englishArr[3])
            # txtFor.replace(self.hindiArr[4], self.englishArr[4])
            # txtFor.replace(self.hindiArr[5], self.englishArr[5])
            # txtFor.replace(self.hindiArr[6], self.englishArr[6])
            # txtFor.replace(self.hindiArr[7], self.englishArr[7])
            # txtFor.replace(self.hindiArr[8], self.englishArr[8])
            # txtFor.replace(self.hindiArr[9], self.englishArr[9])
            # txtFor.replace(self.hindiArr[10], self.englishArr[10])
            # txtFor.replace(self.hindiArr[11], self.englishArr[11])
            # txtFor.replace(self.hindiArr[12], self.englishArr[12])
            # txtFor.replace(self.hindiArr[13], self.englishArr[13])
            # txtFor.replace(self.hindiArr[14], self.englishArr[14])
            # txtFor.replace(self.hindiArr[15], self.englishArr[15])
            # txtFor.replace(self.hindiArr[16], self.englishArr[16])
            # txtFor.replace(self.hindiArr[17], self.englishArr[17])
            # txtFor.replace(self.hindiArr[18], self.englishArr[18])
            file.write(txtFor)
            file.close()
            if k == 12 :
                k=0
                y+=1


obj = GetSource()
obj.getter('Cuttack','Odisha')


