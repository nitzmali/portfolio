# main_app.py
import streamlit as st
from hydralit import HydraApp
from pages_2.landing_page import Landingpage
from pages_2.about_page import AboutPage
from pages_2.projects_page import ProjectPage
from pages_2.work_experience_page import WorkExperiencePage
from pages_2.work_experience_project_details import ProjectDetailsApp
from pages_2.work_experience_details import WorkExperienceDetailsApp
from pages_2.about_page import AboutPage
# Import other pages as needed
import streamlit as st
#from streamlit.components.v1 import html
from PIL import Image
from widgets import navbar
import streamlit.components.v1 as components

st.set_page_config(page_title="Nitin Mali",layout="wide",initial_sidebar_state="collapsed")
from st_pages import hide_pages, show_pages, Page



over_theme = {
    'txc_inactive': '#FFEBEE',  # Light Pink: Inactive text color
    'menu_background': '#37474F',  # Dark Slate Grey: Menu background color
    'txc_active': '#FFC107',  # Amber: Active text color
    'option_active': '#B2DFDB'  # Light Turquoise: Active option background color
}
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

# Initialize the Hydra app
app = HydraApp(title='Nitin Mali Portfolio', hide_streamlit_markers=True,use_navbar=True, navbar_sticky=True,navbar_mode='pinned',use_cookie_cache=True, navbar_animation=True,navbar_theme=over_theme)
#
@app.addapp(title='HOME',is_home=True)
def HOME():
    Landingpage().run()
    navbar.render_footer()
    
@app.addapp(title='WORK EXPERIENCE')
def WORK_EXPERIENCE():
    WorkExperiencePage().run()
    navbar.render_footer()

@app.addapp(title='ABOUT')
def ABOUT():
    AboutPage().run()
    navbar.render_footer()

@app.addapp(title='PROJECTS')
def PROJECTS():
    ProjectPage().run()
    navbar.render_footer()

@app.addapp(title='PROJECTS DETAILS')
def PROJECTS_DETAILS():
    ProjectDetailsApp().run()
    #navbar.render_footer()

@app.addapp(title='WORK EXPERIENCE DETAILS')
def WORK_EXPERIENCE_DETAILS():
    WorkExperienceDetailsApp().run()
    #navbar.render_footer()





# Run the app
if __name__ == "__main__":
    complex_nav = {
        'WORK EXPERIENCE': ['WORK EXPERIENCE'],
        'ABOUT': ['ABOUT'],
        'PROJECTS': ['PROJECTS'],

        #'PROJECTS DETAILS': ['PROJECTS DETAILS']

    }
    app.run(complex_nav)
