import pandas as pd
import pyfiglet as pfg
from termcolor import cprint

from interface import select_article
from news_parser import get_google_news_result

p = pfg.figlet_format("News Accumulator",font = 'slant')
cprint(p,'blue',attrs = ['bold'])

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
