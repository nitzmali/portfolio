import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
from streamlit_timeline import timeline
import matplotlib.pyplot as plt
from streamlit.components.v1 import html
import json
from widgets import sankey_work_experience
from streamlit_extras.switch_page_button import switch_page
from hydralit import HydraHeadApp
from widgets import navbar
import base64
from pages_2.project_details_page_data import ProjectDetailsPageData
class WorkExperienceDetailsApp(HydraHeadApp):
    def run(self):
        #top_placeholder.markdown("#")

        if 'selected_project' not in st.session_state:
            st.session_state.selected_project = None

                
        # Function to convert PDF file to base64
        def get_base64_of_pdf(pdf_file_path):
            with open(pdf_file_path, "rb") as pdf_file:
                return base64.b64encode(pdf_file.read()).decode('utf-8')
        def return_pdf_embed(pdf_file_path):
            base64_pdf = get_base64_of_pdf(pdf_file_path)
            # Embed the PDF in the app
            pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1600" height="1000" type="application/pdf"></iframe>'
            return pdf_display
        def create_tabs(project,pdf=True):
                    st.markdown("""
                        <style>

                            .stTabs [data-baseweb="tab-list"] {
                                gap: 100px;
                            }

                            .stTabs [data-baseweb="tab"] {
                                height: 50px;
                                white-space: pre-wrap;
                                #background-color: #F0F2F6;
                                border-radius: 4px 4px 4px 4px;
                                gap: 100px;
                                padding-top: 10px;
                                padding-bottom: 10px;
                            }
                            p {
                                font-size:1rem;
                            }
                            .stTabs [aria-selected="true"] {
                                background-color: #FFFFFF;
                            }

                        </style>""", unsafe_allow_html=True)
                    
                    '''
                    tab1, tab2, tab3 = st.tabs(["Details 🔍", "Code 💻", "Conclusion ✅"])

                    

                    with tab1:
                        if not pdf:
                            st.markdown(project["details"], unsafe_allow_html=True)
                        else:
                            st.markdown(return_pdf_embed(project["pdf_file_path"]), unsafe_allow_html=True)

                    with tab2:
                        st.markdown(f"[Code Repository]({project['code']})")
                        # Create the nbviewer URL for your notebook
                        if project["title"]=="Income and BMI Prediction":
                            st.write("House Income Data Preparation")
                            github_url = 'https://github.com/nitzmali/BMI_PREDICTION/blob/main/1.1%20-%20Data_Preparation%20%5BHH%5D.ipynb?raw=true'
                            nbviewer_url = github_url.replace('github.com', 'nbviewer.jupyter.org/github')
                            st.markdown(f'<iframe src="{nbviewer_url}" width="100%" height="800" frameborder="0"></iframe>', unsafe_allow_html=True)
                            st.write("House Income Data Exploration")
                            github_url = 'https://github.com/nitzmali/BMI_PREDICTION/blob/main/1.2%20-%20Data%20Exploration%20%5BHH%5D.ipynb?raw=true'
                            nbviewer_url = github_url.replace('github.com', 'nbviewer.jupyter.org/github')
                            st.markdown(f'<iframe src="{nbviewer_url}" width="100%" height="800" frameborder="0"></iframe>', unsafe_allow_html=True)
                            st.write("House Income Modelling")
                            github_url = 'https://github.com/nitzmali/BMI_PREDICTION/blob/main/1.3%20-%20Encoding%20and%20%20Modelling%20%5BHH%5D.ipynb?raw=true'
                            nbviewer_url = github_url.replace('github.com', 'nbviewer.jupyter.org/github')
                            st.markdown(f'<iframe src="{nbviewer_url}" width="100%" height="800" frameborder="0"></iframe>', unsafe_allow_html=True)
                            st.write("BMI Data Preparation")
                            github_url = 'https://github.com/nitzmali/BMI_PREDICTION/blob/main/1.2%20-%20Data%20Exploration%20%5BHH%5D.ipynb?raw=true'
                            nbviewer_url = github_url.replace('github.com', 'nbviewer.jupyter.org/github')
                            st.markdown(f'<iframe src="{nbviewer_url}" width="100%" height="800" frameborder="0"></iframe>', unsafe_allow_html=True)
                            st.write("BMI Data Exploration")
                            github_url = 'https://github.com/nitzmali/BMI_PREDICTION/blob/main/2.2%20-%20Data%20Exploration%20%5BBMI%5D.ipynb?raw=true'
                            nbviewer_url = github_url.replace('github.com', 'nbviewer.jupyter.org/github')
                            st.markdown(f'<iframe src="{nbviewer_url}" width="100%" height="800" frameborder="0"></iframe>', unsafe_allow_html=True)
                            st.write("BMI -- Regression Machine Learning Model")
                            github_url = 'https://github.com/nitzmali/BMI_PREDICTION/blob/main/2.3%20-%20Encoding%20and%20Modelling%20%5BBMI%5D.ipynb?raw=true'
                            nbviewer_url = github_url.replace('github.com', 'nbviewer.jupyter.org/github')
                            st.markdown(f'<iframe src="{nbviewer_url}" width="100%" height="800" frameborder="0"></iframe>', unsafe_allow_html=True)

                        if project["title"]=="AI Powered Job Transition Pathway using Generative LSTM Models":
                            st.write("## Data Loading and Processing")
                            github_url = 'https://github.com/nitzmali/job_transition_pathway/blob/main/notebooks/data_process.ipynb?raw=true'
                            nbviewer_url = github_url.replace('github.com', 'nbviewer.jupyter.org/github')
                            st.markdown(f'<iframe src="{nbviewer_url}" width="100%" height="800" frameborder="0"></iframe>', unsafe_allow_html=True)
                            st.write("## Clustering Job Ttiles using Spacy")
                            github_url = 'https://github.com/nitzmali/job_transition_pathway/blob/main/notebooks/build_clustering_titles_skills_iden_models.ipynb?raw=true'
                            nbviewer_url = github_url.replace('github.com', 'nbviewer.jupyter.org/github')
                            st.markdown(f'<iframe src="{nbviewer_url}" width="100%" height="800" frameborder="0"></iframe>', unsafe_allow_html=True)
                            st.write("## Generate Synthetic data to map job transitions")
                            github_url = 'https://github.com/nitzmali/job_transition_pathway/blob/main/notebooks/jobs_data_generation.ipynb?raw=true'
                            nbviewer_url = github_url.replace('github.com', 'nbviewer.jupyter.org/github')
                            st.markdown(f'<iframe src="{nbviewer_url}" width="100%" height="800" frameborder="0"></iframe>', unsafe_allow_html=True)
                            st.write("## Job Prediction")
                            github_url = 'https://github.com/nitzmali/job_transition_pathway/blob/main/notebooks/final_models/job_prediction.ipynb?raw=true'
                            nbviewer_url = github_url.replace('github.com', 'nbviewer.jupyter.org/github')
                            st.markdown(f'<iframe src="{nbviewer_url}" width="100%" height="800" frameborder="0"></iframe>', unsafe_allow_html=True)
                            st.write("## Skills Prediction")
                            github_url = 'https://github.com/nitzmali/job_transition_pathway/blob/main/notebooks/final_models/skills_prediction.ipynb?raw=true'
                            nbviewer_url = github_url.replace('github.com', 'nbviewer.jupyter.org/github')
                            st.markdown(f'<iframe src="{nbviewer_url}" width="100%" height="800" frameborder="0"></iframe>', unsafe_allow_html=True)
                            st.write("## Course Prediction")
                            github_url = 'https://github.com/nitzmali/job_transition_pathway/blob/main/notebooks/final_models/course_prediction.ipynb?raw=true'
                            nbviewer_url = github_url.replace('github.com', 'nbviewer.jupyter.org/github')
                            st.markdown(f'<iframe src="{nbviewer_url}" width="100%" height="800" frameborder="0"></iframe>', unsafe_allow_html=True)    

                    with tab3:
                        st.write(project["conclusion"])
                    '''
        projects = ProjectDetailsPageData().work_experience_projects
        #st.write(st.session_state)
        # Find the project details using the project name
        project_name = st.session_state.selected_project
        #project_name = 'Machine Learning Image Colorization'
        project = next((proj for proj in projects if proj["title"] == project_name), None)
        # Back button to return to the main page
        if st.button('⬅️',key="1"):
            if st.session_state.current_page=='PROJECTS':
            # Explicitly set the session state to go back to the WORK EXPERIENCE page
            #st.session_state.current_page = 'work experience page'
                st.session_state.selected_project = None
                self.assign_session(st.session_state,'HOME')
                self.do_redirect('PROJECTS')
            else:
                st.session_state.selected_project = None
                self.assign_session(st.session_state,'HOME')
                self.do_redirect('WORK EXPERIENCE')
        
        if project is not None:

            #col1, col2 = st.columns([4.5, 6])
            #col3, col4 = st.columns([2.5, 6])

            def is_iframe(image_string):
                        return "<iframe" in image_string
                    
            if is_iframe(project["image"]):
                # If it's an iframe, render it directly
                media_html = project["image"]
            else:
                # If it's an image URL, use the img tag
                media_html = f'<img class="image" src="{project["image"]}" alt="{project["title"]}">'
            '''
            css_style1 = """
                    <style>
                    .centered {
                        text-align: center; /* Center text */
                        margin: auto;      /* Center in a column */
                        padding:5px;
                        #font-weight: bold;
                        font-size:2rem;
                    }
                    img {
                        display: grid;    /* Block display */
                        margin-left: auto; /* Center image horizontally */
                        margin-right: auto;
                        transform: scale(0.8);
                        height: 500px;
                        width: 700px;
                        #border: 1px solid black;
                        box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2); 
                        transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth transition for hover effects */
                    }
                    /*.img:hover {
                    box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.3); /* Enhance shadow on hover */
                }*/

                    </style>
                    """

            with st.container():
                    st.markdown(css_style1, unsafe_allow_html=True)
                    st.markdown(f"<div class='centered'> {project_name}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='img'>{media_html}</div>", unsafe_allow_html=True)
                
            #tab1, tab2, tab3 = st.tabs(["Details", "Code", "Conclusion"])

            #with tab1:
                #st.markdown(project["details"], unsafe_allow_html=True)
            st.markdown('###')
            #with st.expander("Details",expanded=False):
                #create_tabs(project,project["pdf"])

            css_style3 = """
            <style>
            .expander-header {
                font-weight: bold;
                font-size: large;
                text-align: center;
            }
            .expander-content {
                padding: 10px;
                background-color: Gainsboro; /* Light gray background */
                border-radius: 10px; /* Rounded corners for the content */
            }
            </style>
            """

            st.markdown(css_style3, unsafe_allow_html=True)

            # You can add the code for tab2 and tab3 as per your requirements
            '''
            # Back button to return to the main page
            
            st.markdown(
                    """
                <style>
                button {
                    height: 5%;
                    padding-top: 1px !important;
                    padding-bottom: 1px !important;
                }
                </style>
                """,
                    unsafe_allow_html=True,
                )
            css_style1 = """
                <style>
                .centered {
                    text-align: center;  /* Center text */
                    margin: auto;        /* Center in a column */
                    font-size: 2rem;
                    max-width: 900px;
                }


                .details-container {
                    max-width: 900px;    /* Set a maximum width for the content */
                    margin: auto;        /* Center the container */
                    padding-left: 180px; 
                    text-align: left;    /* Align text to the left within the container */
                    font-size: 1rem;     /* Adjust font size as needed */
                }

                img {
                    display: block;      /* Block display for centering */
                    margin: auto;        /* Center image horizontally */
                    transform: scale(0.8);
                    height: 500px;
                    width: 700px;
                    box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2);
                    transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth transition for hover effects */
                }
                </style>

                    """
            st.markdown(css_style1, unsafe_allow_html=True)
            st.markdown(f"<h1 class='centered'>{project['title']}</h1>", unsafe_allow_html=True)
            st.markdown(f"<div class='centered'>{media_html}</div>", unsafe_allow_html=True)

            
            #st.markdown(f"<div class='centered'>{project_name}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='details-container'>{project['description']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='details-container'>{project['details']}</div>", unsafe_allow_html=True)


            
            
            if st.button('⬅️',key="2"):
                if st.session_state.current_page=='PROJECTS':
                    # Explicitly set the session state to go back to the WORK EXPERIENCE page
                    #st.session_state.current_page = 'work experience page'
                    st.session_state.selected_project = None
                    self.assign_session(st.session_state,'HOME')
                    self.do_redirect('PROJECTS')
                else:
                    st.session_state.selected_project = None
                    self.assign_session(st.session_state,'HOME')
                    self.do_redirect('WORK EXPERIENCE')
                
        else:
            st.error("Project not found.")
            st.session_state.selected_project=None
        navbar.render_footer()
        st.markdown('<script>window.scrollTo(0, 0);</script>', unsafe_allow_html=True)
        html(
        """
            <script>
                window.parent.document.querySelector('section.main').scrollTo(0, 0);
            </script>
        """,
        height=0
    )
        
        st.session_state.selected_project = None
        



if __name__ == "__main__":
     
    '''
    if 'selected_project' not in st.session_state:
        st.session_state.selected_project = None
    project_name = st.session_state.selected_project
    #show_project_details_page(project_name)
    '''

