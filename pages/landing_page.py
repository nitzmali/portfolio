import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
from streamlit_timeline import timeline
from widgets import navbar
class Landingpage:
  def run(self):

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
    left_co, right_co = st.columns([1.2, 1.2])
    with right_co:
          st.image("https://github.com/nitzmali/portfolio/blob/main/assets/images/nitin_image_exchange_place.gif?raw=true",width=300)
    
    
    with left_co:
      #st.write("# Hi, I'm Nitin! 👋 ")
      st.markdown("""
      <style>
          h1, p{
          text-align: left;
          margin-top: 0;
          margin-bottom: 0;
          padding-top: 50px;
          padding-bottom: 0;}
      </style>
      <h1> Hi, I'm Nitin! 👋 </h1>
      <p><i> I'm on a quest to unlock the potential of AI, making it an accessible ally for professionals to redefine the boundaries of what's possible in their business landscapes.</i></p>
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
            <p>I weave the art of product innovation with the precision of data science, transforming the complex tapestry of data into actionable insights. At the heart of my journey lies a pivotal role at ZS, where I have pioneered analytics and strategic solutions. My adventures at Aktana, Webmd and Bristol Myers Squib have sharpened my acumen, showcasing my adaptability across diverse industries.</p>
            <p>My unwavering mission is to distill vast oceans of data into potent elixirs of business intelligence, fuelling the growth of enterprises in this data-driven era. I navigate the realms of AI, Product Analytics, and Strategic Planning with an alchemist’s touch, melding them into transformative business strategies.</p>
            
          <h3 class="highlight">Key Expertise:</h3>
            <ul>
                <li>Orchestrating the symphony of Product Data Science and Analytics</li>
                <li>Data Infrastructure & Engineering on AWS</li>
                <li>Mastering the enigmas of Big Data, Machine Learning, and Natural Language Processing</li>
                <li>Choreographing data-driven ballets in Analytics and Business Strategy</li>
            </ul>

          <h3 class="highlight">Professional Skills:</h3>
            <ul>
                <li>Weaving narratives that resonate, honing Communication into an art form</li>
                <li>Polishing Business Acumen to a mirror sheen, reflecting the needs and potentials of markets</li>
                <li>Problem-Solving with the finesse of a chess grandmaster, strategizing several moves ahead</li>
                <li>Orchestrating Team Dynamics to create symphonies of collaborative success</li>
            </ul>
          <p>My arsenal brims with tools like Python, Spark, Adobe Analytics, and Advanced Excel, complemented by the robust platforms of Snowflake and AWS RDS. From the depths of Postgres and Oracle SQL to the peaks of MySQL and MongoDB, I traverse databases with ease. My visualization canvas stretches from Tableau to the artistic strokes of Matplotlib and Ggplot2, all while navigating the cloudscapes of AWS services. I am also proficient in a variety of statistical methods and machine learning techniques. In this odyssey of data, my role as a Product Data Scientist is not just a profession, but a calling – to turn the unseen into the unforgettable, and the complex into the compelling.</p>
        </div>
        <hr>
        <h2 style='text-align: left; color: black; padding-top: 0; padding-bottom: 0;'>Career Timeline</h2>
    """, unsafe_allow_html=True)

        
    # load data
    with open('data/example_time_line_nitin.json', "r") as f:
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
  Landingpage().run()