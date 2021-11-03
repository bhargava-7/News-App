from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from bs4 import BeautifulSoup
import requests


def base(request):
    return render(request,'base.html')


class news_object:
  def __init__(self):
    self.text = ""
    self.link = ""
    self.source=""



def technology(request):

    Techpage = requests.get('https://www.indiatoday.in/technology')
    soup= BeautifulSoup(Techpage.content,'lxml')
    Techheadings= soup.findAll('ul',class_='itg-listing')
    technology =[]
    technologylinks=[]
    for x in Techheadings:
       for y in x:
          tech=news_object()
          tech.text=y.text
          tech.link="https://indiatoday.in"+y.a['href']
          tech.source="India Today"
          technology.append(tech)
    return render(request, 'tech.html', {'technology': technology})

def lifestyle(request):
    Lifepage = requests.get('https://www.indiatoday.in/lifestyle')
    soup= BeautifulSoup(Lifepage.content,'lxml')
    Lifeheadings= soup.findAll('ul',class_='itg-listing')
    lifestyle=[]
    for x in Lifeheadings:
        for y in x:
            life=news_object()
            life.text=y.text
            life.link="https://indiatoday.in"+y.a['href']
            life.source="India Today"
            lifestyle.append(life)
    return render(request, 'lifestyle.html', {'lifestyle': lifestyle})

def sports(request):
    Sportpage = requests.get('https://www.indiatoday.in/sports')
    soup= BeautifulSoup(Sportpage.content,'lxml')
    sportheadings= soup.findAll('ul',class_='itg-listing')
    hSportpage = requests.get('https://www.thehindu.com/sport/')
    hsoup= BeautifulSoup(hSportpage.content,'lxml')
    hsportheadings= hsoup.findAll('h3')
    hsports=[]
    for x in hsportheadings[:17]:
            sport=news_object()
            sport.text=x.text
            sport.link='https://www.thehindu.com/sport/'
            sport.source="The Hindu"
            hsports.append(sport)
    
    sports=[]
   
    for x in sportheadings:
        for y in x:
            sport=news_object()
            sport.text=y.text
            sport.link="https://indiatoday.in"+y.a['href']
            sport.source="India Today"
            sports.append(sport)
    sname="India Today"
    sports+=hsports
    
    return render(request, 'sports.html', {'sports': sports,'IndiaToday':sname})




