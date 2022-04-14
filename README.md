# 📰 News-Accumulator

A python automation script to quickly gather and view latest happenings and news information from the web</br>
in a summarised and concise way.

### Functionality
API calls to g-news is used to generate lists of news articles based on the search keyword and also extract various other information from it. Then data is scraped from the website of the article selected by the user itself, to get the contents. The data is cleaned and structured to provide a concise output. Also features a convinient menu based interface.

 - Generates a list of relevant articles showing the title and the respective publication agency based on any user given keyword.
 - Select and view the contents of any article(Page Contents).
 - Interactive menu based interface that allows switching between articles or search a new topic.
 - Customization options to extract relevant useful pieces of information from the site.

### Technologies Used
- **Requests** for handling web server communicatons and sending get requests.
- **Beautiful Soup** for parsing the html of the website and derive useful contents as a dom object.
- **xml.dom.minidom** to parse the xml string and store it in a structured way as dom object.
- **news api** to collect latest news json stream.

### Domains

- **CLI-Tools**
- **XML-dom**
- **APIs**
- **Web Scraping**
- **Data Science**

</br>

### Requirements
 🔗[Requirement guidelines for this project](requirements.txt)
 
</br>

### Running Locally

</br>

**Using a new python virtual environment**

Create a virtual environment in the project dirctory  env.
```
python -m venv app
```
Activate the virtual environment
```
Windows: app\Scripts\activate
```

</br>

**Install all the required packages**

```
$pip install -r requirements.txt
```


**Navigate to the project directory and type command**

```
$python main.py
```


</br>

### Usage And Output
Here are some sample run of the program

### Run a new keyword search and get a list of articles

&nbsp;<img src = "https://i.postimg.cc/SsCdf8j4/na1.png" style = "width:55%;">

### <b>Select any article to view contents</b>

&nbsp;&nbsp;<img src = "https://i.postimg.cc/59C71X5L/na2.png" style = "width:55%;">&nbsp;

&nbsp;&nbsp;<img src = "https://i.postimg.cc/5y46PYbT/na3.png" style= "width:53%;">


### Menu to perform various actions

</br>

- **[ 2 ] : view another article &nbsp;&nbsp; [ 3 ] : search another topic**

&nbsp;&nbsp;&nbsp;<img src = "https://i.postimg.cc/26QMT3Ss/na4.png" style = "width : 48%;">&nbsp;&nbsp;<img src = "https://i.postimg.cc/HnjtdJwG/gns6.png"  style = "width : 46%;" > 


- **[ 1 ] : additional info &nbsp;&nbsp; [ 4 ] : exit**

&nbsp;&nbsp;&nbsp;&nbsp;<img src = "https://i.postimg.cc/yd1PppW8/gns8.png" style = "width: 48%;">&nbsp;&nbsp;<img src = "https://i.postimg.cc/W4PSg1vr/gns11.png" style = "width: 47%;">
