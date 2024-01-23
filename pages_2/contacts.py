import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
#import streamlit.components.v1 as components
from streamlit_timeline import timeline
from widgets import navbar
import json
from widgets import navbar,sankey_work_experience

class ContactsPage:
  def run(self):

    st.title("Contact Me")
    st.image("https://github.com/nitzmali/portfolio/blob/main/assets/images/nitin_image_exchange_place.gif?raw=true",width=300)

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
        <ul>
            <li>🌐: <a href="https://mroneai.com" target="_blank">mroneai.com</a></li>
            <li>🔗: <a href="https://linkedin.com/in/nitsmali" target="_blank">linkedin.com/in/nitsmali</a></li>
            <li>🐙: <a href="https://github.com/nitzmali" target="_blank">github.com/nitzmali</a></li>
            <li>✉️: <a href="mailto:nitsmali@hotmail.com">nitsmali@hotmail.com</a></li>
            <li>📞: (908)-275-7808</li>
        </ul>
        </div>
        <hr>
    """, unsafe_allow_html=True)

        # Further details can be added here based on the selected company
    #st.download_button(label="Download Resume", data="Your resume content", file_name="assets/documents/Mali_Nitin_Resume_DS.pdf", mime="application/pdf")
    # Provide the path to your local PDF file
    file_path = 'assets/documents/Mali_Nitin_Resume_DS.pdf'
        # Read the PDF file into bytes
    with open(file_path, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name="Mali_Nitin_Resume_DS.pdf",
        mime="application/pdf"
    )


        # use full page width
    #st.set_page_config(page_title="Timeline Example", layout="wide")
        # load data







if __name__=='__main__':
  ContactsPage().run()