import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
from streamlit_timeline import timeline
from widgets import navbar
from pages_2.project_details_page_data import ProjectDetailsPageData
from hydralit import HydraHeadApp
class ProjectPage(HydraHeadApp):
    def run(self):
        if 'current_page' not in st.session_state:
            st.session_state.current_page = 'PROJECTS'
        if 'selected_project' not in st.session_state:
            st.session_state.selected_project = None

        st.markdown("""
            <style>
            .card {
                margin-bottom: 20px;
                border-radius: 10px;
                border: none;
                box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
            }
            .card-body {
                padding: 15px;
            }
            .card-title {
                margin-bottom: 15px;
                font-weight: bold;
            }
            .card-text {
                font-size: 14px;
                margin-bottom: 15px;
            }
            .image {
                height: auto;
                max-height: 400px;
                width: 100%;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
                object-fit: contain;
                border: 0.5px solid #000000; /* Add a border to the image */
            }
            .streamlit-button {
                margin-top: 10px;
                border-radius: 5px;
            .streamlit-expander-header { /* Adjust the styling for the expander header */
                font-size: 16px;
                font-weight: bold;
            }
            .streamlit-expander { /* Adjust the styling for the expander */
                margin-top: 0px;
                border-top: none;
                position: absolute;
                bottom: 0;
                left: 0;
            }
            
            </style>
        """, unsafe_allow_html=True)

        import base64
        # Function to convert PDF file to base64
        def get_base64_of_pdf(pdf_file_path):
            with open(pdf_file_path, "rb") as pdf_file:
                return base64.b64encode(pdf_file.read()).decode('utf-8')
        def return_pdf_embed(pdf_file_path):
            base64_pdf = get_base64_of_pdf(pdf_file_path)
            # Embed the PDF in the app
            pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
            return pdf_display

        # Assuming you have a PDF file named 'example.pdf' in the same directory as your Streamlit script
        pdf_file_path_smart_dustbin_project = 'assets/documents/Smart_Dustbin_manthan.pdf'
        pdf_file_path_isro_project = 'assets/documents/ISRO.pdf'
        # Sample project data
        projects = ProjectDetailsPageData().projects
        
        def create_tabs(project,pdf=True):
            with st.expander("View More",expanded=False):
                tab1, tab2, tab3 = st.tabs(["Details", "Code", "Conclusion"])

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


        # Number of columns for the grid
        cols_per_row = 2
        def is_iframe(image_string):
            return "<iframe" in image_string
        
        def assign_and_redirect(title):
            st.session_state.selected_project = title
            self.assign_session(st.session_state, 'PROJECTS DETAILS')
            self.do_redirect('PROJECTS DETAILS')

        # Create the card layout
        for i in range(0, len(projects), cols_per_row):
            cols = st.columns(cols_per_row)
            for j in range(cols_per_row):
                if i + j < len(projects):
                    project = projects[i + j]
                    if is_iframe(project["image"]):
                        # If it's an iframe, render it directly
                        media_html = project["image"]
                    else:
                        # If it's an image URL, use the img tag
                        media_html = f'<img class="image" src="{project["image"]}" alt="{project["title"]}">'

                    with cols[j]:
                        st.markdown(f"""
                            <div class="card">
                                {media_html}
                                <div class="card-body">
                                    <h5 class="card-title">{project['title']}</h5>
                                    <p class="card-text">{project['description']}</p>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
                        #create_tabs(project,project["pdf"])
                        if st.button("View More",key=project["title"]+'i'+'j'):
                            assign_and_redirect(project['title'])

                st.markdown("""
                    <hr style="
                        border: none; 
                        height: 1px; 
                        background: linear-gradient(to right, #B2DFDB 0%, #B2DFDB 100%); 
                        margin-top: 0px; 
                        margin-bottom: 0px;">
                """, unsafe_allow_html=True)



                #st.markdown('<hr style="border:2px solid #008080; width:50%; margin:auto;"/>', unsafe_allow_html=True)

   







            




