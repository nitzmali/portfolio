import streamlit as st

def render_navbar():


    st.markdown("""
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
    <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Nitin Mali</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
        <li class="nav-item active">
            <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="#about">About</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="#work-experience">Work_Experience</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="#projects">Projects</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="#social-media">Social Media</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="#contact">Contact</a>
        </li>
        </ul>
    </div>
    </nav>
    """, unsafe_allow_html=True)