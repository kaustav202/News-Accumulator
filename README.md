# 📰 News-Accumulator

A python automation script to quickly gather and view latest happenings and news information from the web</br>
in a summarised and concise way.

### Functionality
API calls to g-news is used to generate lists of news articles based on the search keyword and also extract various other information from it.Then data is scraped from the website of the article selected by the user itself, to get the contents.The data is cleaned and structured to provide a concise output. Also features a convinient menu based interface.

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

### Requirements
 🔗[Requirement guidelines for this project](requirements.txt)
 
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

**Run a new keyword search and get a list of articles**

<img src = "https://i.postimg.cc/Fsdx6LF3/gns1.png" style = "width: 55%;">

**Select any article no to view it**

<img src = "https://i.postimg.cc/Y9dx5Nmf/gns2.png" style = "width:49%;">&nbsp;&nbsp;<img src = "https://i.postimg.cc/FH0VrXLK/gns3.png" style= "width:50%;">

</br>


**Menu to perform various actions**
- **Press 2  to view another article**

<img src = "https://i.postimg.cc/xjFRgRQ9/gns4.png" style = "width : 48%;">&nbsp;&nbsp;<img src = "https://i.postimg.cc/hGgbhZL1/gns5.png" style = "width : 38%;">



- **Press 3  to search a different set of articles**

<img src = "https://i.postimg.cc/HnjtdJwG/gns6.png"  style = "width : 48%;" > &nbsp;&nbsp; <img src = "https://i.postimg.cc/kX0yPgDZ/gns7.png" style = "width : 48%;" >


- **Press 1  to view additional information**

<img src = "https://i.postimg.cc/yd1PppW8/gns8.png" style = "width: 48%;">

-   **Press 4  to Exit**

<img src = "https://i.postimg.cc/W4PSg1vr/gns11.png" style = "width: 48%;">

