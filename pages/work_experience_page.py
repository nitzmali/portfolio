import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
from streamlit_timeline import timeline
import matplotlib.pyplot as plt
import seaborn as sns
import json


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
            "icon": "https://github.com/nitzmali/portfolio/blob/main/assets/images/zs_associates_logo.jpeg?raw=true"
        },
        {
            "role": "Data Engineer Manager",
            "company": "Webmd",
            "period": "November 2022 - January 2023",
            "location": "Bengaluru, India",
            "details": """
                <ul>
                    <li>Streamlining data processes and enhancing pipeline efficiency. Championed the integration of big data technologies, including AWS andSpark, into the company's data architecture.</li>
                    <li>Initiated collaborations with product and customer analytics teams to derive actionable insights from tools such as Google Analytics and Adobe Analytics.</li>
                </ul>
            """,
            "icon": "https://github.com/nitzmali/portfolio/blob/main/assets/images/webmd-190918.jpg?raw=true"  # Replace with the actual URL or path to your icon
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
            "icon": "https://github.com/nitzmali/portfolio/blob/main/assets/images/Aktana_logo_full_blue.jpg?raw=true"
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
            "icon": "https://github.com/nitzmali/portfolio/blob/main/assets/images/bms2.jpg?raw=true"
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
        "icon": "https://github.com/nitzmali/portfolio/blob/main/assets/images/temenos_logo.jpg?raw=true"  # Replace with the actual URL or path to your icon
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
            width: 30px;  /* Adjust the size of the icon */
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
        st.markdown(f"""
            <div class="job-container">
                <div class="job-title">{job['role']}</div>
                <div class="job-company">
                    {job['company']} <img class="job-icon" src="{job['icon']}" alt="Icon">
                </div>
                <div class="job-period-location">{job['period']} - {job['location']}</div>
            </div>
        """, unsafe_allow_html=True)

        with st.expander("See details"):
            st.markdown(f"<div>{job['details']}</div>", unsafe_allow_html=True)






















        # Further details can be added here based on the selected company


        # Add more interactive or visual elements as needed




if __name__=='__main__':
  WorkExperiencePage().run()