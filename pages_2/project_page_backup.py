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

        for project in projects:
            with st.expander(project["name"]):
                st.markdown(f"**Algorithm Name:** {project['algorithm']}")
                st.markdown(f"**Introduction:** {project['introduction']}")
                st.markdown(f"**Project Details:** {project['details']}")
                st.markdown(f"**Model Insights:** {project['insights']}")
                
                # Visualization - ensure the link is valid or file exists
                #st.image(project['visualizations'], caption="Project Visualization")

                # Link to code
                st.markdown(f"[Code Repository]({project['code']})")

                st.markdown(f"**Conclusion:** {project['conclusion']}")

