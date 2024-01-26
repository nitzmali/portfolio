import streamlit as st
import streamlit as st
from pages_2.work_experience_page_data import WorkExperiencePageData
from pages_2.project_details_page_data import ProjectDetailsPageData
from hydralit import HydraHeadApp
from streamlit.components.v1 import html
from streamlit_card import card
from streamlit_javascript import st_javascript
class WorkExperiencePage(HydraHeadApp):
  def run(self):
        
        # Initialize session state for selected project
        if 'current_page' not in st.session_state:
            st.session_state.current_page = 'WORK EXPERIENCE'
        if 'selected_project' not in st.session_state:
            st.session_state.selected_project = None
        #if 'selected_project' not in st.session_state:
            #st.session_state.selected_project = None

        #projects = ProjectDetailsPageData().work_experience_projects
        #st.write(st.session_state)
        # Find the project details using the project name
        project_name = st.session_state.selected_project

        
        # Custom CSS to adjust the layout
        st.markdown("""
            <style>
            .job-container {
                display: flex;
                flex-direction: column;
                #margin-top: 230px; 
            }
            .job-title {
                font-size: 18px;
                font-weight: bold;
            }
            .job-company {
                font-size: 24px;
                display: flex;
                align-items: center;
            }
            .job-icon {
                width: 100px;  /* Adjust the size of the icon */
                margin-left: 10px; /* Space between the company name and the icon */
                margin-top: 10px; 
                margin-bottom: 10px;
            }
            .job-period-location {
                font-size: 16px;
                margin-top: 4px;
                margin-bottom: 10px;
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
        def assign_and_redirect(title,key):
            st.session_state.selected_project = title
            self.assign_session(st.session_state, 'WORK EXPERIENCE DETAILS')
            self.do_redirect('WORK EXPERIENCE DETAILS')


        # Number of columns for the grid
        
        uniq_k_b = 0
        cols_per_row = 4
        def is_iframe(image_string):
            return "<iframe" in image_string
        
        work_experience = WorkExperiencePageData().work_experience
        zs_associates_projects = WorkExperiencePageData().zs_associates_projects
        aktana_projects = WorkExperiencePageData().aktana_projects
        bms_projects = WorkExperiencePageData().bms_projects
        temenos_projects = WorkExperiencePageData().temenos_projects
        webmd_projects = WorkExperiencePageData().webmd_projects
        projects_all = ProjectDetailsPageData().projects
        projects_w = ProjectDetailsPageData().work_experience_projects 
        
        companies_projects = ["zs_associates_projects","aktana_projects","bms_projects","webmd_projects","temenos_projects"]
        # Display each job entry
        
        for job_idx,job in enumerate(work_experience):
            company_name = str(job['company']).lower()
            #col1, col2 = st.columns([1, 4])
            #with col1:

                            # Use the image as a clickable link in the HTML string
            st.markdown(f"""
                <div class="job-container">
                    <div class="job-company">
                        <a href="{job['url']}" target="_blank">{job['company']}</a> 
                        <a href="{job['url']}" target="_blank">
                            <img class="job-icon" src="{job['icon']}" alt="{job['company']} Icon">
                        </a>
                    </div>
                    <div class="job-title">{job['role']}</div>
                    <div class="job-period-location">{job['period']} [ {job['location']} ] </div>
                </div>
            """, unsafe_allow_html=True)

            st.markdown("##")

            projects = locals()[companies_projects[job_idx]]
            for i in range(0, len(projects), cols_per_row):
                
                cols = st.columns(cols_per_row)
                for j in range(cols_per_row):
                    uniq_k_b+=1
                    key= f"details-{job_idx}-{i}-{j}-{uniq_k_b}"
                    if i + j < len(projects):
                        project = projects[i + j]
                        if is_iframe(project["image"]):
                            # If it's an iframe, render it directly
                            media_html = project["image"]
                        else:
                            # If it's an image URL, use the img tag
                            media_html = f'<img class="image" src="{project["image"]}" alt="{project["title"]}">'

                        with cols[j]:
                            
                            '''
                            st.markdown(f"""
                                <div class="card">
                                    <div class="card-body">
                                        <p class="card-text">{project['description']}</p>
                                    </div>
                                </div>
                            """, unsafe_allow_html=True)
                            top_placeholder = st.empty()
                            #st.write(st.session_state)
                            if st.button("View Details",key=key):
                                st.session_state.selected_project = project['title']
                                
                                self.assign_session(st.session_state,'HOME')
                                self.do_redirect('PROJECTS DETAILS')
                            '''
                            
                                                            # Define the function to handle the click action


                            import random

                            def generate_random_gradient():
                                # Define a list of color hex codes
                                colors = ["#6dd5ed", "#2193b0", "#ff758c", "#ff7eb3", "#8e2de2", "#4a00e0", "#f7971e", "#ffd200", "#00b09b", "#96c93d"]
                                colors = ["#00b09b", "#0bb498", "#17b895", "#23bc92", "#2fc08f", "#3bc48c", "#47c889", "#53cc86", "#5fd083", "#6bd480", "#77d87d", "#83dc7a", "#8fe077", "#9be474", "#a7e871", "#b3ec6e", "#bff06b", "#cbf468", "#d7f865", "#e3fc62", "#efff5f", "#f7ff5c", "#ffff59", "#ffff56", "#ffff53", "#ffff50", "#ffff4d", "#ffff4a", "#ffff47", "#ffff44"]
                                colors = [
                                        "#4b79a1", "#283e51", "#3b6978", "#204051", "#5b84b1",
                                        "#0e9aa7", "#3da4ab", "#f6cd61", "#fe8a71", "#ff6f69",
                                        "#d4a5a5", "#b8b5ff", "#622569", "#b15d7a", "#8d6262",
                                        "#5b9aa0", "#d5ded9", "#7f9172", "#a8be8b", "#bfdcae",
                                        "#4a536b", "#6c5b7c", "#c06c84", "#f67280", "#f8b595",
                                        "#355c7d", "#6c5b7b", "#c06c84", "#f67280", "#f8b195",
                                        "#99b898", "#fecea8", "#ff847c", "#e84a5f", "#2a363b",
                                        "#2a3132", "#763626", "#336b87", "#2a3132", "#90afc5",
                                        "#763626", "#46211a", "#693d3d", "#ba5536", "#a43820",
                                        "#505160", "#68829e", "#aebd38", "#598234", "#004d47",
                                        "#1e1f26", "#283655", "#4d648d", "#d0e1f9", "#4f6457",
                                        "#3fb0ac", "#4d9de0", "#7768ae", "#e1bc29", "#eb6841"
                                    ]
                                
                                colors = [
                                    "#ffadad", "#ffd6a5", "#fdffb6", "#caffbf", "#9bf6ff",
                                    "#a0c4ff", "#bdb2ff", "#ffc6ff", "#fffffc", "#ffcb69",
                                    "#ff9f1c", "#ff165d", "#ff6d6a", "#f0a6ca", "#b8bedd",
                                    "#6d6875", "#ffcdb2", "#ffb4a2", "#e5989b", "#b5838d",
                                    "#6d6875", "#bde0fe", "#a2d2ff", "#cdb4db", "#ffc8dd",
                                    "#ffafcc", "#bde0fe", "#a2d2ff", "#cdb4db", "#ffc8dd",
                                    "#ffafcc", "#e29578", "#e85d04", "#f48c06", "#faa307",
                                    "#ffba08", "#e0aaff", "#c77dff", "#9b5de5", "#f15bb5",
                                    "#fee440", "#00bbf9", "#00f5d4", "#00bbf0", "#007f5f",
                                    "#2b9348", "#55a630", "#80b918", "#aacc00", "#bfd200",
                                    "#d4a373", "#e76f51", "#f4a261", "#e9c46a", "#2a9d8f",
                                    "#264653", "#2a9d8f", "#e9c46a", "#f4a261", "#e76f51"
                                ]

                                # Randomly select two different colors from the list
                                color1 = random.choice(colors)
                                color2 = random.choice(colors)
                                while color2 == color1:
                                    color2 = random.choice(colors)

                                # Create a linear gradient CSS string
                                gradient = f"linear-gradient(to right, {color1}, {color2})"
                                return gradient
                            st.markdown(f"<div style='margin-left: 70px; height: 60px;overflow: hidden;width: 400px;'>{project['title']} </div>", unsafe_allow_html=True)
                            
                            #st.markdown("##")
                            # Use the card component from streamlit_card library
                            hasClicked = card(
                                title='',
                                text='',
                                image=project['image'],  # Replace with your image URL if available
                                key=uniq_k_b,
                                # Define the action to take on click
                                on_click=lambda: assign_and_redirect(project['title'],key),
                                styles = {
                                    "card": {
                                        "width": "300px",
                                        "height": "150px",
                                        "border-radius": "15px",
                                        "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                                        "margin": "20px",
                                        "transition": "0.5s",
                                        #"background-color": "#ffffff",
                                        "display": "block",
                                        "flex-direction": "column",
                                        "justify-content": "space-between",
                                        "align-items": "center",
                                        "padding": "15px",
                                        "overflow": "hidden",
                                        "position": "relative",
                                        #"background-image": generate_random_gradient(),
                                    },
                                    "title": {
                                        "font-size": "12px",
                                        "color": "#000",
                                    },
                                    "text": {
                                        "font-size": "12px",
                                        "color": "#000",
                                    },
                                    "filter": {
                                        "background-color": "rgba(255, 255, 255, 0.1)", 
                                    },
                                }
                            )
                            


                            # Check if the card was clicked and perform action
                            if hasClicked:
                                assign_and_redirect(project['title'],key)

                                    
                '''
                st.markdown("""
                    <hr style="
                        border: none; 
                        height: 3px; 
                        background: linear-gradient(to right, #B2DFDB 0%, #B2DFDB 100%); 
                        margin-top: 2px; 
                        margin-bottom: 2px;">
                """, unsafe_allow_html=True)
                    
                '''
                    

            st.markdown("""
            <hr style="
                border: none; 
                height: 3px; 
                background: linear-gradient(to right, #000000 0%, #000000 100%);
                margin-top: 2px; 
                margin-bottom: 2px;">
        """, unsafe_allow_html=True)
        projects_ = projects_all + projects_w 
        if project_name!=None:
                    #project_name = 'Machine Learning Image Colorization'
            project = next((proj for proj in projects_ if proj["title"] == project_name), None)
            scroll_position = str(project["scrollPosition"])
            #st.markdown('<script>window.scrollTo(0, 1000);</script>', unsafe_allow_html=True)
            html_script = f"""
                <script>
                    window.parent.document.querySelector('section.main').scrollTo(0, {scroll_position});
                </script>
            """
            html(html_script, height=0)
        else:
            st.markdown('<script>window.scrollTo(0, 0);</script>', unsafe_allow_html=True)
            html(
            """
                <script>
                    window.parent.document.querySelector('section.main').scrollTo(0, 0);
                </script>
            """,
            )


if __name__ == "__main__":
    WorkExperiencePage().run()
