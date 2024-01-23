#-----------dwell child app----------------------------------------------------------
from hydralit import HydraHeadApp
import streamlit as st

class DwellTimeApp(HydraHeadApp):

    def __init__(self, title = '', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        
    def run(self):
        st.info('running dwell')
        print('running dwell')
        #run_dwell()
        return None

#-------------------------------------------------------------------------------------

#-----------dwell 2 child app----------------------------------------------------------
from hydralit import HydraHeadApp
import streamlit as st

class DwellTimeApp2(HydraHeadApp):

    def __init__(self, title = '', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        
    def run(self):
        st.info('running dwell 2')
        print('running dwell 2')
        #run_dwell()
        return None

#-------------------------------------------------------------------------------------


#-----------home child app------------------------------------------------------------
import streamlit as st
from hydralit import HydraHeadApp

class HomeApp(HydraHeadApp):


    def __init__(self, title = 'Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

    def run(self):

        try:
            st.info('Home app')

            _,_,_, col_text,_ = st.columns([1,1,1,7,2])

            if col_text.button('Dwell➡️'):
                self.do_redirect('Dwell')

            if col_text.button('Dwell 2 ➡️'):
                self.do_redirect('Dwell 2')

        except Exception as e:
            st.error('Error details: {}'.format(e))

#--------------------------------------------------------------------------------------


#-----------parent app to run children-------------------------------------------------
from hydralit import HydraApp

if __name__ == '__main__':
    app = HydraApp(title='Hydralit Tester')

    app.add_app("Home", icon="🏠", app=HomeApp(title='Home'),is_home=True)
    app.add_app("Dwell", icon="📚", app=DwellTimeApp(title="Dwell App"))
    app.add_app("Dwell 2", icon="📚", app=DwellTimeApp2(title="Dwell App 2"))

    app.run()

#--------------------------------------------------------------------------------------