import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components


class Landingpage:
  def render(self):

    st.write('''
    # Nitin Mali
    ## Senior Data Scientist at ZS
    ## B.E - Computer Science, Ms.c - Data Science
    ''')
    with st.sidebar:
       submit_button = st.button(label="*Download Resume*")

            
    image = Image.open('/Users/nyzy/nitzmali/portfolio/assets/images/LPYH.gif')


    left_co, cent_co,last_co = st.columns([0.9,1,1])
    with cent_co:
        st.markdown("![Alt Text](https://media.giphy.com/media/CVtNe84hhYF9u/giphy.gif)")
        st.write("")

if __name__=='__main__':
  Landingpage().render()