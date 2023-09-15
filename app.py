
import streamlit as st
st.set_page_config(page_title="Nitin Mali",layout="wide",initial_sidebar_state="collapsed")
import yfinance as yf  
import pandas as pd 
import streamlit as st
import numpy as np
import pandas as pd
import time
from widgets.navbar import *
from streamlit.components.v1 import html
from PIL import Image
import streamlit.components.v1 as components


def main():
    #navbar 
    render_navbar()
    # css
    with open("assets/styles/style.css") as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    #markdowns
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)


with st.container():
   st.write("This is inside the container")

   # You can call any Streamlit command, including custom components:
   st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")



#Header
st.write('''
# Nitin Mali
## Ms.c, Data Science
##### *Resume* 
''')
         
image = Image.open('/Users/nyzy/nitzmali/portfolio/assets/images/LPYH.gif')


left_co, cent_co,last_co = st.columns([0.9,1,1])
with cent_co:
    st.markdown("![Alt Text](https://media.giphy.com/media/CVtNe84hhYF9u/giphy.gif)")



# bootstrap 4 collapse example
components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div id="accordion">
      <div class="card">
        <div class="card-header" id="headingOne">
          <h5 class="mb-0">
            <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            Collapsible Group Item #1
            </button>
          </h5>
        </div>
        <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #1 content
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-header" id="headingTwo">
          <h5 class="mb-0">
            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            Collapsible Group Item #2
            </button>
          </h5>
        </div>
        <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #2 content
          </div>
        </div>
      </div>
    </div>
    """,
    height=600,
)    



# Function to embed Bootstrap CDN
def add_bootstrap():
    st.markdown("""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
  </head>
  <body>
    <h1>Hello, world!</h1>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
  </body>
</html>
        """, unsafe_allow_html=True)

# Using the function to embed Bootstrap
add_bootstrap()

components.html("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
<div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="https://mdbcdn.b-cdn.net/img/Photos/Slides/img%20(23).webp" class="d-block w-100" alt="nitin">
    </div>
    <div class="carousel-item">
      <img src="https://mdbcdn.b-cdn.net/img/Photos/Slides/img%20(23).webp" class="d-block w-100" alt="...">
    </div>  
    <div class="carousel-item">
      <img src="https://mdbcdn.b-cdn.net/img/Photos/Slides/img%20(23).webp" class="d-block w-100" alt="...">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>""",height=600)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- I'm a seasoned data scientist. My forte lies in harnessing advanced analytics and machine learning to distill complex data into transformative business solutions. 
- My pivotal roles at ZS and Aktana have centered on innovative data science, while my engagement at Xsunt enriched my proficiency in analytics domain. 
- Regardless of the industry, my aim is steadfast: extracting actionable intelligence from data torrents to help businesses thrive in a data-centric world. 
- My expertise encompasses AI, Data Science, Advanced Analytics, Sales and Product Analytics, Strategic Planning, and Business Strategy.


**Data Science, Analytics:**
- Leveraging data for actionable insights and strategic alignment
- segmentation, channel modeling, A/B testing, market mix modeling.
- Leading cross-functional projects and collaboration with product, engineering, and design teams.

**Data Infrastructure & Engineering on AWS:**
- Building scalable data pipelines and features.
- ETL, data visualization using tools like Tableau/Python.

**Big Data, Machine Learning, & NLP:**
- Utilizing big data tech, diverse ML algorithms, including time series forecasting, recommendation systems, and NLP for sentiment analysis.

**Analytics & Business Strategy:**
- Refining marketing using data analytics, emphasizing predictive modeling for optimal reach.

**Technical Skills:** \n
My technical toolkit include the following, and I can learn new tools and languages quickly in the job:
- Programming Languages/ Analytical Tools - Python, Spark, Adobe Analytics, Advanced Excel
- Database Query Language - Snowflake, AWS RDS, Postgres, Oracle SQL, MySQL, MongoDB
- Data Visualization - Tableau, Matplotlib, Ggplot2
- Cloud - AWS [RDS,EC2, Glue, EMR,S3] and DataBricks [MLFlow, Auto ML]
- Data Analysis - Statistical Analysis, Exploratory Data Analysis, Regression Analysis, A/B Testing, Experimental Design and Analysis, Optimization
- Statistical methods/Machine Learning - Linear/Logistic Regression, Time series analysis, A/B Testing, Clustering, Principal Component Reduction, Survival Analysis, ARIMA, Decision Trees, Random Forest, 
NLP

**Business Skills:**
- Communication: Translating data complexities for a non-tech audience.
- fostering data-driven organizational decisions using Excel and powerpoint
- Business Acumen: Aligning analytics with overarching business objectives.
- Problem-Solving: Turning challenges into data-driven insights.
- Team Dynamics: Leading and integrating diverse teams for comprehensive solutions.
''')

st.markdown('''
## Education
''')
            
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([10,2],gap="large")
  with col1:
    st.markdown(a,unsafe_allow_html=True)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

txt('**Master of Science** (Data Science), *Rutgers University*, New Jersey, United States','Jan 2017- Jun 2018')
st.markdown('''
- GPA: `3.74`
- Project `Built a website for Blogging under Rutgers Student Association Using Python and Django framework where I published my website on Heroku app using sql3 database server.`
- Focus: `AI, Machine Learning, Statistics, Data Analytics, Data Mining, Big data, Business Intelligence, Project Management.`
''')
            

txt('**Bachelor of Engineering** (Computer Science), *M.S Ramaiah*, Bengaluru, India','May 2011- May 2015')
st.markdown('''
- GPA: `3.6`
- Research thesis entitled **ISRO (Indian Space Research Organisation)** `Design of a fault tolerant autonomoy of a spacecraft. Collaborated with ISRO scientists on a spacecraft, meticulously handling extensive data to reduce faults using machine learning. Published a research paper on IRJET journal.`
- Go Mad (Android App) `Plays two songs simultaneously, one song in the left and one in the right ear phone without any splitters.`
- Focus: `AI, Machine Learning, Statistics, Data Analytics, Data Mining, Big data, Business Intelligence, Project Management.`
- Smart Dustbin: **FKCCI(Federation of Karnataka Chambers of Commerce and Industry)** `Smart Dustbin provides an easy solution to waste management. It segregates waste into wet and dry at a domestic level using simple IOT capacitor device.`
''')
            

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Chanin Nantasenamat</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#bioinformatics-tools">Bioinformatics Tools</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


#####################
st.markdown('''
## Work Experience
''')
txt('**Data Scientist, ZS**, New York, United States',
'Jan 2023 - Present')
st.markdown('''
- Developed and executed channel propensity models with Neural Networks on rich, real-world data sets, subsequently enhancing representative engagement rates with doctors by an impressive 25%.  
- Conducted deep data analysis using Association Rule Mining and Large Language Models (LLMs) to derive strategic insights, influencing product and brand strategy in specific therapeutic areas. 
- Leveraged multi-channel optimization strategies, utilizing Linear Programming, and Logistic Regression, to determine the most effective channels for reps to engage with doctors, achieving a 10% efficiency improvement while maintaining high engagement levels. 
- Designed, deployed, and evaluated business experiments using Ensemble Methods, pinpointing opportunities for higher adoption and using NLP techniques for enriched patient experience. 
- Successfully conducted advanced patient and doctor segmentation techniques using Decision Trees and Clustering algorithms, which played a pivotal role in boosting the marketing ROI by 20%. 
- Spearheaded commercial analytics projects, leveraging Gradient Boosted Trees and Random Forest algorithms to achieve a robust 15% YoY increase in sales through predictive modeling insights. 
- Presented data-driven insights to senior management using Topic Modeling and Sentiment Analysis, converting intricate analyses into actionable, business-centric conclusions.
''')
            
txt('**Data Engineer Manager, WebMD**, New York, United States',
'Nov 2022 - Jan 2023')
st.markdown('''
- Integrated cutting-edge big data tools like AWS and Spark, enhancing data processing capabilities.
- Led key data visualization projects, employing Tableau and Power BI for comprehensive stakeholder reports.
''')
            

txt('**Data Scientist, Aktana**, New York, United States',
'Nov 2019 - Nov 2022')
st.markdown('''
- Played a crucial role in the development and deployment of the Contextual Intelligence Engine (CIE) on AWS EMR, utilizing Gradient Boosting Machines, Decision Trees, and Naive Bayes for tasks like channel propensity, optimization, and sentiment analysis. Ensured top-tier model performance through a diverse set of ML algorithms like SVMs and DBSCAN.
- Engineered a cutting-edge automated ETL process on AWS using Lambda functions, which bolstered data accessibility, cut inefficiencies by 35%, and established a single source of truth, critical for all machine learning and analytics endeavors.
- Undertook detailed customer segmentation with K-means clustering, churn prediction via Decision Trees, and market basket analysis using the Apriori algorithm. These initiatives led to marked enhancements in marketing strategies and outcomes while continuously exploring and adopting ARIMA and Prophet for time series forecasting to enhance the team's technical repertoire.
- Spearheaded the transition from Alteryx BI to Snowflake and Tableau, leveraging Neural Networks for data preprocessing and creating data warehouses and dashboards tailored for pharmaceutical clients, thus positioning the company as a leader in scalable and efficient data visualization.
''')
            
txt('**Data Analyst, Xsunt Corp**, pennsylvania, United States',
'Jun 2018 - Oct 2019')
st.markdown('''
- Collaborated with Bristol Myers Squibb, improving dashboard utility, resulting in a 40% surge in user engagement.
- Applied advanced segmentation techniques for targeted sales and marketing initiatives with 60% sales forecast achieved via simple time series.
- Applied Bayesian techniques, hypothesis testing, and regression models to optimize data-driven strategies.
''')
            
txt('**Software Engineer, Temenos**, Bengaluru, India',
'Jun 2018 - Oct 2019')
st.markdown('''
- Amplified the efficiency of the Temenos Payments Suite by integrating SQL with Python, achieving a 30% improvement.
- Reduced payment discrepancies by 25% through in-depth defect analysis.
''')
            
txt('**Data Science Intern, Indian Space Research Organization (ISRO)**, Bengaluru, India',
'Jan 2015 - May 2015')
st.markdown('''
- Collaborated with ISRO scientists on a spacecraft fault-tolerant autonomy project, meticulously handling extensive data, ensuring its integrity, and innovating solutions to reduce discrepancies by 15%.
- Published a research paper on IRJET journal. 
''')
            

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`, `Digital Ocean`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/nitsmali/')
txt2('Twitter', 'https://twitter.com/nyzygyan')
txt2('GitHub', 'https://github.com/nitzmali')
txt2('Medium', 'https://medium.com/@nitinmali_68448')

if __name__=='__main__':
    main()