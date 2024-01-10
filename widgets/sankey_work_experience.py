import streamlit as st
from streamlit.components.v1 import html
from PIL import Image
import streamlit.components.v1 as components
import plotly.graph_objects as go
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.colors as mcolors
import plotly.express as px

def render_image():

    # Your experience_skills_mapping dictionary remains the same
    experience_skills_mapping = {
        "Temenos": {
            "Stakeholder Collaboration": {
                "Communication": {
                    "Subcategories": ["Effective Articulation", "Data Storytelling"],
                    "Weight": 5
                },
                "Collaboration and Cross Functional": {
                    "Subcategories": ["Cross-Functional Collaboration", "Teamwork for Innovation"],
                    "Weight": 10
                }
            },
            "Data Mining and Analysis": {
                "Data Acquisition & Transformation": {
                    "Subcategories": ["Data Infrastructure & Management", "Data Warehousing & Reporting"],
                    "Weight": 20
                },
                "Analytics": {
                    "Subcategories": ["Product Analytics", "Statistical Analysis"],
                    "Weight": 40
                }
            },
            "A/B Testing for UI": {
                "Machine Learning": {
                    "Subcategories": ["ML Techniques & Algorithms"],
                    "Weight": 10
                },
                "Analytics": {
                    "Subcategories": ["Product Analytics Strategy"],
                    "Weight": 80
                },
                "Programming/Tools": {
                    "Subcategories": ["Languages & Frameworks"],
                    "Weight": 20
                }
            },
            "Customer Segmentation and Pricing Strategy": {
                "Machine Learning": {
                    "Subcategories": ["ML Techniques & Algorithms"],
                    "Weight": 10
                },
                "Analytics": {
                    "Subcategories": ["Product Analytics"],
                    "Weight": 80
                },
                "Business Strategy": {
                    "Subcategories": ["Data-Driven Business Insights"],
                    "Weight": 10
                }
            },
            "Statistical and Mathematical Methodologies": {
                "Machine Learning": {
                    "Subcategories": ["ML Techniques & Algorithms"],
                    "Weight": 20
                },
                "Statistics": {
                    "Subcategories": ["Statistical Knowledge", "Statistical Specialized Techniques"],
                    "Weight": 20
                }
            },
            "Product Management Collaboration": {
                "Collaboration and Cross Functional": {
                    "Subcategories": ["Cross-Functional Collaboration", "Teamwork for Innovation"],
                    "Weight": 10
                },
                "Business Strategy": {
                    "Subcategories": ["Translating Business Needs", "Analytics Strategy Contribution"],
                    "Weight": 80
                }
            },
            "Database Analysis for Product Development": {
                "Data Acquisition & Transformation": {
                    "Subcategories": ["Data Infrastructure & Management", "Data Warehousing & Reporting"],
                    "Weight": 40
                }
            },
            "Advanced Testing Strategies Development": {
                "Programming/Tools": {
                    "Subcategories": ["Languages & Frameworks"],
                    "Weight": 40
                },
                "Lead": {
                    "Subcategories": ["Team Leadership", "Strategic Management"],
                    "Weight": 10
                },
                "Team Management": {
                    "Subcategories": ["Efficient Project Handling", "Culture of Accountability"],
                    "Weight": 10
                }
            }
        },
        "Bristol Myers Squibb": {
            "Stakeholder Collaboration": {
                "Communication": {
                    "Subcategories": ["Effective Articulation", "Data Storytelling"],
                    "Weight": 40
                },
                "Collaboration and Cross Functional": {
                    "Subcategories": ["Cross-Functional Collaboration", "Teamwork for Innovation"],
                    "Weight": 40
                }
            },
            "Logical Model Development": {
                "Data Acquisition & Transformation": {
                    "Subcategories": ["Data Infrastructure & Management", "Data Warehousing & Reporting"],
                    "Weight": 20
                }
            },
            "Analytics Report Development": {
                "Visualization": {
                    "Subcategories": ["Proficient in Tableau", "Matplotlib"],
                    "Weight": 20
                },
                "Data Acquisition & Transformation": {
                    "Subcategories": ["Data Warehousing & Reporting"],
                    "Weight": 20
                }
            },
            "Sales Data Processing Automation": {
                "Programming/Tools": {
                    "Subcategories": ["Languages & Frameworks"],
                    "Weight": 20
                },
                "Data Acquisition & Transformation": {
                    "Subcategories": ["Data Infrastructure & Management", "SQL Expertise"],
                    "Weight": 80
                }
            },
            "Automated Reporting System Development": {
                "Programming/Tools": {
                    "Subcategories": ["Web Technologies & Systems"],
                    "Weight": 20
                },
                "Data Acquisition & Transformation": {
                    "Subcategories": ["Data Infrastructure & Management","SQL Expertise"],
                    "Weight": 20
                }
            },
            "Operational Reporting in Tableau": {
                "Visualization": {
                    "Subcategories": ["Proficient in Tableau"],
                    "Weight": 20
                }
            },
            "Client Engagement Analysis": {
                "Analytics": {
                    "Subcategories": ["Product Analytics", "Statistical Analysis"],
                    "Weight": 40
                },
                "Communication": {
                    "Subcategories": ["Effective Articulation", "Data Storytelling"],
                    "Weight": 20
                }
            },
            "Dashboard Performance Enhancement": {
                "Visualization": {
                    "Subcategories": ["Proficient in Tableau"],
                    "Weight": 20
                },
                "Programming/Tools": {
                    "Subcategories": ["Languages & Frameworks"],
                    "Weight": 20
                }
            },
            "ETL Infrastructure Engineering": {
                "Cloud, Containerization, ML Ops": {
                    "Subcategories": ["Cloud Platforms"],
                    "Weight": 60
                },
                "Data Acquisition & Transformation": {
                    "Subcategories": ["Data Infrastructure & Management","SQL Expertise"],
                    "Weight": 20
                }
            },
            "Geographic Sales Data Analysis": {
                "Machine Learning": {
                    "Subcategories": ["ML Techniques & Algorithms"],
                    "Weight": 20
                },
                "Analytics": {
                    "Subcategories": ["Product Analytics"],
                    "Weight": 20
                }
            }
        },
        "ZS": {
            "Stakeholder Collaboration": {
                "Communication": {
                    "Subcategories": ["Effective Articulation", "Data Storytelling"],
                    "Weight": 40
                },
                "Collaboration and Cross Functional": {
                    "Subcategories": ["Cross-Functional Collaboration", "Teamwork for Innovation"],
                    "Weight": 40
                }
            },
            "CNNs and LLMs for User Interaction Analysis at ZS": {
                "Deep Learning": {
                    "Subcategories": ["DL Frameworks & Techniques", "DL Model Types"],
                    "Weight": 60
                },
                "GenAI and NLP": {
                    "Subcategories": ["GenAI"],
                    "Weight": 40
                },
                "Machine Learning": {
                    "Subcategories": ["ML Theory & Application", "ML Model Evaluation & Optimization"],
                    "Weight": 25
                },
                "Data Acquisition & Transformation": {
                    "Subcategories": ["Mining with NLP","SQL Expertise"],
                    "Weight": 10
                }
            },
            "Multi-channel Optimization and Experimentation at ZS": {
                "Statistics": {
                    "Subcategories": ["Statistical Specialized Techniques"],
                    "Weight": 30
                },
                "Machine Learning": {
                    "Subcategories": ["ML Techniques & Algorithms"],
                    "Weight": 20
                },
                "Analytics": {
                    "Subcategories": ["Product Analytics Strategy"],
                    "Weight": 40
                },
                "Business Strategy": {
                    "Subcategories": ["Data-Driven Business Insights"],
                    "Weight": 20
                }
            },
            "Machine Learning Strategy Translation at ZS": {
                "Machine Learning": {
                    "Subcategories": ["ML Techniques & Algorithms"],
                    "Weight": 25
                },
                "Programming/Tools": {
                    "Subcategories": ["Languages & Frameworks"],
                    "Weight": 40
                },
                "Business Strategy": {
                    "Subcategories": ["Translating Business Needs"],
                    "Weight": 10
                }
            },
            "Data Analysis and Interpretation at ZS": {
                "Programming/Tools": {
                    "Subcategories": ["Languages & Frameworks", "Advanced Data Handling"],
                    "Weight": 40
                },
                "Machine Learning": {
                    "Subcategories": ["ML Techniques & Algorithms"],
                    "Weight": 20
                },
                "Statistics": {
                    "Subcategories": ["Statistical Knowledge"],
                    "Weight": 50
                }
            },
            "Data-Driven Organizational Growth and Efficiency at ZS": {
                "Collaboration and Cross Functional": {
                    "Subcategories": ["Cross-Functional Collaboration"],
                    "Weight": 20
                },
                "Team Management": {
                    "Subcategories": ["Efficient Project Handling", "Culture of Accountability"],
                    "Weight": 40
                },
                "Lead": {
                    "Subcategories": ["Stakeholder Influence"],
                    "Weight": 40
                }
            }
        },
        "Aktana": {
            "Stakeholder Collaboration": {
                "Communication": {
                    "Subcategories": ["Effective Articulation", "Data Storytelling"],
                    "Weight": 40
                },
                "Collaboration and Cross Functional": {
                    "Subcategories": ["Cross-Functional Collaboration", "Teamwork for Innovation"],
                    "Weight": 30
                }
            },
            "Contextual Intelligence Engine Development Aktana": {
                "Machine Learning": {
                    "Subcategories": ["ML Theory & Application", "ML Model Evaluation & Optimization"],
                    "Weight": 30
                },
                "Cloud, Containerization, ML Ops": {
                    "Subcategories": ["Cloud Platforms"],
                    "Weight": 60
                },
                "Business Strategy": {
                    "Subcategories": ["Data-Driven Business Insights"],
                    "Weight": 40
                }
            },
            "Machine Learning and Analytics Data Platform Integration Aktana": {
                "Data Acquisition & Transformation": {
                    "Subcategories": ["Data Infrastructure & Management", "Data Warehousing & Reporting"],
                    "Weight": 40
                },
                "Machine Learning": {
                    "Subcategories": ["ML Techniques & Algorithms"],
                    "Weight": 30
                },
                "Cloud, Containerization, ML Ops": {
                    "Subcategories": ["Cloud Platforms"],
                    "Weight": 60
                },
                "Data Acquisition & Transformation": {
                    "Subcategories": ["SQL Expertise"],
                    "Weight": 90
            }
            },
            "Neural Network-Based Channel Propensity Models Development Aktana": {
                "Machine Learning": {
                    "Subcategories": ["ML Techniques & Algorithms"],
                    "Weight": 30
                },
                "GenAI and NLP": {
                    "Subcategories": ["GenAI"],
                    "Weight": 60
                },
                "Business Strategy": {
                    "Subcategories": ["Data-Driven Business Insights"],
                    "Weight": 40
                },
                "Product and Business": {
                    "Subcategories": ["Data-Driven Product Strategy"],
                    "Weight": 60
                }
            },
            "No-Code Automated Machine Learning Platform Development Aktana": {
                "Machine Learning": {
                    "Subcategories": ["ML Theory & Application", "ML Model Evaluation & Optimization"],
                    "Weight": 25
                },
                "Programming/Tools": {
                    "Subcategories": ["Languages & Frameworks", "Web Technologies & Systems"],
                    "Weight": 20
                },
                "Collaboration and Cross Functional": {
                    "Subcategories": ["Cross-Functional Collaboration", "Teamwork for Innovation"],
                    "Weight": 15
                },
                "Product and Business": {
                    "Subcategories": ["Data Standards for Product Teams", "Data Evangelism in Product Development"],
                    "Weight": 70
                }
            },
            "Statistical and Machine Learning Solutions Implementation and Maintenance Aktana": {
                "Machine Learning": {
                    "Subcategories": ["ML Theory & Application", "ML Model Evaluation & Optimization"],
                    "Weight": 25
                },
                "Statistics": {
                    "Subcategories": ["Statistical Knowledge", "Statistical Specialized Techniques"],
                    "Weight": 60
                },
                "Team Management": {
                    "Subcategories": ["Efficient Project Handling", "Talent Development"],
                    "Weight": 40
                }
            },
            "Technical Vision and Strategy Influencing for Engineering Teams Aktana": {
                "Business Strategy": {
                    "Subcategories": ["Translating Business Needs", "Analytics Strategy Contribution"],
                    "Weight": 40
                },
                "Lead": {
                    "Subcategories": ["Team Leadership", "Strategic Management"],
                    "Weight": 40
                },
                "Team Management": {
                    "Subcategories": ["Global Team Management", "Decision-Making and Negotiation"],
                    "Weight": 40
                }
            }
        }
    }

    # Sort the experiences within each company
    for company in experience_skills_mapping:
        experience_skills_mapping[company] = dict(sorted(experience_skills_mapping[company].items()))


    # Initialize lists for Sankey diagram
    labels = []
    source = []
    target = []
    value = []

    # Flag to include the second level (experiences)
    include_second_level = False  # Set this to False if you want to exclude the second level

    # Function to add label and return its index
    def add_label(label):
        if label not in labels:
            labels.append(label)
        return labels.index(label)

    # Function to process each subcategory
    def process_subcategory(experience_index, category_index, subcategories, weight):
        for sub_category in subcategories:
            sub_category_index = add_label(sub_category)
            source.append(category_index)
            target.append(sub_category_index)
            value.append(weight)  # Weight for category to sub-category connection

    # Function to process each category
    def process_category(company_index, experience_index, categories, include_experience):
        for category, details in categories.items():
            category_index = add_label(category)
            # Connect either the company or the experience to the category,
            # depending on whether the second level is included
            source_index = experience_index if include_experience else company_index
            source.append(source_index)
            target.append(category_index)
            value.append(details["Weight"])  # Weight for experience to category connection
            # Process the subcategories
            process_subcategory(experience_index, category_index, details["Subcategories"], details["Weight"])

    # Populate labels, source, target, and value lists
    for company, experiences in experience_skills_mapping.items():
        company_index = add_label(company)
        for experience, categories in experiences.items():
            experience_index = add_label(experience)
            if include_second_level:
                # Connect the company to the experience
                source.append(company_index)
                target.append(experience_index)
                experience_weight = sum(detail["Weight"] for detail in categories.values())
                value.append(experience_weight)  # Sum of weights for the experience
            # Process each category within the experience
            process_category(company_index, experience_index, categories, include_second_level)

    company_colors = {'Temenos': '#1f77b4',
    'Bristol Myers Squibb': '#2ca02c',
    'ZS': '#d62728',
    'Aktana': '#9467bd',
    'Communication': '#17becf',
    'Collaboration and Cross Functional': '#9edae5',
    'Data Acquisition & Transformation': '#7f7f7f',
    'Analytics': '#ff7f0e',
    'Machine Learning': '#ffbb78',
    'Programming/Tools': '#c49c94',
    'Business Strategy': '#e377c2',
    'Statistics': '#f7b6d2',
    'Visualization': '#c7c7c7',
    'Deep Learning': '#c5b0d5',
    'GenAI and NLP': '#8c564b',
    'Lead': '#c49c94',
    'Team Management': '#c7c7c7',
    'Product and Business': '#dbdb8d',
    'Data Infrastructure & Management': '#17becf',
    'Data Warehousing & Reporting': '#9edae5',
    'Product Analytics': '#ff7f0e',
    'Statistical Analysis': '#ffbb78',
    'Languages & Frameworks': '#c49c94',
    'Web Technologies & Systems': '#e377c2',
    'Data-Driven Business Insights': '#f7b6d2',
    'Statistical Knowledge': '#c7c7c7',
    'Statistical Specialized Techniques': '#c5b0d5',
    'Effective Articulation': '#8c564b',
    'Data Storytelling': '#c49c94',
    'ML Techniques & Algorithms': '#c7c7c7',
    'ML Theory & Application': '#dbdb8d',
    'ML Model Evaluation & Optimization': '#17becf',
    'DL Frameworks & Techniques': '#9edae5',
    'DL Model Types': '#ff7f0e',
    'GenAI': '#ffbb78',
    'Cross-Functional Collaboration': '#c49c94',
    'Teamwork for Innovation': '#e377c2',
    'Translating Business Needs': '#f7b6d2',
    'Analytics Strategy Contribution': '#c7c7c7',
    'Efficient Project Handling': '#c5b0d5',
    'Culture of Accountability': '#8c564b',
    'Global Team Management': '#c49c94',
    'Decision-Making and Negotiation': '#c7c7c7',
    'Stakeholder Influence': '#dbdb8d',
    'Data-Driven Product Strategy': '#17becf',
    'Collaboration with UX Research': '#0000ff',
    'Data Evangelism in Product Development': '#0100fe',
    'Vision and Strategy for Product Expansion': '#0200fd',
    'Adaptability and Flexibility': '#0300fc',
    'Continuous Learning': '#0400fb',
    'Inquisitive Nature': '#0500fa',
    'Documentation and Knowledge Sharing': '#0600f9',
    'Open Source and Community Involvement': '#0700f8',
    'Democratization of Data': '#0800f7'}


    # Let's assign new gradient colors to all keys in the company_colors dictionary

    # First, get all the keys in the dictionary
    all_keys = list(company_colors.keys())

    # For this example, let's use three gradients
    gradients = {
        'Gradient 1': ('blue', 'green'),
        'Gradient 2': ('red', 'yellow'),
        'Gradient 3': ('purple', 'orange')
    }


    # Since we want to assign a unique color to each key in the company_colors dictionary,
    # we'll generate a sufficient number of unique colors using the previously defined function.

    import random
    def generate_unique_colors(num_colors, seed=None):
        """
        Generate a list of unique colors as hexadecimal values.
        If a seed is given, the random colors generated will be the same every time.
        """
        # If a seed is provided, use it to ensure reproducibility
        if seed is not None:
            np.random.seed(seed)
            
        # Generate random colors in RGB space
        colors = np.random.rand(num_colors, 3)
        
        # Convert to hex
        hex_colors = [mcolors.to_hex(color) for color in colors]
        return hex_colors

    # Example usage:
    seed_value = None  # Set the seed for reproducibility
    num_elements = len(company_colors)  # Replace with the actual number of elements you have
    unique_colors = generate_unique_colors(num_elements, seed=seed_value)

    # Assign the unique colors to each key in the company_colors dictionary
    for (key, _), color in zip(company_colors.items(), unique_colors):
        company_colors[key] = color

    company_colors




    def get_link_color(source_index):
        # Find the label for the given source index
        label = labels[source_index]
        # Return the corresponding color, default to a neutral color if not found
        return company_colors.get(label, '#cccccc')

    # Create the Sankey diagram
    # Now, when creating the Sankey diagram, specify colors for links
    color_scale = px.colors.sequential.gray
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=20,
            thickness=20,
            line=dict(color='black', width=0.5),
            label=labels,
            #color="black"  # Set the node color to black (if you want)
        ),
        link=dict(
            source=source,
            target=target,
            value=value,
            #color=[get_link_color(s) for s in source]  # Assign colors based on source company
            #color=[color_scale[int(val/max(value)*len(color_scale)-1)] for val in value],  # Apply color scale based on value
        ),
        # Set font properties for labels here
        textfont=dict(color='black', size=13, family='Arial, sans-serif')
    )])

    # Update the layout with a larger figure size
    fig.update_layout(
            title={
        'text': "Experience Skills Mapping",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
        font=dict(size=12, color='black', family='Arial, sans-serif'),
        #autosize=True,
        #margin=dict(l=0, r=0, t=0, b=0),
        width=1600,  # Width of the figure in pixels
        height=1050   # Height of the figure in pixels
    )

    # Add annotations if needed
    fig.add_annotation(
        text="Company",
        x=0.02,
        y=0.9,
        showarrow=False,
        font=dict(
            size=14,
            color="black",
            family='Arial, sans-serif'
        ),
        align="center",
        xanchor="center",
        yanchor="top",
        xref="paper",
        yref="paper"
    )

        # Add annotations if needed
    fig.add_annotation(
        text="Skills Category",
        x=0.5,
        y=0.9,
        showarrow=False,
        font=dict(
            size=14,
            color="black"
        ),
        align="center",
        xanchor="center",
        yanchor="top",
        xref="paper",
        yref="paper"
    )

    fig.add_annotation(
    text="For definition, please visit tab -> WORK EXPERIENCE",
    x=0.5,
    y=0.00001,
    showarrow=False,
    font=dict(
        size=10,
        color="black"
    ),
    align="center",
    xanchor="center",
    yanchor="top",
    xref="paper",
    yref="paper"
)

    return fig

