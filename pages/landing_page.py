import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
from streamlit_timeline import timeline

class Landingpage:
  def render(self):

    #st.markdown("<h1 style='text-align: left; color: black;'>Nitin Mali</h1>", unsafe_allow_html=True)
    with st.sidebar:
       submit_button = st.button(label="*Download Resume*")
    '''
    left_co, cent_co,last_co = st.columns(3)
    with left_co:
        st.markdown("![Alt Text](https://media.giphy.com/media/CVtNe84hhYF9u/giphy.gif)")
        st.write("")
    
    '''
    # Profile Picture
    left_co, right_co = st.columns([1.2, 1.8])
    with right_co:
          st.image("https://github.com/nitzmali/portfolio/blob/main/assets/images/profile_picture-PhotoRoom.png?raw=true",width=250)
    
    
    with left_co:
      #st.write("# Hi, I'm Nitin! 👋 ")
      st.markdown("""
      <style>
          h1 {
          text-align: right;
          margin-top: 0;
          margin-bottom: 0;
          padding-top: 0;
          padding-bottom: 0;}
      </style>
      <h1> Hi, I'm Nitin! 👋 </h1>
  """, unsafe_allow_html=True)
       
    
    # Brief Introduction
    st.markdown("""
        <style>
            .about-container {
                color: #4f4f4f; /* Adjust the color as needed */
                text-align:left;
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
            .about-container h2, .about-container h3 {
            margin-top: 0;
            margin-bottom: 0;
            text-align: left;
            }
            /* Ensure that there is no extra space inherited from global styles */
            .about-container * {
            margin-top: 0;
            margin-bottom: 0;
            padding-top: 0;
            padding-bottom: 0;
            }
        </style>
        <div class="about-container">
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
                <li>Team Dynamics</li><br>
            </ul>
        </div>
    """, unsafe_allow_html=True)

        
    # load data
    with open('/Users/nyzy/nitzmali/portfolio/data/example_time_line_nitin.json', "r") as f:
        data = f.read()

    #st.markdown("<h2 style='text-align: left; color: black;'>Career Timeline</h1>", unsafe_allow_html=True)
    '''
    st.markdown("""
        <style>
            h1 {text-align: left;
            margin-top: 0;
            margin-bottom: 0;
            padding-top: 0;
            padding-bottom: 0;}
        </style>
        <h1> Career Timeline </h1>
    """, unsafe_allow_html=True)
    '''
    timeline(data, height=800)



    

if __name__=='__main__':
  Landingpage().render()