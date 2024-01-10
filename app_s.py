# main_app.py
import streamlit as st
from hydralit import HydraApp
from pages.landing_page import Landingpage
from pages.about_page import AboutPage
from pages.projects_page import ProjectPage
from pages.work_experience_page import WorkExperiencePage
# Import other pages as needed
import streamlit as st
#from streamlit.components.v1 import html
from PIL import Image
from widgets import navbar
#import streamlit.components.v1 as components
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

@app.addapp(title='HOME')
def HOME(title='Home',is_home=True):
    Landingpage().run()
    navbar.render_footer()
    
@app.addapp(title='WORK EXPERIENCE')
def WORK_EXPERIENCE():
    WorkExperiencePage().run()
    navbar.render_footer()

@app.addapp()
def PROJECTS(title='PROJECTS'):
    ProjectPage().run()
    navbar.render_footer()



# Run the app
if __name__ == "__main__":
    app.run()
