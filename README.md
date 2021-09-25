# 📰 google-NewsArticle-scrapper

An automation python script to quickly gather and view information from the web (google-news)


### Functionality
First data is scraped from google news to generate list of articles based on the search keyword and publishing agency in tabular manner.
Then data is scraped from the user selected article website to get the contents from website of that article.
 - Generates a list of relevant articles by title and the respective address based on the given keyword.
 - View the contents of any specified article(Page Contents).
 - Customization options to extract relevant useful pieces of information from the site.

### Requirements
 [Requirement guidelines for this project](requirements.txt)
 
### Running Locally
**It is best to use a python virtual environment**

Create a virtual environment in the project dirctory  env.
```
python -m venv app
```
Activate the virtual environment
```
Windows: app\Scripts\activate
```
Install the required modules `pip install -r requirements.txt`\
Go to the directory containing main.py and type command  `python main.py`

### Usage And Output
Here are some sample run of the program

**Run a new keyword search and get a list of articles**


![alt text](https://i.postimg.cc/Fsdx6LF3/gns1.png)

**Select any article no to view it**

![alt text](https://i.postimg.cc/Y9dx5Nmf/gns2.png)
![alt text](https://i.postimg.cc/FH0VrXLK/gns3.png)

**Menu to perform various actions**
- **Press 2  to view another article**

![alt text](https://i.postimg.cc/xjFRgRQ9/gns4.png)
![alt text](https://i.postimg.cc/hGgbhZL1/gns5.png)

- **Press 3  to search a different set of articles**

![alt text](https://i.postimg.cc/HnjtdJwG/gns6.png)
![alt text](https://i.postimg.cc/kX0yPgDZ/gns7.png)

- **Press 1  to view additional information**

![alt text](https://i.postimg.cc/yd1PppW8/gns8.png)
![alt text](https://i.postimg.cc/xdy5RVfZ/gns9.png)
![alt text](https://i.postimg.cc/5yGS0xgX/gns10.png)

-   **Press 4  to Exit**
![alt text](https://i.postimg.cc/W4PSg1vr/gns11.png)
