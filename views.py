from bs4 import BeautifulSoup
import re
import requests

#Auxiliary function providing option start new search
def restart_session():
    print("\nSearch Again ??") 
    se = input("Y : yes  N: no    ")
    if se in ('Y','y'):
        return -1
    elif se in ('N','n'):
        return 0
    else:
        print("Please provide valid input")
        return restart_session()



#Menu Function that controls action based on user input
def menu(df,id):
    print("\nEnter next task : ","1. View Additional info","2. Open another article","3. Search other article","4. Exit",sep = "\n")
    op = int(input())
    if op == 1:
        print("\nPublication Date : ",df["info"][id+1]['publication date'])
        print("\nDescription : ",df["info"][id+1]['description'])
        return menu(df, id)
    elif op == 2:
        return view_article(df)
    elif op == 3:
        return restart_session()
    elif op == 4:
        return 0
    else:
        print("\n\nPlese provide valid input!!")
        menu(df,id)


#Function to parse contents from the selected website and display it
def view_article(df):
    print("\nWhich article should i open ?" , end= "")
    anum = int(input("Specify Number : "))
    url = df["links"][anum]
    r = requests.get(url) # recieve http response object and store it
    html_str = r.text
    soup = BeautifulSoup(html_str,'html.parser') # create beautiful soup object and parse the html string0
    # get all the text content
    textcontents = re.sub(r'\n\s*\n', r'\n\n', soup.get_text().strip(), flags=re.M)
    print("\n\nHere are the contents of the website : \n\n\n")
    print(textcontents)
    return menu(df,anum-1)


#Function to generate table of articles and respective agencies from the dataframe recieved
def select_article(df,flag):
    if flag == 0:
        df.index = df.index+1
    print("\nhere are some of the articles :: ")
    print(df[["title","agency"]])
    print("\nDo you want to view any article ? ",end="")
    choice = input("Y : yes  N: no ")
    if choice in ('N','n'):
        return restart_session()
    elif choice in ('Y','y'):
        return view_article(df)
    else :
        print("\n","please provide a valid input!!",sep ="")
        return select_article(df,-1)
