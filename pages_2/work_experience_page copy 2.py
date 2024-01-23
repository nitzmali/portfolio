# Your existing imports
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
from streamlit_timeline import timeline
import matplotlib.pyplot as plt
import json
# ... rest of your imports

# Assuming you have defined your 'projects' and 'work_experience' lists as shown earlier

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
                "image": '<iframe src="https://slides.com/nitinmali/capstone/embed" width="880" height="400" title="Capstone Presentation" scrolling="no" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>',
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
                "image": "https://github.com/nitzmali/portfolio/blob/main/assets/images/job_transition.png?raw=true",
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


work_experience = [
        {
            "role": "Data Scientist",
            "company": "ZS Associates",
            "period": "January 2023 - Present",
            "location": "New York, USA",
            "details": """
                <ul>
                    <li>Led the development of utilizing Convolutional Neural Networks (CNNs), to analyze and interpret complex user interaction data, effectively enhancing engagement with our digital tools by 25%.</li>
                    <li>Employed Generative AI, specifically Transformer-based Large Language Models (LLMs), for in-depth textual analysis and content generation, enabling more personalized and relevant HCP-user interactions.</li>
                    <li>Engineered sophisticated multi-channel optimization and business experimentation strategies by integrating Bayesian Methods for probabilistic inference, Logistic Regression for predictive analysis, and Ensemble Methods to aggregate insights from multiple models, yielding a tangible 10% improvement in digital engagement efficiency.</li>
                    <li>Translated machine learning insights into actionable strategies, akin to the impact of using Scikit-learn in time series models, reducing forecasting errors by 18%.</li>
                    <li>Applied analytical and statistical programming skills using Python, TensorFlow, and Pandas to collect, analyze, and interpret large data sets, driving significant insights and outcomes.</li>
                    <li>Collaborated with various stakeholders across multiple departments to leverage data for organizational growth, while also streamlining data science projects by identifying and eliminating duplicative efforts, thereby enhancing team coordination and improving project efficiency by 50%.</li>
                    <li>Pioneered the creation of advanced credit risk models utilizing CNNs, Generative AI, and LLMs to analyze customer credit data, enhancing loan evaluation accuracy and integrating these models into Vanguard’s system, thereby boosting credit risk process efficiency by 30% and facilitating more nuanced lending decisions.</li>
                    <li>Employed Bayesian Methods, Logistic Regression, and Ensemble Methods in developing financial forecasting models, significantly improving the accuracy of predictions for asset values and market trends.</li>
                    <li>Designed and implemented sophisticated fraud detection algorithms using Generative AI and CNNs, achieving a notable reduction in online transaction fraud at Vanguard Group. Concurrently led a team to bolster investment risk management, culminating in the development of a real-time risk monitoring dashboard, which substantially enhanced risk mitigation strategies.</li>
                    <li>Transformed financial modeling techniques at Vanguard by adapting CNNs and LLMs for analyzing market trends and asset performance, markedly increasing asset valuation accuracy. This transformation included the integration of Bayesian Methods, Logistic Regression, and Ensemble Methods to refine financial forecasts and inform strategic investment decisions.</li>
                </ul>
            """,
            "icon": "https://github.com/nitzmali/portfolio/blob/main/assets/images/zs_associates_logo.jpeg?raw=true",
            "url":"https://zs.com",
        },
        {
            "role": "Data Engineer Manager",
            "company": "Webmd",
            "period": "November 2022 - January 2023",
            "location": "NewYork, USA",
            "details": """
                <ul>
                    <li>Streamlining data processes and enhancing pipeline efficiency. Championed the integration of big data technologies, including AWS andSpark, into the company's data architecture.</li>
                    <li>Initiated collaborations with product and customer analytics teams to derive actionable insights from tools such as Google Analytics and Adobe Analytics.</li>
                </ul>
            """,
            "icon": "https://github.com/nitzmali/portfolio/blob/main/assets/images/WebMD_logo.png?raw=true",  # Replace with the actual URL or path to your icon
            "url":"https://webmd.com",
        },
        {
            "role": "Data Scientist - Machine Learning Engineer",
            "company": "Aktana",
            "period": "November 2019 - December 2022",
            "location": "San Francisco, USA",
            "details": """
                <ul>
                    <li>Orchestrated the development of a Contextual Intelligence Engine (CIE) leveraging various machine learning models with Python and Spark on AWS EMR, resulting in a 40% uplift in targeted engagement and a streamlined data workflow automation.</li>
                    <li>Spearheaded the integration of a robust machine learning and analytics data platform utilizing Delta Lake on AWS, significantly enhancing algorithmic workflows and analytics.</li>
                    <li>Collaborated with product managers to develop neural network-based channel propensity models, enhancing healthcare professional engagement by 25%.</li>
                    <li>Utilized predictive analytics and behavioral modeling in AI for digital content personalization, achieving a 32% increase in conversion rates.</li>
                    <li>Advanced Gradient Boosting Machines were used to optimize marketing mix models, leading to a 21% improvement in digital marketing ROI.</li>
                    <li>Collaborated with Machine Learning Engineers and Product Managers to develop a user-centric, no-code automated machine learning platform using Knime and Databricks MLflow.</li>
                    <li>Implemented and maintained over 15 statistical and machine learning solutions, covering the entire life cycle from development to deployment including metadata management, optimizing model performance at scale.</li>
                    <li>Influenced the technical vision and strategies of engineering teams by translating machine learning insights into actionable, data-driven recommendations.</li>
                </ul>
            """,
            "icon": "https://github.com/nitzmali/portfolio/blob/main/assets/images/Aktana_logo_full_blue.jpg?raw=true",
            "url":"https://aktana.com",
        },
        {
            "role": "Data Analyst",
            "company": "Bristol Myers Squibb (BMS)",
            "period": "June 2018 - October 2019",
            "location": "Princeton, USA",
            "details": """
                <ul>
                    <li>Built and refined 36+ logical models, collaborating with database administrators to develop physical models and overall data architecture, enhancing the understanding of large datasets.</li>
                    <li>Developed comprehensive analytics reports for Sales, Patient, Claims data for reps to look at using Python and SQL within the XPERT platform, streamlining processes and saving over 60 hours monthly.</li>
                    <li>Automated BMS Sales Data Processing for US, using a Python-triggered email automation script to refresh data daily and publish on Dashboard.</li>
                    <li>Led the development of automated reporting systems for key performance metrics using Python and SQL, saving more than 30 hours each week.</li>
                    <li>Created dynamic operational reports in Tableau integrated with XPERT, enhancing team coordination and operational efficiency, resulting in significant cost savings.</li>
                    <li>Managed and analyzed client engagement metrics within the XPERT platform, optimizing client services and improving workforce allocation.</li>
                    <li>Enhanced dashboard performance in collaboration with Bristol Myers Squibb using XPERT, resulting in a 40% increase in user engagement.</li>
                    <li>Engineered and implemented ETL infrastructures at XSUNT, integrating SQL databases with Python to boost decision-making efficiency by 42% through enhanced data processing.</li>
                    <li>Utilized Python clustering methods to analyze geographic sales data, identifying and strategically improving underperforming markets, contributing to a 4% increase in profits.</li>
                    <li>Collaborated with product and sales teams to apply advanced customer segmentation and cohort analysis, leading to a strategic 21% pricing reduction for key segments, increasing annual revenue by over $100,000.</li>
                </ul>
            """,
            "icon": "https://github.com/nitzmali/portfolio/blob/main/assets/images/Bristol-Myers_Squibb_Logo.svg.png?raw=true",
            "url":"https://bms.com",
        },
        {
        "role": "Financial Analyst",
        "company": "Temenos",
        "period": "January 2015 - October 2016",
        "location": "Bengaluru, India",
        "details": """
            <ul>
                <li>Collaborated with 23 stakeholders to leverage advanced analytics in identifying investment opportunities and risks, guiding strategic decision-making in asset management.</li>
                <li>Conducted extensive data mining and analysis across multiple databases to optimize investment strategies and product offerings in wealth management.</li>
                <li>Orchestrated comprehensive A/B testing for client interfaces, achieving a 23% increase in client engagement and satisfaction through tailored wealth management solutions.</li>
                <li>Implemented advanced customer segmentation and cohort analysis, leading to a 21% optimized pricing strategy for high-value investment portfolios, boosting revenue by $500,000.</li>
                <li>Employed innovative statistical methods to develop and analyze financial products, enhancing portfolio diversification and risk management in asset management.</li>
                <li>Tailored analytics solutions to meet specific needs in wealth management, enhancing product development and investment performance.</li>
                <li>Led the creation of advanced testing strategies for financial systems, focusing on performance tuning and monitoring to maintain 99.9% system uptime, ensuring consistent reliability in financial transactions and reporting.</li>
            </ul>
        """,
        "icon": "https://github.com/nitzmali/portfolio/blob/main/assets/images/temenos_logo.jpg?raw=true",  # Replace with the actual URL or path to your icon,
        "url":"https://temenos.com",
    }
    ]

# Initialize session state for selected project and page view
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'
if 'selected_project' not in st.session_state:
    st.session_state.selected_project = None

# Custom CSS to adjust the layout and center the job container
st.markdown("""
    <style>
    .card-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        align-items: stretch;
    }
    .card {
        margin: 10px;
        flex-basis: 21%;  /* Adjust the card width here */
        border-radius: 10px;
        box-shadow: 0 2px 4px 0 rgba(0,0,0,0.2);
    }
    .card:hover {
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    }
    .card img {
        width: 100%;
        height: auto;
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
    }
    .card h5 {
        margin: 16px;
    }
    .card p {
        margin: 16px;
    }
    .job-container {
        text-align: center;
        margin-bottom: 40px;
    }
    .streamlit-button {
        display: block;
        width: 80%;
        margin: 10px auto;
        padding: 10px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Function to show project details (as a separate page)
def show_project_details(project):
    st.session_state['selected_project'] = project

# Main app logic
def main():
    if st.session_state.current_page == 'home':
        st.title('My Work Experience')

        # Display each job entry
        for job in work_experience:
            st.markdown(f"""
                <div class="job-container">
                    <h2 class="job-title">{job['role']}</h2>
                    <div class="job-company">
                        <img class="job-icon" src="{job['icon']}" alt="{job['company']} Icon">
                        <h3>{job['company']}</h3>
                    </div>
                    <p class="job-period-location">{job['period']} - {job['location']}</p>
                </div>
            """, unsafe_allow_html=True)
        
        # Display the project cards in a grid
        st.markdown("<div class='card-container'>", unsafe_allow_html=True)
        for project in projects:
            st.markdown(f"""
                <div class="card">
                    <img src="{project['image']}" alt="{project['title']}">
                    <h5>{project['title']}</h5>
                    <p>{project['description']}</p>
                    <button class="streamlit-button" onclick="window.location.href='#project-details';">View Details</button>
                </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    elif st.session_state.current_page == 'project_details':
        # Display the project details for the selected project
        selected_project = st.session_state.selected_project
        st.markdown(f"<h2>{selected_project['title']}</h2>", unsafe_allow_html=True)
        st.markdown(selected_project['details'], unsafe_allow_html=True)
        # Add a back button to go to the home page
        if st.button('Back to all projects'):
            st.session_state.current_page = 'home'
            st.session_state.selected_project = None

if __name__ == '__main__':
    main()
