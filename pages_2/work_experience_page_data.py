import pandas as pd 
from hydralit import HydraHeadApp
class WorkExperiencePageData():
    work_experience = [
        {
            "role": "BT",
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
            "role": "Data Science Engineer",
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
    ]
        
    zs_associates_projects = [
    
                    {
                    "title": "Advanced Data Management in Pharma",
                    "image": "https://github.com/nitzmali/portfolio/blob/main/assets/images/segmentation.png?raw=true", 
                    "description": "Led a comprehensive project for top pharma client resulting in a significant enhancement in data architecture and machine learning model efficacy.",
                    "details": """
                    """,
                    "insights": "This project exemplified the integration of advanced data processing and machine learning techniques to elevate analytics and decision-making capabilities in the pharmaceutical sector.",
                    "visualizations": "",  
                    "code": "",  
                    "conclusion": "Successfully enabled enhanced data-driven strategies for global pharma clients, ensuring precision and efficiency in their analytics operations.",
                    "pdf": False,
                    "pdf_file_path": ""
                },
                {
                    "title": "Commercial Sanofi One AI Diamond Machine Learning Model Ops",
                    "image": "https://github.com/nitzmali/portfolio/blob/main/assets/images/ZS_2.1.jpg?raw=true", 
                    "description": "Pioneered an end-to-end ML Ops project, achieving significant advancements in efficiency, reliability, and scalability in ML operations for the pharmaceutical industry.",
                    "details": """
                    """,
                    "insights": "The project marked a milestone in data handling efficiency, setting new standards in automated data processing within the pharmaceutical sector.",
                    "visualizations": "",  
                    "code": "",  
                    "conclusion": "The project's success demonstrated the transformative impact of automation in data pipeline management, paving the way for future advancements in the field.",
                    "pdf": False,
                    "pdf_file_path": ""
                },

    ]

    webmd_projects = [{
    "title": "Integration of Machine Learning and Analytics Platform Using Delta Lake on AWS",
    "image": "",  # Add the URL or path to the relevant image
    "description": "Spearheaded the integration of a robust machine learning and analytics data platform utilizing Delta Lake on AWS. This significantly enhanced algorithmic workflows and analytics, creating a scalable solution that streamlined data from raw to refined stages. It accelerated data readiness for ML models and the Contextual Intelligence Engine (CIE), saving considerable time for data scientists by creating recursive feature stores for efficient model building.",
    "details": "",  # Add any additional detailed explanation about the project if necessary
    "insights": "",  # Insights gained or impact of the project
    "visualizations": "",  # URL or path to visualizations, if any
    "code": "",  # URL to code repository, if applicable
    "conclusion": "",  # Summary of the outcomes or conclusions of the project
    "pdf": False,
    "pdf_file_path": ""
    }]


    aktana_projects = [
                {
                "title": "Revolutionizing Customer Engagement with CRI Score",
                "image": "https://github.com/nitzmali/portfolio/blob/main/assets/images/aktana_1.png?raw=true", 
                "description": "Spearheaded the development of the Customer Relationship Index (CRI), significantly enhancing omnichannel engagement tracking and data-driven marketing decisions.",
                "details": """
                """,
                "insights": "The CRI Score project marked a significant advancement in measuring and understanding customer engagement, fostering a data-centric approach in marketing.",
                "visualizations": "",  
                "code": "",  
                "conclusion": "The successful implementation of the CRI Score transformed marketing strategies, proving its efficacy in enhancing customer engagement and sales forecasting.",
                "pdf": False,
                "pdf_file_path": ""
            },
    {
        "title": "Optimizing HCP Engagement with Advanced Channel Propensity Models",
        "image": "",
        "description": "Led a groundbreaking project to leverage neural networks in enhancing engagement rates with healthcare professionals, achieving a 25% increase in targeted communications efficiency.",
        "details": """
        """,
        "insights": "This project demonstrated the power of machine learning in transforming healthcare marketing strategies, setting a new benchmark in engagement analytics.",
        "visualizations": "",
        "code": "", 
        "conclusion": "The successful implementation of channel propensity models marked a major advancement in data-driven healthcare marketing.",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
            "title": "Revolutionizing Pharma Marketing with Advanced Attribution Modelling",
            "image": "",  
            "description": "Led a transformative project in pharmaceutical marketing, employing advanced attribution modeling to optimize ROI and reshape marketing strategies, resulting in substantial improvements in resource allocation and sales outcomes.",
            "details": """
            """,
            "insights": "This project marked a significant advancement in attribution modeling within pharmaceutical marketing, setting new standards for data-driven strategy formulation.",
            "visualizations": "",  
            "code": "",  
            "conclusion": "The project's success lies in its ability to provide actionable insights, leading to smarter marketing investments and enhanced sales performance.",
            "pdf": False,
            "pdf_file_path": ""
        },
            {
        "title": "Optimizing Pharma Marketing with AI-Driven HCP Engagement Strategies",
        "image": "", 
        "description": "Spearheaded a critical project integrating AI and ML models to revolutionize pharmaceutical marketing strategies, resulting in markedly improved HCP engagement, increased prescribing behavior, and optimized ROI.",
        "details": """
        """,
        "insights": "This project has significantly advanced the capabilities of pharmaceutical marketing, utilizing AI and ML to deliver precise, effective strategies that resonate with HCPs.",
        "visualizations": "", 
        "code": "", 
        "conclusion": "A landmark project in the field, setting a new standard for data-driven, AI-enhanced pharmaceutical marketing and sales strategies.",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "Gen AI Powered Next Best Action Recommendations",
        "image": "",
        "description": "Pioneered an innovative AI-driven Next Best Action recommendation system, significantly enhancing sales rep efficiency and HCP engagement in the healthcare sector. This cutting-edge project utilized advanced Seq2Seq models with LSTM and attention mechanisms, leading to a marked improvement in sales conversion rates and a more personalized approach to healthcare professional interactions.",
        "details": """
        """,
        "insights": "This project demonstrated the power of machine learning in transforming healthcare marketing strategies, setting a new benchmark in engagement analytics.",
        "visualizations": "",
        "code": "", 
        "conclusion": "The successful implementation of channel propensity models marked a major advancement in data-driven healthcare marketing.",
        "pdf": False,
        "pdf_file_path": ""
            },

    ]



    bms_projects = [
{
                "title": "Revolutionizing Pharma Analytics: Advanced Data Science Integration",
                "image": "",
                "description": "This project ambitiously integrates advanced data science and AI/ML technologies into a comprehensive analytics platform, revolutionizing pharmaceutical industry practices. The result is a marked improvement in operational efficiency, marketing ROI, and a deeper understanding of patient and consumer needs, setting new benchmarks in data-driven strategies in healthcare.",
                "details": """
                """,
                "insights": "This project demonstrated the power of machine learning in transforming healthcare marketing strategies, setting a new benchmark in engagement analytics.",
                "visualizations": "",
                "code": "", 
                "conclusion": "The successful implementation of channel propensity models marked a major advancement in data-driven healthcare marketing.",
                "pdf": False,
                "pdf_file_path": ""
            },
    {
        "title": "Precision Customer Engagement: Advanced Segmentation and Journey Analytics",
        "image": "https://github.com/nitzmali/portfolio/blob/main/assets/images/segmentation.png?raw=true",
        "description": "This project revolutionizes customer engagement in the healthcare sector by integrating advanced data analytics and machine learning techniques. We focus on precise customer segmentation and detailed journey mapping, utilizing a blend of data from diverse sources.",
        "details": "",
        "insights": "",
        "visualizations": "",
        "code": "",
        "conclusion": "",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "Dynamic HCP Segmentation: Monte Carlo Simulations in Pharma Marketing",
        "image": "",  # Add the URL or path to the relevant image
        "description": "This project exemplifies the innovative application of Monte Carlo simulations and K-means clustering to segment healthcare professionals (HCPs) in pharmaceutical marketing. Focusing on capturing and analyzing complex behavioral patterns, the project employed a variety of tools like Python, R, and Tableau to model HCP behaviors and preferences. This advanced approach led to improved segmentation accuracy, resulting in higher ROI and more effective marketing strategies.",
        "details": "",
        "insights": "",
        "visualizations": "",
        "code": "",
        "conclusion": "",
        "pdf": False,
        "pdf_file_path": ""
    },
   
    # ... More projects can be added as needed ...
    ]

    temenos_projects = [
    {
        "title": "Advanced Analytics for Investment Opportunity Identification",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Collaborated with 23 stakeholders to leverage advanced analytics in identifying investment opportunities and risks, guiding strategic decision-making in asset management.",
        "details": "",
        "insights": "",
        "visualizations": "",
        "code": "",
        "conclusion": "",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "Data Mining and Analysis for Wealth Management Optimization",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Conducted extensive data mining and analysis across multiple databases to optimize investment strategies and product offerings in wealth management.",
        "details": "",
        "insights": "",
        "visualizations": "",
        "code": "",
        "conclusion": "",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "A/B Testing for Enhanced Client Engagement in Wealth Management",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Orchestrated comprehensive A/B testing for client interfaces, achieving a 23% increase in client engagement and satisfaction through tailored wealth management solutions.",
        "details": "",
        "insights": "",
        "visualizations": "",
        "code": "",
        "conclusion": "",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "Innovative Statistical Methods in Financial Product Development",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Employed innovative statistical methods to develop and analyze financial products, enhancing portfolio diversification and risk management in asset management.",
        "details": "",
        "insights": "",
        "visualizations": "",
        "code": "",
        "conclusion": "",
        "pdf": False,
        "pdf_file_path": ""
    }

    # ... More projects can be added as needed ...
    ]

    webmd_projects = [
    {
        "title": "WebMD's Advanced AWS Data Science Platform",
        "image": "",  # Add the URL or path to the relevant image
        "description": "This project highlights WebMD's development of a sophisticated data science and analytics platform using AWS services and Delta Lake. It emphasizes operational efficiency, advanced data management, and machine learning capabilities, leading to significant improvements in data processing, analytics, and business outcomes.",
        "details": "",
        "insights": "",
        "visualizations": "",
        "code": "",
        "conclusion": "",
        "pdf": False,
        "pdf_file_path": ""
    }
        ]

