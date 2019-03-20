# Facebook - ERROR404 [ https://www.facebook.com/error4o4.org/ ]
#             ___ _ __ _ __ ___  _ __  | || |  / _ \| || |  
#            / _ \ '__| '__/ _ \| '__| | || |_| | | | || |_ 
#           |  __/ |  | | | (_) | |    |__   _| |_| |__   _|
#            \___|_|  |_|  \___/|_||ANGEL||_|  \___/   |_|               
# GITHUB - ERROR404 [ https://github.com/error404-notfound ]
#  APP TEST - http://www.mediafire.com/file/b2p8w8v3d0z8p5m/LEON-TUNNEL-VPN.apk -

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests
import re
def getcsrf(t):
	d=t[(t.find("csrf")+28):(t.find("csrf")+60)]
	return d
total=[]
def eliminate(l):
        if(l not in total):
                total.append(l)



print ('''
   \033[1;31m           {01000101}{01010010}{01010010}{01001111}
             ___ _ __ _ __ ___  _ __  | || |  / _ \| || |  
            / _ \ '__| '__/ _ \| '__| | || |_| | | | || |_ 
\033[1;37m           |  __/ |  | | | (_) | |    |__   _| |_| |__   _|
            \___|_|  |_|  \___/|_||ANGEL||_|  \___/   |_|                                              
  \033[1;31m       {01010010}{00110100}|HOST-EXTRACTOR|{00110000}{00110100}                 
    \033[1;37m             | - \033[1;37m||facebook.com/error4o4.org|| 
       ''')
                
url="https://dnsdumpster.com/"
print'''\033[1;36m'''
dom=raw_input("Host: ")
print ('''  ''')
r=requests.get(url)
t=r.text
tkn="csrftoken="+getcsrf(t)+";"
header = {"Referer":"https://dnsdumpster.com","Cookie" :tkn}
r=requests.post("https://dnsdumpster.com",data={'csrfmiddlewaretoken':getcsrf(t),'targetip':dom},headers=header)
resp=r.text
l=re.findall((r'<tr><td class="col-md-4">(.*?).'+dom+'<br>'),resp)
for i in l:
        if(i!=''):
                v=i+'.'+dom
                eliminate(v)
link=[]
url="https://www.virustotal.com/en/domain/"+dom+"/information/"
r=requests.get(url)
t=r.text
f=open("Angel.txt","w")
f.write(t)
f.write("Angel - https://www.facebook.com/error4o4.org")
f.close()
f=open("Angel.txt","r")
a=""
n=0
for i in f:
           if i=="  <div class=\"enum \">\n":
                                            f.readline()
                                            a=f.readline()
                                            a.lstrip()
                                            if(a[-3:-1]=="om"):
                                                               
                                                               link=link+[a[100:-100]]
                                                               n+=1
for i in link:
    eliminate(i)
for i in total:
        print(i)




print("\nCompletado - Error404")

