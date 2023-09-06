import yfinance as yf 
import streamlit as st 
import pandas as pd 
import streamlit as st
import numpy as np
import pandas as pd
import time
from streamlit.components.v1 import html
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Chanin Nantasenamat</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#bioinformatics-tools">Bioinformatics Tools</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)



#pages 



#caching 

@st.cache_data
def long_running_function(param1, param2):
    time.sleep(5)
    st.write("wait")
    return "nitin"

long_running_function("x1","x2")





#themes

st.write("https://docs.streamlit.io/library/advanced-features/theming")


#show progress 
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(1):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

with st.echo():
    st.write("The chart above shows some numbers I picked for you.I rolled actual dice for these, so they're *guaranteed* to be random.")
    st.image("https://static.streamlit.io/examples/dice.jpg") 

with st.spinner():
    with st.spinner('Wait for it...'):
        time.sleep(5)
st.write("The chart above shows some numbers I picked for you.I rolled actual dice for these, so they're *guaranteed* to be random.")
st.image("https://static.streamlit.io/examples/dice.jpg") 


#layout
# 
# #st.expander 
# 
st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write("The chart above shows some numbers I picked for you.I rolled actual dice for these, so they're *guaranteed* to be random.")
    st.image("https://static.streamlit.io/examples/dice.jpg") 

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)



#use select box to choose from a series
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })
'''
option1 = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option1
'''
'''
#use checkboxes to show/hide data 

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

# unique key for widget
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name



# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable selectbox widget", key="disabled")
    st.radio(
        "Set selectbox label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )






#button and checkbox 

st.title("Radio Buttons, checkboxes and buttons")
page_names =['Checkbox','Button']
page = st.radio('Navigation', page_names)

st.write("** The variable 'page' returns:** ", page)

check=None
result=None
if page=='Checkbox':
    st.subheader("Welcome to the checkbox page")
    st.write("Nice to see you! :wave")
    check = st.checkbox("Click here")
    st.write('state of the checkbox', check)

if check:
    nested_btn = st.button("Button nested in checkbox")

    if nested_btn:
        st.write(":cake:"*20)
else:
    st.subheader("Welcome to the button page")
    st.write("thumbs up")
    result=st.button("Click Here")
    st.write("state of button", result)

if result:
    nested_check = st.checkbox("Checkbox nested in Button ")

    if nested_check:
        st.write("nested cehck heart")







st.write("""
"Simple Stock Proce APP 

Shown are the stock closing price abd volume of google 


""")
'''
tickerSymbol = 'GOOGL'

tickerData =  yf.Ticker(tickerSymbol)

tickerDF= tickerData.history(period='id', start='2010-5-31', end='2020-5-31')

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)



'''

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))



chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)


#widgets 
#slider
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

#button
st.button("Reset", type="primary")
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')


st.title("Making a button")

result = st.button("click here")
st.write(result)
st.write(result)
if result:
    st.write(":smile")

'''