import requests
from xml.dom.minidom import parseString
import pandas as pd
from bs4 import BeautifulSoup
import re

def get_google_news_result(term, count):
    results = []
    # Parses the string as xml document object
    obj = parseString(
        requests.get('http://news.google.com/news?q=%s&output=rss' %
                     term).text)
    items = obj.getElementsByTagName('item')
    
    # Storing the Titles , Agencies, Links and Info
    titles = list()
    links = list()
    agencies = list()
    infos = list()
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
    return titles, agencies links , infos
