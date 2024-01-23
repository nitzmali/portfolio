from hydralit import HydraHeadApp, HydraApp
import streamlit as st

class WorkExperienceApp(HydraHeadApp):
    def run(self):
        # Your code for the Work Experience page
        if st.button('Go to Project Details'):
            self.do_redirect('Project Details')

class ProjectDetailsApp(HydraHeadApp):
    def run(self):
        # Your code for the Project Details page
        if st.button('Go Back'):
            self.do_redirect('WORK EXPERIENCE')

if __name__ == '__main__':
    app = HydraApp(title='My Portfolio')

    app.add_app("WORK EXPERIENCE", icon="🏢", app=WorkExperienceApp(), is_home=True)
    app.add_app("Project Details", icon="📝", app=ProjectDetailsApp())

    app.run()
