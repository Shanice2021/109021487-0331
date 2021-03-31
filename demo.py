import requests
from bs4 import BeautifulSoup
#headers={
#    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
#}
#req=requests.get('https://csie.asia.edu.tw/project/semester-103',headers=headers)

## req=requests.get('https://csie.asia.edu.tw/project/semester-103',verify=False)

req=requests.get('http://210.70.80.21/~bs109021487/')
req.encoding='utf-8'
if req.status_code==200:
    #print(r.text)
    soup=BeautifulSoup(req.text,"lxml")
    #print(soup)
    result1=soup.find_all("p")
    fp=open("out2.txt","w",encoding="utf-8")
    #print(result1)

    for val in result1:            
        text1=val.text.replace(' ','')
        text1=text1.replace('\n','')
        data=text1.split(",")
        print(text1)
        fp.write(text1+'\n')
    fp.close()
else:
    print("no page")