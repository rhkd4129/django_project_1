import re
from turtle import title
import requests
from bs4 import BeautifulSoup
#https://www.kduniv.ac.kr/kor/CMS/Board/Board.do?robot=Y&mCode=MN246&page=3
url = 'https://www.kduniv.ac.kr/kor/CMS/Board/Board.do?robot=Y&mCode=MN246&page=1'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,'lxml')

#stitle

# titles  = soup.find_all('p',attrs={"class":"stitle"})
subjects=[]
subjects = soup.find_all('tr',attrs={"class":"child_1 isnotice"}).find.all('td',attrs={"class":"cate"})
division=[]
#division = subjects.find('td',attrs={"class":"cate"})

# for title in subjects: 
#     print(title)


for x in subjects:
    print(x)
