# main_app.py

import streamlit as st
from streamlit.components.v1 import html
from PIL import Image
import streamlit.components.v1 as components
st.set_page_config(page_title="Nitin Mali",layout="wide",initial_sidebar_state="collapsed")
from pages.page_2 import main
from pages.landing_page import Landingpage
from pages.about_page import AboutPage
from widgets import navbar
PAGES = {
    "Home": Landingpage().render,
    "About":AboutPage().render
    # ... other pages
}

class PortfolioApp:

    def __init__(self):
        self.page_router()
        pass

    def page_router(self):
        page = st.sidebar.selectbox("Navigate", list(PAGES.keys()))
        
        # Call the appropriate page function
        if page in PAGES:
            page_function = PAGES[page]
            page_function()  # Call the function

if __name__ == "__main__":
    #navbar.custom_css()
    navbar.render_navbar()

    PortfolioApp()
    from st_pages import hide_pages, show_pages, Page

    show_pages(
        [
            Page("app_s.py"),
            Page("pages/landing_page.py")
        ]
    )
    navbar.render_footer()
    
    