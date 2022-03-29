# This module handles the API call and parses the resulting xml document tree.

import requests
from defusedxml.minidom import parseString
# defusedxml removes vulnerabilities

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
