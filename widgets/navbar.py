import streamlit as st
from streamlit.components.v1 import html
from PIL import Image
import streamlit.components.v1 as components
def render_navbarr():


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
#<header tabindex="-1" data-testid="stHeader" class="css-uc1cuc e8zbici2"><div data-testid="stDecoration" class="css-1dp5vir e8zbici1"></div><div data-testid="stToolbar" class="css-14xtw13 e8zbici0"><span id="MainMenu" aria-haspopup="true" aria-expanded="false"><button kind="header" class="css-4l4x4v edgvbvh3"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="currentColor" xmlns="http://www.w3.org/2000/svg" color="inherit" class="e1fb0mya1 css-fblp2m ex0cdmw0"><path fill="none" d="M0 0h24v24H0V0z"></path><path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"></path></svg></button></span></div></header>
     # css
    with open("assets/styles/style.css") as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    #markdowns
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

def render_navbar():
    with open("assets/styles/style.css") as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    st.markdown("""
    <nav class="navbar fixed-top navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">Nitin Mali</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item active">
                    <a class="nav-link" href="#">Home<span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">About</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Work Experience</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Projects</a>
                </li>
            </ul>
        </div>
    </nav>
    """, unsafe_allow_html=True)

def render_footer():
    st.markdown("""

    <!-- Font Awesome -->
    <link
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
    rel="stylesheet"
    />
    <!-- Google Fonts -->
    <link
    href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
    rel="stylesheet"
    />
    <!-- MDB -->
    <link
    href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/7.1.0/mdb.min.css"
    rel="stylesheet"
    />

    <!-- MDB -->
    <script
    type="text/javascript"
    src="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/7.1.0/mdb.umd.min.js"
    ></script>

    <footer class="text-center text-white " style="background-color: rgba(0, 0, 0, 0.2);">
    <!-- Grid container -->
    <div class="container p-4 pb-0">
        <!-- Section: Social media -->
        <section class="mb-4">
        <!-- Facebook -->
        <a
            class="btn text-white btn-floating m-1"
            style="background-color: #3b5998;"
            href="https://www.facebook.com/nitsmali/"
            role="button"
            ><i class="fab fa-facebook-f"></i
        ></a>
        <a
            class="btn text-white btn-floating m-1"
            style="background-color: #55acee;"
            href="https://twitter.com/nyzygyan"
            role="button"
            ><i class="fab fa-twitter"></i
        ></a>
        <!-- Google -->
        <a
            class="btn text-white btn-floating m-1"
            style="background-color: #dd4b39;"
            href="#!"
            role="button"
            ><i class="fab fa-google"></i
        ></a>
        <!-- Instagram -->
        <a
            class="btn text-white btn-floating m-1"
            style="background-color: #ac2bac;"
            href="https://instagram.com/nyzygyan"
            role="button"
            ><i class="fab fa-instagram"></i
        ></a>
        <!-- Linkedin -->
        <a
            class="btn text-white btn-floating m-1"
            style="background-color: #0082ca;"
            href="https://www.linkedin.com/in/nitsmali/"
            role="button"
            ><i class="fab fa-linkedin-in"></i
        ></a>
        <!-- Github -->
        <a
            class="btn text-white btn-floating m-1"
            style="background-color: #333333;"
            href="https://github.com/nitzmali"
            role="button"
            ><i class="fab fa-github"></i
        ></a>
        </section>
        <!-- Section: Social media -->


    </div>
    <!-- Grid container -->

    <!-- Copyright -->
    <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2);">
        © 2023 Nitin Mali | All Rights Reserved
    </div>
    <!-- Copyright -->
    </footer>""", unsafe_allow_html=True)