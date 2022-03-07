# 📰 News-Accumulator

A python automation script to quickly gather and view latest happenings and news information from the web</br>
in a summarized and consise way.

### Functionality
First data is scraped from google news to generate list of articles based on the search keyword and publishing agency</br> in tabular manner.
Then data is scraped from the article selected by the user to get the contents from website of that article.
 - Generates a list of relevant articles by title and the respective address based on the given keyword.
 - View the contents of any specified article(Page Contents).
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
 [Requirement guidelines for this project](requirements.txt)
 
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

**Install the required modules**

`$pip install -r requirements.txt`


**Go to the project directory and type command**

`$python main.py`


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

