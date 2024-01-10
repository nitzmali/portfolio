import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
from streamlit_timeline import timeline
from widgets import navbar,sankey_work_experience
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
        <p>I weave the art of innovation with the precision of data science, transforming the complex tapestry of data into actionable insights. At the heart of my journey lies a pivotal role at ZS, where I have pioneered data and strategic solutions. My adventures at Aktana, Webmd, Bristol Myers Squib and Temenos have sharpened my acumen, showcasing my adaptability across diverse industries.</p>
        <p>My unwavering mission is to distill vast oceans of data into potent elixirs of business intelligence, fuelling the growth of enterprises in this data-driven era. I navigate the realms of AI, Product Analytics, and Strategic Planning with an alchemist’s touch, melding them into transformative business strategies.</p>
        <hr>
        <hr>
        <h3 class="highlight">Education</h3>
        <h4>Rutgers University</h4>
        <p><strong>     Master of Science (M.S) in Data Science</strong> | GPA: 3.7 | Jan 2017 - May 2018</p>
        <h4>M.S. Ramaiah Institute of Technology</h4>
        <p><strong>     Bachelor of Engineering (B.E) in Computer Science Engineering</strong> | GPA: 3.7 | Jul 2011 - May 2015</p>
        <hr>
        <h3 class="highlight">Contact Information</h3>
        <ul>
            <li>🌐: <a href="https://mroneai.com" target="_blank">mroneai.com</a></li>
            <li>🔗: <a href="https://linkedin.com/in/nitsmali" target="_blank">linkedin.com/in/nitsmali</a></li>
            <li>🐙: <a href="https://github.com/nitzmali" target="_blank">github.com/nitzmali</a></li>
            <li>✉️: <a href="mailto:nitsmali@hotmail.com">nitsmali@hotmail.com</a></li>
            <li>📞: <a href="tel:+19082757808">(908)-275-7808</a></li></li>
        </ul>
        </div>
        <hr>
    """, unsafe_allow_html=True)

         # Create columns where the first one is empty and acts like a left margin
    left_margin, chart_column = st.columns([1, 20])  # Adjust the ratio to control the offset
                                # Add a button to download the resume
    

     # Render the chart in the right column
    with chart_column:
        st.plotly_chart(sankey_work_experience.render_image())  

        st.markdown("""<h2 style='text-align: left; color: black; padding-top: 0; padding-bottom: 0;'>Career Timeline</h2>""",unsafe_allow_html=True)

        
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