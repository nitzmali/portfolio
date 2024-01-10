import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
from streamlit_timeline import timeline
import matplotlib.pyplot as plt
import json
from widgets import sankey_work_experience


class WorkExperiencePage:
  def run(self):
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



    import streamlit as st

    st.title('My Work Experience')

    # Custom CSS to adjust the layout
    st.markdown("""
        <style>
        .job-container {
            display: flex;
            flex-direction: column;
        }
        .job-title {
            font-size: 30px;
            font-weight: bold;
        }
        .job-company {
            font-size: 18px;
            display: flex;
            align-items: center;
        }
        .job-icon {
            width: 100px;  /* Adjust the size of the icon */
            margin-left: 10px; /* Space between the company name and the icon */
        }
        .job-period-location {
            font-size: 16px;
            margin-top: 4px;
            margin-bottom: 10px;
        }
        </style>
    """, unsafe_allow_html=True)


    # Display each job entry
    for job in work_experience:
        # Use the image as a clickable link in the HTML string
        st.markdown(f"""
            <div class="job-container">
                <div class="job-title">{job['role']}</div>
                <div class="job-company">
                    <a href="{job['url']}" target="_blank">{job['company']}</a> 
                    <a href="{job['url']}" target="_blank">
                        <img class="job-icon" src="{job['icon']}" alt="{job['company']} Icon">
                    </a>
                </div>
                <div class="job-period-location">{job['period']} - {job['location']}</div>
            </div>
        """, unsafe_allow_html=True)

        with st.expander("See details"):
            st.markdown(f"<div>{job['details']}</div>", unsafe_allow_html=True)
             # Create columns where the first one is empty and acts like a left margin
    left_margin, chart_column = st.columns([1, 20])  # Adjust the ratio to control the offset

     # Render the chart in the right column
    with chart_column:
        st.plotly_chart(sankey_work_experience.render_image())  


    # Brief Introduction
    st.markdown("""
        <style>
            .about-container {
                color: #4f4f4f; /* Adjust the color as needed */
                text-align:left;
            }
            .about-header {
                color: #2874A6; /* Header color */
            }
            .highlight {
                color: #2E86C1; /* Highlights or key points */
            }
            .career-highlight {
                color: #21618C; /* Career highlights color */
                font-weight: bold;
            }
            .about-container h2, .about-container h3 {
            margin-top: 0;
            margin-bottom: 0;
            text-align: left;
            }
            /* Ensure that there is no extra space inherited from global styles */
            .about-container * {
            margin-top: 0;
            margin-bottom: 0;
            padding-top: 0;
            padding-bottom: 0;
            }
        </style>
        <div class="about-container">
        <hr>
        <h3 class="highlight"> Skills Overview Definition</h3>
        <h4>Programming/Tools:</h4>
        <ul>
                <li><strong>Languages & Frameworks:</strong> Proficient in Python, Spark, PyTorch, C, C++, R, TensorFlow, JavaScript, along with extensive use of Hadoop for big data processing.</li>
                <li><strong>Web Technologies & Systems:</strong> Experienced in Streamlit, HTML, CSS, JSON, and Linux system management.</li>
                <li><strong>Advanced Data Handling:</strong> Skilled in Advanced Excel for complex data analysis and manipulation.</li>
        </ul>

        <h4>Data Acquisition, Mining & Transformation:</h4>
        <ul>
                <li><strong>Data Acquisition:</strong> Expertise in acquiring data from diverse sources using APIs and AWS S3.</li>
                <li><strong>Mining with NLP:</strong> Utilizing NLP for extracting valuable insights from textual data.</li>
                <li><strong>Data Infrastructure & Management:</strong> Building Data Lake infrastructure, creating ETL/ELT pipelines, data modeling, and managing data architecture.</li>
                <li><strong>SQL Expertise:</strong> Proficient in SQL optimization and performance tuning.</li>
                <li><strong>Data Warehousing & Reporting:</strong> Experienced in Snowflake, AWS RDS, Postgres, Neo4j, Oracle SQL, MySQL, MongoDB for comprehensive data warehousing and reporting.</li>
        </ul>

        <h4>Visualization:</h4>
        <ul>
            <li>Proficient in Tableau, Qlik Sense, SSRS, Matplotlib, Seaborn for crafting compelling data stories.</li>
        </ul>

        <h4>Cloud, Containerization, ML Ops:</h4>
        <ul>
                <li><strong>Cloud Platforms & ML Ops:</strong> Skilled in AWS (including SageMaker, RDS, EC2, Glue, EMR, S3), Data Bricks (MLFlow, Auto ML), Dataiku, Knime, and Docker.</li>
                <li><strong>ML Model Deployment:</strong> Collaborating with MLOps teams for deploying machine learning models, ensuring scalability and reliability.</li>
        </ul>

        <h4>Machine Learning:</h4>
        <ul>
                <li><strong>ML Theory & Application:</strong> Deep understanding of machine learning theory and its practical application.</li>
                <li><strong>Model Evaluation & Optimization:</strong> Evaluating and optimizing machine learning models for performance, accuracy, and consistency.</li>
                <li><strong>Techniques & Algorithms:</strong> Proficient in regression, time series analysis (ARIMA), clustering, decision trees, random forest, XGBoost, PCA, and using SKLearn.</li>
        </ul>

        <h4>Deep Learning:</h4>
                <li><strong>Frameworks & Techniques:</strong> Expertise in TensorFlow, PyTorch, Hugging Face, Spacy, langchain, Keras, and GPU-based training.</li>
                <li><strong>Model Types:</strong> Experienced in convolutional and recurrent models.</li>

        <h4>GenAI and NLP:</h4>
                <li><strong>Advanced NLP:</strong> LLM, transformers, embeddings, topic models, NER, Q&A, document summarization/classification, text generation, sentiment analysis, finetune LLMs.</li>
                <li><strong>Search & Retrieval:</strong> Retrieval Augmented Generation (RAG),semantic search, VectorDBs, prompt engineering, implementing information search and retrieval at scale, using a range of solutions ranging from keyword search to semantic search using embeddings.</li>

        <h4>Analytics:</h4>
                <li><strong>Product Analytics:</strong> Skilled in analyzing both structured and unstructured data for product analytics.</li>
                <li><strong>Statistical Analysis:</strong> statistical methods to identify patterns, anomalies, relationships, and trends.</li>
                <li><strong>Product Analytics Strategy:</strong> Leading analysis projects to deepen understanding of customers, uncover product improvement opportunities, provide actionable recommendations, and drive impact for our business.</li>

        <h4>Statistics:</h4>
                <li><strong>Statistical Knowledge:</strong> Strong foundation in various statistical methods and mathematical disciplines.</li>
                <li><strong>Specialized Techniques:</strong> Proficient in Bayesian Analysis, Linear Programming, and conducting A/B testing.</li>

        <h4>Communication:</h4>
                <li><strong>Effective Articulation:</strong> Excel at conveying complex technical concepts and aligning them with business objectives to ensure comprehensive understanding across all organizational levels.</li>
                <li><strong>Senior Management Interaction:</strong> Proven ability to confidently influence and communicate with senior management, adept at presenting data-driven insights and findings succinctly.</li>
                <li><strong>Clear and Concise Reporting:</strong> Skilled in leading interactions with both business and technical stakeholders, presenting findings and recommendations through well-crafted reports and presentations.</li>
                <li><strong>Authentic Engagement:</strong> Committed to direct communication, offering candid feedback, and promoting authenticity, thereby fostering a transparent and efficient work environment.</li>
                <li><strong>Data Storytelling:</strong> Expert in navigating through complex data sets to extract meaningful stories, translating analytics into relevant business insights.</li>


        <h4>Lead:</h4>
                <li><strong>Team Leadership:</strong> Demonstrated track record in leading and mentoring data science teams, underpinned by strong organizational and interpersonal skills.</li>
                <li><strong>Strategic Management:</strong> Proficient in managing trade-offs and exercising leadership in a matrixed environment without direct authority.</li>
                <li><strong>Stakeholder Influence:</strong> Highly influential in educating challenging stakeholders about the critical role of data in business contexts.</li>
                <li><strong>Mentorship and Guidance:</strong> Committed to mentoring junior data scientists, fostering a culture of innovation, technical excellence, and continuous learning.</li>
                <li><strong>Decision-Making and Negotiation:</strong> Robust negotiation and decision-making skills, adept at aligning business and customer needs with strategic updates, vision, and KPIs.</li>


        <h4>Team Management:</h4>
                <li><strong>Efficient Project Handling:</strong> Proficient in managing multiple projects with competing priorities, ensuring high organizational efficiency.</li>
                <li><strong>Culture of Accountability:</strong> Foster a team environment focused on accountability, open communication, and self-management.</li>
                <li><strong>Impactful Leadership:</strong> Proactively drive impactful initiatives, ensuring team engagement and leading by example to achieve collective goals.</li>
                <li><strong>Goal Achievement:</strong> Consistently surpass individual and team objectives through effective leadership and strategic planning.</li>
                <li><strong>Global Team Management:</strong> Experienced in coordinating and working with globally distributed teams, nurturing a diverse and inclusive work culture.</li>
                <li><strong>Talent Development:</strong> Passionate about developing talent within my team and beyond, focusing on continuous learning and career growth.</li>
                <li><strong>Adaptive Time Management:</strong> Demonstrated ability to prioritize tasks, manage time effectively, and adapt to shifting priorities in dynamic environments.</li>

        <h4>Collaboration and Cross Functional:</h4>
                <li><strong>Cross-Functional Collaboration:</strong> Expertise in working with cross-functional teams, including product managers, engineers, and operations, to integrate solutions into products.</li>
                <li><strong>Teamwork for Innovation:</strong> Collaborate effectively to promote speed, agility, and innovation in team endeavors.</li>
                <li><strong>AI-Driven Product Development:</strong> Partner with data scientists, software engineers, and product managers to deliver AI-powered products, integrating technical expertise with business goals.</li>

        <h4>Business Strategy:</h4>
                <li><strong>Translating Business Needs:</strong> Skilled in understanding and converting business requirements into data-driven and technical solutions.</li>
                <li><strong>Adaptive Strategy:</strong> Proficient in adjusting strategies to meet evolving business needs in a dynamic environment.</li>
                <li><strong>Analytics Strategy Contribution:</strong> Actively participate in shaping and governing the analytics strategy, aligning it with business objectives.</li>
                <li><strong>Data-Driven Business Insights:</strong> Possess a strong acumen for business, adept at linking data modeling activities with business challenges and opportunities.</li>


        <h4>Product and Business:</h4>
                <li><strong>Product Metrics & Experimentation:</strong> Skilled in defining and tracking key product metrics, designing customer-facing experiments, and evaluating product changes through meticulous experiment design and analysis.</li>
                <li><strong>Holistic Product Understanding:</strong> Proficient in understanding both the technical and business aspects of Data Products, ensuring balanced decision-making that centers user needs.</li>
                <li><strong>Agile Methodology:</strong> Experienced in and embraces agile methodologies, ensuring flexibility and responsiveness in product development.</li>
                <li><strong>Feature Enhancement:</strong> Adept at identifying and integrating new features from diverse data sources to improve model performance and robustness.</li>
                <li><strong>Data Standards for Product Teams:</strong> Established standards and best practices for how product groups should interact with and utilize data.</li>
                <li><strong>Data-Driven Product Strategy:</strong> Proficient in analyzing product data to inform and guide product direction and strategy effectively.</li>
                <li><strong>Collaboration with UX Research:</strong> Partnered with UX research teams to design surveys and derive quantitative insights for enhanced customer experiences.</li>
                <li><strong>Data Evangelism in Product Development:</strong> Passionate about promoting a data-informed approach to product development among product managers, designers, and engineers.</li>
                <li><strong>Vision and Strategy for Product Expansion:</strong> Crafted vision and strategic roadmaps to accelerate expansion within large organizations, identifying and executing new product initiatives for large-scale solutions.</li>
        <h4>General:</h4>
                <li><strong>Adaptability and Flexibility:</strong> Exhibits a positive and adaptable attitude, readily adjusting to new technologies and industry challenges.</li>
                <li><strong>Continuous Learning:</strong> Actively researches and stays abreast of emerging technologies, state-of-the-art methods, and applications in data science.</li>
                <li><strong>Inquisitive Nature:</strong> Known for a curiosity-driven approach, constantly seeking answers and pushing boundaries in knowledge and application.</li>
                <li><strong>Documentation and Knowledge Sharing:</strong> Maintains comprehensive documentation of machine learning modeling processes and procedures.</li>
                <li><strong>Open Source and Community Involvement:</strong> Actively contributes to GitHub, open-source initiatives, research projects, and engages in Kaggle competitions.</li>
                <li><strong>Democratization of Data:</strong> Committed to making data knowledge and insights accessible across various teams and disciplines.</li>

        <hr>
        <h3 class="highlight">Contact Information</h3>
        <ul>
            <li>🌐: <a href="https://mroneai.com" target="_blank">mroneai.com</a></li>
            <li>🔗: <a href="https://linkedin.com/in/nitsmali" target="_blank">linkedin.com/in/nitsmali</a></li>
            <li>🐙: <a href="https://github.com/nitzmali" target="_blank">github.com/nitzmali</a></li>
            <li>✉️: <a href="mailto:nitsmali@hotmail.com">nitsmali@hotmail.com</a></li>
            <li>📞: (908)-275-7808</li>
        </ul>
        </div>
        <hr>
    """, unsafe_allow_html=True)

        # Further details can be added here based on the selected company
    st.download_button(label="Download Resume", data="Your resume content", file_name="assets/documents/Mali_Nitin_Resume_DS.pdf", mime="application/pdf")

        # Add more interactive or visual elements as needed




if __name__=='__main__':
  WorkExperiencePage().run()