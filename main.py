import requests
from defusedxml.minidom import parseString
# defusedxml removes vulnerabilities
import pandas as pd
import pyfiglet as pfg
from termcolor import cprint
from view import select_article 

p = pfg.figlet_format("News Accumulator",font = 'slant')
cprint(p,'blue',attrs = ['bold'])

def get_google_news_result(term, count):
    # Parses the string obtained from get request as xml document object
    obj = parseString(
        requests.get('http://news.google.com/news?q=%s&output=rss' %
                     term).text)
    items = obj.getElementsByTagName('item')
    # Storing the Titles , Agencies, Links and Info
    titles = []
    links = []
    agencies = []
    infos = []
    for item in items[:count]:
        title, agency , link = '', '',''
        info = {}
        for node in item.childNodes:
            if node.nodeName == 'title':
                title = node.childNodes[0].data
            elif node.nodeName == 'link':
                link = node.childNodes[0].data
            elif node.nodeName == 'pubDate':
                info["publication date"] = node.childNodes[0].data
            elif node.nodeName == 'description':
                info["description"] = node.childNodes[0].data
            elif node.nodeName == 'source':
                agency = node.childNodes[0].data
        titles.append(title)
        links.append(link)
        infos.append(info)
        agencies.append(agency)
    return titles, agencies , links , infos

def get_inp():
    titleName = input("Enter the news title keyword: ")
    articleCount = int(input('Enter the number of article count: '))
    titles, agencies , links , info = get_google_news_result(titleName, articleCount)
    news = {'title': titles,'agency':agencies ,'links': links , 'info' : info } 
    # store the recieved information as a dataframe
    df = pd.DataFrame(news, columns=['title','agency', 'links' , 'info' ])
    key = select_article(df,0)
    if key == -1:
        get_inp()
get_inp()
