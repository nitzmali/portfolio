import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
from streamlit_timeline import timeline
from widgets import navbar
class ProjectPage:
    def run(self):
        projects = [
            {
                "name": "Project 1",
                "algorithm": "Algorithm used in Project 1",
                "introduction": "Brief introduction of Project 1",
                "details": "Detailed explanation of Project 1",
                "insights": "Insights from Project 1",
                "visualizations": "URL_to_visualization_1",  # or path to local file
                "code": "URL_to_code_repository_1",
                "conclusion": "Conclusion of Project 1"
            },
            # Add more projects in a similar structure
        ]

        selected_project = st.sidebar.selectbox("Select a Project", [p["name"] for p in projects])
        project = next(p for p in projects if p["name"] == selected_project)

        st.title(project["name"])
        st.markdown(f"**Algorithm:** {project['algorithm']}")
        st.markdown(f"**Introduction:** {project['introduction']}")

        if st.checkbox("Show Visualizations"):
            #st.image(project['visualizations'], caption="Project Visualization")
            st.markdown("VIZ")

        metric1 = st.slider("Select Metric 1 Value", min_value=0.0, max_value=1.0, value=0.5)
        # Display something based on slider value

        tab1, tab2, tab3 = st.tabs(["Details", "Code", "Conclusion"])

        with tab1:
            st.write(project["details"])

        with tab2:
            st.markdown(f"[Code Repository]({project['code']})")

        with tab3:
            st.write(project["conclusion"])





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
                height: 100%;
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

        # Assuming you have a PDF file named 'example.pdf' in the same directory as your Streamlit script
        pdf_file_path = 'assets/documents/Smart_Dustbin_manthan.pdf'
        base64_pdf = get_base64_of_pdf(pdf_file_path)

        # Embed the PDF in the app
        pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'


        # Sample project data
        projects = [
            {
                "title": "Go Mad Android App",
                "image": "https://github.com/nitzmali/portfolio/blob/main/assets/images_resized/gomad.png?raw=true",
                "description": "Harmonizing Innovation: The Dual-Melody Android App",
                "details": "In a blend of creativity and technology, we developed an Android application that introduces a new way of experiencing music—delivering distinct songs to each ear. This app redefines personal audio by allowing users to immerse themselves in two different audio streams simultaneously, one for each ear. It's a symphony of innovation designed to cater to the diverse auditory preferences of the user, perfect for those moments when one melody is simply not enough.",
                "insights": "Insights from Project 1",
                "visualizations": "URL_to_visualization_1", 
                "code": "URL_to_code_repository_1",
                "conclusion": "Conclusion of Project 1"
            },
            {
                "title": "Smart Dustbin",
                "image": "https://youtu.be/09odCLopdrc?si=Vgr8L8ltDlQnXXjR",
                "description": "Revolutionizing Waste Management with Smart Dustbin",
                "details":F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>',
                "insights": "Insights from Project 1",
                "visualizations": "URL_to_visualization_1",  # or path to local file
                "code": "URL_to_code_repository_1",
                "conclusion": "Conclusion of Project 1"
            },
            # Add more projects as needed...
        ]

        def create_tabs(project,pdf=True):
            with st.expander("View More",expanded=False):
                tab1, tab2, tab3 = st.tabs(["Details", "Code", "Conclusion"])

                with tab1:
                    if not pdf:
                        st.write(project["details"])
                    else:
                        st.markdown(pdf_display, unsafe_allow_html=True)

                with tab2:
                    st.markdown(f"[Code Repository]({project['code']})")

                with tab3:
                    st.write(project["conclusion"])


        # Number of columns for the grid
        cols_per_row = 3

        # Create the card layout
        for i in range(0, len(projects), cols_per_row):
            cols = st.columns(cols_per_row)
            for j in range(cols_per_row):
                if i + j < len(projects):
                    project = projects[i + j]
                    st.header("This is ",str(j))
                    with cols[j]:
                        st.markdown(f"""
                            <div class="card">
                                <img class="image" src="{project['image']}" alt="{project['title']}">
                                <div class="card-body">
                                    <h5 class="card-title">{project['title']}</h5>
                                    <p class="card-text">{project['description']}</p>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
                        create_tabs(project)







            




