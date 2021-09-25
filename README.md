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
