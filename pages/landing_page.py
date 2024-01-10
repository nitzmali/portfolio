import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
from streamlit_timeline import timeline
from widgets import navbar
class Landingpage:
  def run(self):

    #st.markdown("<h1 style='text-align: left; color: black;'>Nitin Mali</h1>", unsafe_allow_html=True)
    with st.sidebar:
       submit_button = st.button(label="*Download Resume*")
    '''
    left_co, cent_co,last_co = st.columns(3)
    with left_co:
        st.markdown("![Alt Text](https://media.giphy.com/media/CVtNe84hhYF9u/giphy.gif)")
        st.write("")
    
    '''
    # Profile Picture
    left_co, right_co = st.columns([1.2, 1.2])
    with right_co:
          st.image("https://github.com/nitzmali/portfolio/blob/main/assets/images/nitin_image_exchange_place.gif?raw=true",width=300)
    
    
    with left_co:
      #st.write("# Hi, I'm Nitin! 👋 ")
      st.markdown("""
      <style>
          h1, p{
          text-align: left;
          margin-top: 0;
          margin-bottom: 0;
          padding-top: 50px;
          padding-bottom: 0;}
      </style>
      <h1> Hi, I'm Nitin! 👋 </h1>
      <p><i> I'm on a quest to unlock the potential of AI, making it an accessible ally for professionals to redefine the boundaries of what's possible in their business landscapes.</i></p>
  """, unsafe_allow_html=True)
       
    
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
        <p>I weave the art of product innovation with the precision of data science, transforming the complex tapestry of data into actionable insights. At the heart of my journey lies a pivotal role at ZS, where I have pioneered analytics and strategic solutions. My adventures at Aktana, Webmd and Bristol Myers Squib have sharpened my acumen, showcasing my adaptability across diverse industries.</p>
        <p>My unwavering mission is to distill vast oceans of data into potent elixirs of business intelligence, fuelling the growth of enterprises in this data-driven era. I navigate the realms of AI, Product Analytics, and Strategic Planning with an alchemist’s touch, melding them into transformative business strategies.</p>
        <hr>
        <h3 class="highlight"> Professional Experience</h3>
        
        <h4>ZS</h4><p><strong>Data Scientist</strong> | Jan 2023 - Present | New York, United States</p>
        <h4>WebMD</h4>
        <p><strong>Data Engineer Manager</strong> | Nov 2022 - Jan 2023 | New York, United States</p>
        <h4>Aktana</h4>
        <p><strong>Data Scientist</strong> | Nov 2019 - Nov 2022 | California, United States</p>
        <h4>Bristol Myers Squibb</h4>
        <p><strong>Data Analyst</strong> | Jun 2018 - Oct 2019 | California, United States</p>
        <h4>Temenos</h4>
        <p><strong>Software Engineer</strong> | Jul 2015 - Oct 2016 | California, United States</p>
        <h4>Indian Space Research Organization</h4>
        <p><strong>Data Scientist Intern</strong> | Jan 2015 - May 2015 | California, United States</p>
        <hr>
        <h3 class="highlight"> Skills Overview</h3>
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
        <h3 class="highlight">Education</h3>
        <h4>Rutgers University</h4>
        <p><strong>     Master of Science (M.S) in Data Science</strong> | GPA: 3.7 | Jan 2017 - May 2018</p>
        <h4>M.S. Ramaiah Institute of Technology</h4>
        <p><strong>     Bachelor of Engineering (B.E) in Computer Science Engineering</strong> | GPA: 3.7 | Jul 2011 - May 2015</p>
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
        <h2 style='text-align: left; color: black; padding-top: 0; padding-bottom: 0;'>Career Timeline</h2>
    """, unsafe_allow_html=True)

        
    # load data
    with open('data/example_time_line_nitin.json', "r") as f:
        data = f.read()

    #st.markdown("<h2 style='text-align: left; color: black;'>Career Timeline</h1>", unsafe_allow_html=True)
    '''
    st.markdown("""
        <style>
            h1 {text-align: left;
            margin-top: 0;
            margin-bottom: 0;
            padding-top: 0;
            padding-bottom: 0;}
        </style>
        <h1> Career Timeline </h1>
    """, unsafe_allow_html=True)
    '''
    timeline(data, height=800)






    

if __name__=='__main__':
  Landingpage().run()