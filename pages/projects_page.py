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

        st.markdown("""
            <style>
            .card {
                margin-bottom: 20px;
                border-radius: 10px;
                border: none;
                box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
            }
            .card-body {
                padding: 15px;
            }
            .card-title {
                margin-bottom: 15px;
                font-weight: bold;
            }
            .card-text {
                font-size: 14px;
                margin-bottom: 15px;
            }
            .image {
                height: auto;
                max-height: 400px;
                width: 100%;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
                object-fit: contain;
                border: 0.5px solid #000000; /* Add a border to the image */
            }
            .streamlit-button {
                margin-top: 10px;
                border-radius: 5px;
            .streamlit-expander-header { /* Adjust the styling for the expander header */
                font-size: 16px;
                font-weight: bold;
            }
            .streamlit-expander { /* Adjust the styling for the expander */
                margin-top: 0px;
                border-top: none;
                position: absolute;
                bottom: 0;
                left: 0;
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

        # Assuming you have a PDF file named 'example.pdf' in the same directory as your Streamlit script
        pdf_file_path_smart_dustbin_project = 'assets/documents/Smart_Dustbin_manthan.pdf'
        pdf_file_path_isro_project = 'assets/documents/ISRO.pdf'
        # Sample project data
        projects = [
            {
                "title": "Go Mad Android App",
                "image": "https://github.com/nitzmali/portfolio/blob/main/assets/images_resized/gomad.png?raw=true",
                "description": "Harmonizing Innovation: The Dual-Melody Android App",
                "details": "In a blend of creativity and technology, we developed an Android application that introduces a new way of experiencing music—delivering distinct songs to each ear. This app redefines personal audio by allowing users to immerse themselves in two different audio streams simultaneously, one for each ear. It's a symphony of innovation designed to cater to the diverse auditory preferences of the user, perfect for those moments when one melody is simply not enough.",
                "insights": "Insights from Project 1",
                "visualizations": "URL_to_visualization_1", 
                "code": "https://www.facebook.com/GoMadApp",
                "conclusion": "Conclusion of Project 1",
                "pdf":False

            },
            {
                "title": "Smart Dustbin",
                "image": "https://github.com/nitzmali/portfolio/blob/main/assets/images/smart_dustbin.png?raw=true",
                "description": "Revolutionizing Waste Management with Smart Dustbin",
                "details":'',
                "insights": "Insights from Project 1",
                "visualizations": "URL_to_visualization_1",  # or path to local file
                "code": "https://youtu.be/09odCLopdrc?si=Vgr8L8ltDlQnXXjR",
                "conclusion": "Conclusion of Project 1",
                "pdf":True,
                "pdf_file_path":'assets/documents/Smart_Dustbin_manthan.pdf'
            },
            {
                "title": "Fault Tolerant Autonomoy Of A Spacecraft",
                "image": "https://media.giphy.com/media/viXmmzsetEf4mmFZsi/giphy.gif",
                "description": "Pioneering Spacecraft Autonomy: Final Year Project & ISRO Internship",
                "details":'',
                "insights": "Insights from Project 1",
                "visualizations": "URL_to_visualization_1",  # or path to local file
                "code": "https://youtu.be/09odCLopdrc?si=Vgr8L8ltDlQnXXjR",
                "conclusion": "Conclusion of Project 1",
                "pdf":True,
                "pdf_file_path":'assets/documents/ISRO.pdf'
            },
            {
                "title": "Blogging Website",
                "image": "https://github.com/nitzmali/portfolio/blob/main/assets/images/Rutgers_logo_2.jpg?raw=true",
                "description": "Digital Innovations: Django-Powered Blogging for Rutger's Students",
                "details":'I have successfully developed and launched two distinct web applications, showcasing versatility and technical prowess in modern web development. The first is a dynamic blogging website built using the Django framework, a testament to my skills in Python and full-stack development. This platform offers an intuitive user interface and robust features, catering to a wide range of blogging needs and published on Heroku for seamless accessibility.',
                "insights": "Insights from Project 1",
                "visualizations": "URL_to_visualization_1",  # or path to local file
                "code": "https://github.com/nitzmali/Artificial-Intelligence--Path-Planning-and-Search-Algorithms",
                "conclusion": "Conclusion of Project 1",
                "pdf":False,
                "pdf_file_path":''
            },
            {
                "title": "AI Algorithms",
                "image": "https://github.com/nitzmali/portfolio/blob/main/assets/images/DFS.PNG?raw=true",
                "description": "Navigating Complexity: AI Path Planning and Search Algorithms",
                "details":"I delved into the intricate world of Artificial Intelligence, focusing on path planning and search algorithms. This project was an extensive exploration of various search techniques, applied both in traditional path planning contexts and in the more abstract realm of constructing and designing complex structures. We began by generating and solving simple mazes using classical search algorithms like Breadth-First Search (BFS), Depth-First Search (DFS), and A*. Our journey didn't stop there; we pushed the boundaries further by employing advanced algorithms such as Local Beam Search to create mazes specifically designed to challenge our initial solutions. This project not only deepened my understanding of AI search algorithms but also honed my skills in creatively applying these techniques to solve increasingly complex problems.",
                "insights": "Insights from Project 1",
                "visualizations": "URL_to_visualization_1",  # or path to local file
                "code": "https://github.com/nitzmali/Artificial-Intelligence--Path-Planning-and-Search-Algorithms",
                "conclusion": "Conclusion of Project 1",
                "pdf":False,
                "pdf_file_path":''
            },
            {
                "title": "Machine Learning Image Colorization",
                "image": "https://github.com/nitzmali/portfolio/blob/main/assets/images_resized/color_to_gray.png?raw=true",
                "description": "Reviving Colors through AI: Machine Learning Image Colorization",
                "details":"I embarked on an innovative machine learning venture to transform grayscale images into vibrant color. Utilizing K-means clustering and linear regression, our team trained a model capable of accurately inferring and applying color to monochromatic images. The process involved meticulous division of data into training, test, and validation sets, coupled with extensive experimentation with various hyperparameters. These included the number of clusters, the format of input data (whether clustered, normalized, or one-hot encoded), and the type of output, along with adjustments in the learning rate. Our focus was on fine-tuning the parameters in the linear regression model to maximize accuracy, with validation data sets serving as our benchmark for success. This project not only demonstrated the practical applications of machine learning in image processing but also pushed the limits of how artificial intelligence can restore and enhance visual data.",
                "insights": "Insights from Project 1",
                "visualizations": "URL_to_visualization_1",  # or path to local file
                "code": "https://github.com/nitzmali/Convert-gray-color-image-to-Color",
                "conclusion": "Conclusion of Project 1",
                "pdf":False,
                "pdf_file_path":''
            },
                    {
                "title": "Airbnb Travel",
                "image": '<iframe src="https://slides.com/nitinmali/capstone/embed" width="830" height="391" title="Capstone Presentation" scrolling="no" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>',
                "description": "Innovating Travel (Airbnb) : From Predictive Analytics to Automated Airport Navigation",
                "details":"Embarking on a mission to redefine the travel experience, my projects intertwine the power of predictive analytics with smart automation. The first initiative leverages Random Forest algorithms to accurately predict a guest's next travel destination, enhancing the Airbnb booking experience. By analyzing patterns and preferences, this system intelligently forecasts where travelers are most likely to book their next journey, bringing a new level of personalization to the travel industry.</p><p>The second venture focuses on streamlining the airport experience. We've developed a web application tailored for airport lounges, designed to automate room bookings and guide passengers efficiently to their designated gates. This system not only simplifies the booking process but also employs advanced algorithms to find the shortest path to the assigned gate, ensuring a swift and stress-free transition for travelers. Our goal is to transform waiting times into moments of comfort, offering a seamless, user-friendly service that caters to the modern traveler's needs.",
                "insights": "Insights from Project 1",
                "visualizations": "URL_to_visualization_1",  # or path to local file
                "code": "https://slides.com/nitinmali/capstone/",
                "conclusion": "Conclusion of Project 1",
                "pdf":False,
                "pdf_file_path":''
            },
                        {
                "title": "Income and BMI Prediction",
                "image": "https://github.com/nitzmali/portfolio/blob/main/assets/images_resized/BMI_output_2png.png?raw=true",
                "description": "Advancements in Predictive Modeling: Income and BMI Analysis",
                "details":"In two significant projects, I demonstrated the power of predictive modeling, first by developing a model to predict household income and then by creating a model to estimate Body Mass Index (BMI). The household income project involved comprehensive steps such as data loading, feature engineering, model development and validation, and interpretation. Special attention was given to the unique challenge of predicting household income based on individual records, employing techniques like Neighbours Similarity Algorithm and Recursive Feature Elimination to ensure accuracy and quality.</p><p>The BMI prediction project was equally intricate, utilizing demographic data to predict BMI with a focus on both interpretability and performance. This project involved various statistical models and tests, such as OLS, Anova, and Tukey HSD, and employed different forms of linear regression, including Ridge, Lasso, and Elastic-Net, to provide a nuanced understanding of BMI factors. Both projects not only highlighted my skills in data science and statistical analysis but also underscored the importance of predictive modeling in extracting meaningful insights from complex datasets.",
                "insights": "Insights from Project 1",
                "visualizations": "URL_to_visualization_1",  # or path to local file
                "code": "https://github.com/nitzmali/BMI_PREDICTION",
                "conclusion": "Conclusion of Project 1",
                "pdf":False,
                "pdf_file_path":''
            },
            {
                "title": "AI Powered Job Transition Pathway using Generative LSTM Models",
                "image": "https://github.com/nitzmali/portfolio/blob/main/assets/images_resized/job_transition.png?raw=true",
                "description": "This comprehensive project in Data Science delves into the dynamic nature of the modern workforce.",
                "details":'''<div>
                            <h2>FutureScape Navigator: Transforming Career Journeys with Generative AI and LSTM Insights</h2>
                            <h3>Motivation</h3>
                            <p>
                                The modern workforce's dynamic nature calls for continuous adaptation in skills and knowledge. This project arose from a deep understanding of the challenges faced by professionals in plotting their career paths amidst rapidly changing job categories and skill requirements. By leveraging machine learning models, specifically seq2seq models with bidirectional LSTM and attention mechanisms, the project aims to offer tailored career guidance solutions, adapting to the fast-paced professional environment.
                            </p>
                            <h3>Background Information</h3>
                            <p>
                                The research underscores the trend of career switching, reflecting the changing dynamics of work, skill demands, and personal aspirations. It highlights the increasing trend of labor mobility across various age groups, emphasizing the need for tools that facilitate smooth career transitions and enable professionals to tailor their career paths.
                            </p>
                            <h3>Literature Review</h3>
                            <p>
                                The study juxtaposes its unique approach against existing literature, focusing on the enhancement of job-skill representation and the importance of understanding job transition patterns. It stands out for its emphasis on predicting educational courses and career progression using a novel AI approach.
                            </p>
                            <h3>Methodology</h3>
                            <p>
                                Comprehensive data collection from online job portals, skill repositories, and educational platforms form the foundation of this research. The methodology encompasses data cleaning, exploratory data analysis, and sophisticated data processing techniques, including the use of Phrase Matcher Models and fuzzy matching to refine and correlate data across different domains.
                            </p>
                            <h3>ML Modeling</h3>
                            <p>
                                The heart of the project lies in its advanced ML modeling, utilizing Seq2Seq architecture with LSTM layers. These models, coupled with BERT embeddings, are adept at capturing the nuances of language and context, crucial for accurately mapping career paths and skill development trajectories.
                            </p>
                            <h3>Experiments and Model Evaluation</h3>
                            <p>
                                The project delves into various experiments to fine-tune the model, exploring different embeddings and LSTM configurations. The evaluation metrics focus on the model's accuracy in forecasting job roles and the relevance of course recommendations, providing an objective assessment of its effectiveness.
                            </p>
                            <h3>Project Results</h3>
                            <p>
                                The project successfully demonstrates a model-generated output showcasing potential career pathways, requisite skills, and tailored course recommendations, thus offering a comprehensive tool for career planning and skill development.
                            </p>
                            <h3>Discussion and Future Improvement</h3>
                            <p>
                                The research concludes with a critical discussion on its holistic approach, potential improvements, and future directions. It emphasizes the need for continuous refinement of the model to keep pace with the evolving job market and skill landscape.
                            </p>
                        </div>''',
                "insights": "Insights from Project 1",
                "visualizations": "URL_to_visualization_1",  # or path to local file
                "code": "https://github.com/nitzmali/job_transition_pathway",
                "conclusion": "Conclusion of Project 1",
                "pdf":False,
                "pdf_file_path":''
            },
            {
                "title": "Machine Learning Image Colorization",
                "image": "https://github.com/nitzmali/portfolio/blob/main/assets/images_resized/color_to_gray.png?raw=true",
                "description": "Reviving Colors through AI: Machine Learning Image Colorization",
                "details":"I embarked on an innovative machine learning venture to transform grayscale images into vibrant color. Utilizing K-means clustering and linear regression, our team trained a model capable of accurately inferring and applying color to monochromatic images. The process involved meticulous division of data into training, test, and validation sets, coupled with extensive experimentation with various hyperparameters. These included the number of clusters, the format of input data (whether clustered, normalized, or one-hot encoded), and the type of output, along with adjustments in the learning rate. Our focus was on fine-tuning the parameters in the linear regression model to maximize accuracy, with validation data sets serving as our benchmark for success. This project not only demonstrated the practical applications of machine learning in image processing but also pushed the limits of how artificial intelligence can restore and enhance visual data.",
                "insights": "Insights from Project 1",
                "visualizations": "URL_to_visualization_1",  # or path to local file
                "code": "https://github.com/nitzmali/Convert-gray-color-image-to-Color",
                "conclusion": "Conclusion of Project 1",
                "pdf":False,
                "pdf_file_path":''
            },
            # Add more projects as needed...
        ]

        def create_tabs(project,pdf=True):
            with st.expander("View More",expanded=False):
                tab1, tab2, tab3 = st.tabs(["Details", "Code", "Conclusion"])

                with tab1:
                    if not pdf:
                        st.markdown(project["details"], unsafe_allow_html=True)
                    else:
                        st.markdown(return_pdf_embed(project["pdf_file_path"]), unsafe_allow_html=True)

                with tab2:
                    st.markdown(f"[Code Repository]({project['code']})")
                    # Create the nbviewer URL for your notebook
                    if project["title"]=="Income and BMI Prediction":
                        st.write("House Income Data Preparation")
                        github_url = 'https://github.com/nitzmali/BMI_PREDICTION/blob/main/1.1%20-%20Data_Preparation%20%5BHH%5D.ipynb?raw=true'
                        nbviewer_url = github_url.replace('github.com', 'nbviewer.jupyter.org/github')
                        st.markdown(f'<iframe src="{nbviewer_url}" width="100%" height="800" frameborder="0"></iframe>', unsafe_allow_html=True)
                        st.write("House Income Data Exploration")
                        github_url = 'https://github.com/nitzmali/BMI_PREDICTION/blob/main/1.2%20-%20Data%20Exploration%20%5BHH%5D.ipynb?raw=true'
                        nbviewer_url = github_url.replace('github.com', 'nbviewer.jupyter.org/github')
                        st.markdown(f'<iframe src="{nbviewer_url}" width="100%" height="800" frameborder="0"></iframe>', unsafe_allow_html=True)
                        st.write("House Income Modelling")
                        github_url = 'https://github.com/nitzmali/BMI_PREDICTION/blob/main/1.3%20-%20Encoding%20and%20%20Modelling%20%5BHH%5D.ipynb?raw=true'
                        nbviewer_url = github_url.replace('github.com', 'nbviewer.jupyter.org/github')
                        st.markdown(f'<iframe src="{nbviewer_url}" width="100%" height="800" frameborder="0"></iframe>', unsafe_allow_html=True)
                        st.write("BMI Data Preparation")
                        github_url = 'https://github.com/nitzmali/BMI_PREDICTION/blob/main/1.2%20-%20Data%20Exploration%20%5BHH%5D.ipynb?raw=true'
                        nbviewer_url = github_url.replace('github.com', 'nbviewer.jupyter.org/github')
                        st.markdown(f'<iframe src="{nbviewer_url}" width="100%" height="800" frameborder="0"></iframe>', unsafe_allow_html=True)
                        st.write("BMI Data Exploration")
                        github_url = 'https://github.com/nitzmali/BMI_PREDICTION/blob/main/2.2%20-%20Data%20Exploration%20%5BBMI%5D.ipynb?raw=true'
                        nbviewer_url = github_url.replace('github.com', 'nbviewer.jupyter.org/github')
                        st.markdown(f'<iframe src="{nbviewer_url}" width="100%" height="800" frameborder="0"></iframe>', unsafe_allow_html=True)
                        st.write("BMI -- Regression Machine Learning Model")
                        github_url = 'https://github.com/nitzmali/BMI_PREDICTION/blob/main/2.3%20-%20Encoding%20and%20Modelling%20%5BBMI%5D.ipynb?raw=true'
                        nbviewer_url = github_url.replace('github.com', 'nbviewer.jupyter.org/github')
                        st.markdown(f'<iframe src="{nbviewer_url}" width="100%" height="800" frameborder="0"></iframe>', unsafe_allow_html=True)

                    if project["title"]=="AI Powered Job Transition Pathway using Generative LSTM Models":
                        st.write("## Data Loading and Processing")
                        github_url = 'https://github.com/nitzmali/job_transition_pathway/blob/main/notebooks/data_process.ipynb?raw=true'
                        nbviewer_url = github_url.replace('github.com', 'nbviewer.jupyter.org/github')
                        st.markdown(f'<iframe src="{nbviewer_url}" width="100%" height="800" frameborder="0"></iframe>', unsafe_allow_html=True)
                        st.write("## Clustering Job Ttiles using Spacy")
                        github_url = 'https://github.com/nitzmali/job_transition_pathway/blob/main/notebooks/build_clustering_titles_skills_iden_models.ipynb?raw=true'
                        nbviewer_url = github_url.replace('github.com', 'nbviewer.jupyter.org/github')
                        st.markdown(f'<iframe src="{nbviewer_url}" width="100%" height="800" frameborder="0"></iframe>', unsafe_allow_html=True)
                        st.write("## Generate Synthetic data to map job transitions")
                        github_url = 'https://github.com/nitzmali/job_transition_pathway/blob/main/notebooks/jobs_data_generation.ipynb?raw=true'
                        nbviewer_url = github_url.replace('github.com', 'nbviewer.jupyter.org/github')
                        st.markdown(f'<iframe src="{nbviewer_url}" width="100%" height="800" frameborder="0"></iframe>', unsafe_allow_html=True)
                        st.write("## Job Prediction")
                        github_url = 'https://github.com/nitzmali/job_transition_pathway/blob/main/notebooks/final_models/job_prediction.ipynb?raw=true'
                        nbviewer_url = github_url.replace('github.com', 'nbviewer.jupyter.org/github')
                        st.markdown(f'<iframe src="{nbviewer_url}" width="100%" height="800" frameborder="0"></iframe>', unsafe_allow_html=True)
                        st.write("## Skills Prediction")
                        github_url = 'https://github.com/nitzmali/job_transition_pathway/blob/main/notebooks/final_models/skills_prediction.ipynb?raw=true'
                        nbviewer_url = github_url.replace('github.com', 'nbviewer.jupyter.org/github')
                        st.markdown(f'<iframe src="{nbviewer_url}" width="100%" height="800" frameborder="0"></iframe>', unsafe_allow_html=True)
                        st.write("## Course Prediction")
                        github_url = 'https://github.com/nitzmali/job_transition_pathway/blob/main/notebooks/final_models/course_prediction.ipynb?raw=true'
                        nbviewer_url = github_url.replace('github.com', 'nbviewer.jupyter.org/github')
                        st.markdown(f'<iframe src="{nbviewer_url}" width="100%" height="800" frameborder="0"></iframe>', unsafe_allow_html=True)    

                with tab3:
                    st.write(project["conclusion"])


        # Number of columns for the grid
        cols_per_row = 2
        def is_iframe(image_string):
            return "<iframe" in image_string

        # Create the card layout
        for i in range(0, len(projects), cols_per_row):
            cols = st.columns(cols_per_row)
            for j in range(cols_per_row):
                if i + j < len(projects):
                    project = projects[i + j]
                    if is_iframe(project["image"]):
                        # If it's an iframe, render it directly
                        media_html = project["image"]
                    else:
                        # If it's an image URL, use the img tag
                        media_html = f'<img class="image" src="{project["image"]}" alt="{project["title"]}">'

                    with cols[j]:
                        st.markdown(f"""
                            <div class="card">
                                {media_html}
                                <div class="card-body">
                                    <h5 class="card-title">{project['title']}</h5>
                                    <p class="card-text">{project['description']}</p>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
                        create_tabs(project,project["pdf"])

                st.markdown("""
                    <hr style="
                        border: none; 
                        height: 1px; 
                        background: linear-gradient(to right, #B2DFDB 0%, #B2DFDB 100%); 
                        margin-top: 0px; 
                        margin-bottom: 0px;">
                """, unsafe_allow_html=True)

                #st.markdown('<hr style="border:2px solid #008080; width:50%; margin:auto;"/>', unsafe_allow_html=True)

   







            




