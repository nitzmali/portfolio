import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
from streamlit_timeline import timeline

import base64
from streamlit_lottie import st_lottie
import requests
import json
class Landingpage:
  def run(self):

    #st.markdown("<h1 style='text-align: left; color: black;'>Nitin Mali</h1>", unsafe_allow_html=True)
    #with st.sidebar:
       #submit_button = st.button(label="*Download Resume*")
    '''
    left_co, cent_co,last_co = st.columns(3)
    with left_co:
        st.markdown("![Alt Text](https://media.giphy.com/media/CVtNe84hhYF9u/giphy.gif)")
        st.write("")
    
    '''
    # Profile Picture
    left_co, right_co = st.columns([1.2, 0.6])
    with right_co:
            #st.image("https://github.com/nitzmali/portfolio/blob/main/assets/images/nitin_image_exchange_place.gif?raw=true",width=300)

            with open("assets/images/Animation - 1705963227290.json", "r",errors='ignore') as f:
                data = json.load(f)
            st_lottie(data,width=350, height=350)
    
    
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
    timeline(data, height=600)


    def render_svg(svg):
        """Renders the given svg string."""
        b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
        html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
        st.write(html, unsafe_allow_html=True)
    '''
    f = open("assets/images/21852411_sysadmin_03.svg","r")
    lines = f.readlines()
    line_string=''.join(lines)
    render_svg(line_string)
    '''




    

if __name__=='__main__':
  Landingpage().run()