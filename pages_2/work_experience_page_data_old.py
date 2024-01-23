import pandas as pd 
from hydralit import HydraHeadApp
class WorkExperiencePageData():
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
        
    zs_associates_projects = [
    
    {
        "title": "Enhancing Digital Tool Engagement with CNNs",
        "image": "https://github.com/nitzmali/portfolio/blob/main/assets/images/segmentation.png?raw=true",  # Add the URL or path to the relevant image
        "description": "Led the development and application of Convolutional Neural Networks (CNNs) to analyze complex user interaction data, resulting in a 25% enhancement in digital tool engagement.",
        "details": """
        """,
        "insights": "Insights gained or impact of the project.",
        "visualizations": "",  # URL or path to visualizations, if any
        "code": "",  # URL to code repository, if applicable
        "conclusion": "Successfully integrated advanced CNN techniques for meaningful user interaction analysis.",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "Personalizing HCP-User Interactions with Generative AI",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Employed Transformer-based Large Language Models for in-depth textual analysis and content generation, enabling personalized and relevant healthcare professional (HCP) user interactions.",
        "details": "Detailed explanation or additional information about the project, if necessary.",
        "insights": "Insights gained or impact of the project.",
        "visualizations": "",  # URL or path to visualizations, if any
        "code": "",  # URL to code repository, if applicable
        "conclusion": "Achieved a more personalized approach in HCP interactions using Generative AI.",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "Enhancing Digital Engagement Efficiency with Advanced Analytics",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Engineered sophisticated strategies integrating Bayesian Methods, Logistic Regression, and Ensemble Methods for multi-channel optimization, leading to a 10% improvement in digital engagement efficiency.",
        "details": "Detailed explanation or additional information about the project, if necessary.",
        "insights": "Insights gained or impact of the project.",
        "visualizations": "",  # URL or path to visualizations, if any
        "code": "",  # URL to code repository, if applicable
        "conclusion": "Significantly improved digital engagement efficiency through integrated analytical strategies.",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "Boosting Credit Risk Analysis Efficiency",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Pioneered the creation of advanced credit risk models utilizing CNNs, Generative AI, and LLMs, enhancing loan evaluation accuracy and process efficiency by 30%.",
        "details": "Detailed explanation or additional information about the project, if necessary.",
        "insights": "Insights gained or impact of the project.",
        "visualizations": "",  # URL or path to visualizations, if any
        "code": "",  # URL to code repository, if applicable
        "conclusion": "Revolutionized credit risk analysis with state-of-the-art AI technologies.",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "Optimizing Financial Forecasting with Advanced Methods",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Employed Bayesian Methods, Logistic Regression, and Ensemble Methods in developing financial forecasting models, significantly improving the accuracy of predictions for asset values and market trends.",
        "details": "Detailed explanation or additional information about the project, if necessary.",
        "insights": "Insights gained or impact of the project.",
        "visualizations": "",  # URL or path to visualizations, if any
        "code": "",  # URL to code repository, if applicable
        "conclusion": "Enhanced financial forecasting accuracy through advanced analytical methods.",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "Fraud Detection and Risk Management Enhancement",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Designed and implemented sophisticated fraud detection algorithms using Generative AI and CNNs, achieving a notable reduction in online transaction fraud. Led team efforts in investment risk management, culminating in the development of a real-time risk monitoring dashboard.",
        "details": "Detailed explanation or additional information about the project, if necessary.",
        "insights": "Insights gained or impact of the project.",
        "visualizations": "",  # URL or path to visualizations, if any
        "code": "",  # URL to code repository, if applicable
        "conclusion": "Successfully reduced fraud and enhanced risk management using AI technologies.",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "Transforming Financial Modeling with AI",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Transformed financial modeling techniques at Vanguard by adapting CNNs and LLMs for analyzing market trends and asset performance, markedly increasing asset valuation accuracy.",
        "details": "Detailed explanation or additional information about the project, if necessary.",
        "insights": "Insights gained or impact of the project.",
        "visualizations": "",  # URL or path to visualizations, if any
        "code": "",  # URL to code repository, if applicable
        "conclusion": "Advanced the field of financial modeling through the integration of AI technologies.",
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
        "title": "Development of Contextual Intelligence Engine",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Orchestrated the development of a Contextual Intelligence Engine (CIE) leveraging machine learning models with Python and Spark on AWS EMR, resulting in a 40% uplift in targeted engagement and streamlined data workflow automation.",
        "details": "",
        "insights": "",
        "visualizations": "",
        "code": "",
        "conclusion": "",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "Integration of Machine Learning and Analytics Data Platform",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Spearheaded the integration of a robust machine learning and analytics data platform utilizing Delta Lake on AWS, significantly enhancing algorithmic workflows and analytics.",
        "details": "",
        "insights": "",
        "visualizations": "",
        "code": "",
        "conclusion": "",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "Development of Neural Network-Based Channel Propensity Models",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Collaborated with product managers to develop neural network-based channel propensity models, enhancing healthcare professional engagement by 25%.",
        "details": "",
        "insights": "",
        "visualizations": "",
        "code": "",
        "conclusion": "",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "Predictive Analytics for Digital Content Personalization",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Utilized predictive analytics and behavioral modeling in AI for digital content personalization, achieving a 32% increase in conversion rates.",
        "details": "",
        "insights": "",
        "visualizations": "",
        "code": "",
        "conclusion": "",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "Optimization of Marketing Mix Models Using Gradient Boosting Machines",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Advanced Gradient Boosting Machines were used to optimize marketing mix models, leading to a 21% improvement in digital marketing ROI.",
        "details": "",
        "insights": "",
        "visualizations": "",
        "code": "",
        "conclusion": "",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "Development of Automated Machine Learning Platform",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Collaborated with engineers and product managers to develop a user-centric, no-code automated machine learning platform using Knime and Databricks MLflow.",
        "details": "",
        "insights": "",
        "visualizations": "",
        "code": "",
        "conclusion": "",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "Implementation and Maintenance of Machine Learning Solutions",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Implemented and maintained over 15 statistical and machine learning solutions, covering the entire life cycle from development to deployment, including metadata management and optimizing model performance at scale.",
        "details": "",
        "insights": "",
        "visualizations": "",
        "code": "",
        "conclusion": "",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "Influencing Engineering Strategy with Machine Learning Insights",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Influenced the technical vision and strategies of engineering teams by translating machine learning insights into actionable, data-driven recommendations.",
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



    bms_projects = [
    {
        "title": "Development of Logical Models and Data Architecture",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Built and refined over 36 logical models, collaborating with database administrators to develop physical models and overall data architecture, thereby enhancing the understanding of large datasets.",
        "details": "",
        "insights": "",
        "visualizations": "",
        "code": "",
        "conclusion": "",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "Analytics Reporting for Sales, Patient, and Claims Data",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Developed comprehensive analytics reports for Sales, Patient, and Claims data using Python and SQL within the XPERT platform, streamlining processes and saving over 60 hours monthly.",
        "details": "",
        "insights": "",
        "visualizations": "",
        "code": "",
        "conclusion": "",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "Automation of BMS Sales Data Processing",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Automated BMS Sales Data Processing for the US, using a Python-triggered email automation script to refresh data daily and publish on the Dashboard.",
        "details": "",
        "insights": "",
        "visualizations": "",
        "code": "",
        "conclusion": "",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "Automated Reporting Systems for Performance Metrics",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Led the development of automated reporting systems for key performance metrics using Python and SQL, saving more than 30 hours each week.",
        "details": "",
        "insights": "",
        "visualizations": "",
        "code": "",
        "conclusion": "",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "Dynamic Operational Reports in Tableau",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Created dynamic operational reports in Tableau integrated with XPERT, enhancing team coordination and operational efficiency, resulting in significant cost savings.",
        "details": "",
        "insights": "",
        "visualizations": "",
        "code": "",
        "conclusion": "",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "Client Engagement Metrics Management",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Managed and analyzed client engagement metrics within the XPERT platform, optimizing client services and improving workforce allocation.",
        "details": "",
        "insights": "",
        "visualizations": "",
        "code": "",
        "conclusion": "",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "Enhancement of Dashboard Performance",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Enhanced dashboard performance in collaboration with Bristol Myers Squibb using XPERT, resulting in a 40% increase in user engagement.",
        "details": "",
        "insights": "",
        "visualizations": "",
        "code": "",
        "conclusion": "",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "ETL Infrastructure Implementation",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Engineered and implemented ETL infrastructures at XSUNT, integrating SQL databases with Python to boost decision-making efficiency by 42% through enhanced data processing.",
        "details": "",
        "insights": "",
        "visualizations": "",
        "code": "",
        "conclusion": "",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "Python Clustering for Geographic Sales Data Analysis",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Utilized Python clustering methods to analyze geographic sales data, identifying and strategically improving underperforming markets, contributing to a 4% increase in profits.",
        "details": "",
        "insights": "",
        "visualizations": "",
        "code": "",
        "conclusion": "",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "Advanced Customer Segmentation and Cohort Analysis",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Collaborated with product and sales teams to apply advanced customer segmentation and cohort analysis, leading to a strategic 21% pricing reduction for key segments, increasing annual revenue by over $100,000.",
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
        "title": "Advanced Customer Segmentation and Cohort Analysis",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Implemented advanced customer segmentation and cohort analysis, leading to a 21% optimized pricing strategy for high-value investment portfolios, boosting revenue by $500,000.",
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
    },
    {
        "title": "Tailored Analytics Solutions for Wealth Management",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Tailored analytics solutions to meet specific needs in wealth management, enhancing product development and investment performance.",
        "details": "",
        "insights": "",
        "visualizations": "",
        "code": "",
        "conclusion": "",
        "pdf": False,
        "pdf_file_path": ""
    },
    {
        "title": "Advanced Testing Strategies for Financial Systems",
        "image": "",  # Add the URL or path to the relevant image
        "description": "Led the creation of advanced testing strategies for financial systems, focusing on performance tuning and monitoring to maintain 99.9% system uptime, ensuring consistent reliability in financial transactions and reporting.",
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

    '''
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
    '''