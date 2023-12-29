import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
from streamlit_timeline import timeline
import json


class AboutPage:
  def render(self):

    st.title("About Me")

    # Profile Picture
    left_co, cent_co,last_co = st.columns([1.15,1,1])
    with cent_co:
          st.image("/Users/nyzy/nitzmali/portfolio/assets/images/profile_picture.jpg",width=200)
  

    # Brief Introduction
    st.markdown("""
        <style>
            .about-container {
                color: #4f4f4f; /* Adjust the color as needed */
            }
            .about-header {
                color: #2874A6; /* Header color */
            }
            .highlight {
                color: #2E86C1; /* Highlights or key points */
            }
            .career-highlight {
                color: #21618C; /* Career highlights color */
                font-weight: bold;
            }
        </style>
        <div class="about-container">
            <h1 class="about-header">Nitin Mali</h1>
            <h2>Senior Data Scientist at ZS | AI & Data Science Expert | Advanced Analytics and BI Specialist</h2>
            <h2>Located in New York, United States</h2>
            <hr>
            <p>I am a seasoned data scientist with a proven track record of leveraging advanced analytics and machine learning to transform complex data into actionable business solutions. Currently excelling in a pivotal role at ZS, my career has been marked by innovative analytics and strategic contributions. My engagement at Aktana and Xsunt significantly enhanced my proficiency in the analytics domain, underscoring my versatility across various industries.</p>
            <p>My primary goal remains unwavering: to extract actionable intelligence from vast data sets and empower businesses to thrive in a data-centric world. My expertise spans AI, Data Science, Advanced Analytics, Sales and Product Analytics, Strategic Planning, and Business Strategy.</p>
            
          <h3 class="highlight">Key Expertise:</h3>
            <ul>
                <li>Data Science and Analytics</li>
                <li>Data Infrastructure & Engineering on AWS</li>
                <li>Big Data, Machine Learning, & NLP</li>
                <li>Analytics & Business Strategy</li>
            </ul>

          <p>My technical toolkit includes Python, Spark, Adobe Analytics, Advanced Excel, Snowflake, AWS RDS, Postgres, Oracle SQL, MySQL, MongoDB, Tableau, Matplotlib, Ggplot2, and AWS Cloud services. I am also proficient in a variety of statistical methods and machine learning techniques.</p>

          <h3 class="highlight">Professional Skills:</h3>
            <ul>
                <li>Communication</li>
                <li>Business Acumen</li>
                <li>Problem-Solving</li>
                <li>Team Dynamics</li>
            </ul>

          <h3 class="career-highlight">Career Highlights:</h3>
            <p>Senior Data Scientist, ZS (Jan 2023 - Present): Utilized Random Forest and Gradient Boosted Trees to enhance sales trend predictions, achieving a 15% YoY sales increase. Implemented NLP techniques for product feedback analysis, leading to significant product improvements and feature enhancements.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("## Career Timeline")

    # Example Entry in Timeline
    col1, col2 = st.columns([1, 4])
    with col1:
        st.text("2023 - Present")
    with col2:
        st.markdown("""
        **Senior Data Scientist**  
        Company XYZ  
        Brief description of your role and key achievements.
        """)

        # use full page width
    #st.set_page_config(page_title="Timeline Example", layout="wide")

    # load data
    with open('/Users/nyzy/nitzmali/portfolio/data/example_time_line_nitin.json', "r") as f:
        data = f.read()


    image_url = "https://github.com/nitzmali/portfolio/blob/main/assets/images/profile_picture.jpg?raw=true"
    image_url = "assets/images/profile_picture.jpg"
    '''
    with open("/Users/nyzy/nitzmali/portfolio/data/example_time_line_nitin.json") as f:
       data = json.load(f)
    data["events"][0]["media"]["url"]=st.image(image_url, width=200)
    print(data["events"][0]["media"]["url"])
    '''
# Use Streamlit's st.image to render the image with a specific width
    st.image(image_url, width=200) 
    # render timeline
    timeline(data, height=800)




if __name__=='__main__':
  AboutPage().render()
  AboutPage().display_resume()