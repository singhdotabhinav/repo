import time
import streamlit as st
# from streamlit_timeline import st_timeline

def main():
    # dark_mode = st.sidebar.checkbox("Dark Mode")
    # theme_config_light = """
    # [theme]
    # base="light"
    # """
    # theme_config_dark = """
    # [theme]
    # base="dark"
    # """
    # if dark_mode:
    #     st.markdown(theme_config_dark, unsafe_allow_html=True)
    # else:
    #     st.markdown(theme_config_light, unsafe_allow_html=True)
    # st.markdown(light_css, unsafe_allow_html=True)
    st.title(" Abhinav Kumar's Portfolio")
    st.header(" Cimpress India Pvt. Ltd.")
    st.write("Software Developer     |     Bangalore, India     |     Aug 2021 - Present")
    with st.beta_expander(" Work Experience @Cimpress"):
        
        st.markdown("• Orchestrated the migration of data storage to AWS S3, optimising data retrieval time by 40% and enhancing scalability for the company's growing customer base.")
        st.markdown("• Implemented AWS Step Functions to streamline and automate complex workflows, reducing processing time by 50% and improving overall system efficiency.")
        st.markdown("• Experience in deploying Fargate and EC2 tasks from Docker containers, showcasing the ability to manage containerized applications efficiently, whether through serverless container orchestration (Fargate) or traditional virtual machines.")
        st.markdown("• Proficiency in CI/CD pipelines involving automating code integration, testing and deployment feedback and reliable software delivery. Also, used scheduler to automate routine tasks and workflows on schedules, enhancing efficiency and reducing manual effort.")
        st.markdown("• Building data pipelines using AWS Step Functions and Lambda functions to automate the flow of data, facilitating data processing and storage in a structured and efficient manner, ensuring scalability and reliability.")
        st.markdown("• Adeptness in Snowflake and an in-depth understanding of its capabilities, including data warehouse management and analytic execution.")
        st.markdown("• Hands-on experience with Serverless computing, developing and deploying applications without the need of managing server infrastructure, resulting in cost-efficiency and scalable solutions.")
        st.markdown("• Handling, managing, processing and enriching vast datasets, often in order of millions of records, to extract valuable insights, optimised data storage, and enhanced data-driven decision-making processes.")
        st.markdown("• Practical involvement with AWS APIs, including conversion of lambda functions into API Gateway endpoints, and the creation of robust test cases to ensure the reliability and functionality of the API layer.")
        st.markdown("• Proficiency in utilising testing framework such as karate for API testing and jest for testing of react applications, ensuring the thorough validation of software components across various layers of development.")
        st.markdown("• Engaged in GPT integration and leveraging its capabilities to address specific business use cases, demonstrating AI integration in solving real-world challenges.")
        st.markdown("• In-Depth expertise in DynamoDB, including practical experience in implementing parallel scan techniques to optimise search operation, having proficiency in designing efficient and scalable NoSQL database solutions, particularly for large-scale data retrieval and analysis.")
        st.markdown("• Practical experience in developing and working with Flask APIs, demonstrating proficiency in building web applications and services using lightweight and flexible python framework.")
        st.markdown("• Engaged in Slack integration for applications, demonstrating the ability to seamlessly incorporate Slack functionality into software solutions, enabling efficient communication and collaboration within teams and applications.")
        st.markdown('''
            <style>
            [data-testid="stMarkdownContainer"] ul{
                padding-left:40px;
            }
            </style>
            ''', unsafe_allow_html=True)
        
    
    
    st.header("Education - Siddaganga Institute of Technology")
    st.write("Computer Science and Engineering - Graduation Date: Aug 2021 | CGPA - 8.4")
    
    

    # Expander to reveal/hide project details
    st.header("Project Experience")
    with st.beta_expander(" Ecommerce-Webapp"):
        st.write(
            "Inspired by India's endeavours to help India promote indigenous brands. To solve this problem, I have come up with a website, which will help people to buy electronic goods with better ratings. We have more than 1k active users, fetching real-time data from firebase for the products and Amazon API for updating the price of the product."
        )
    with st.beta_expander(" Emotion detection using Artificial Intelligence"):
        st.write(
            "Developed this project to detect the current emotion of humans and to recommend some videos to watch in order to make their mood better. For example, if a person is sad, he will be made to watch some motivational videos. The project was designed using Python and Deep Learning using Flask Framework."
        )
    with st.beta_expander(" Developer Android Application ApniMaa"):
        st.write(
            "Developed a food delivery Android application in the group of three. The application focused on ordering the food, delivering the food, login and logout through firebase."
        )
    with st.beta_expander(" Developed online store for college"):
        st.write(
            "Developed a website that allowed the students of SIT to buy and sell used items. They can click the pictures of the product they want to sell and others can buy it, with flexible negotiations."
        )

    st.header("Skills")

    # Define proficiency levels for each skill
    skills = {
        "Python": 90,
        "AWS": 80,
        "Serverless Computing": 75,
        "CI/CD": 85,
        "Snowflake": 70,
        "Docker": 90,
        "Pytest": 80
    }
    with st.beta_expander("Show Skills"):
        # Button to trigger the animation
        animate_button = True

        # Display skills with animated progress bars upon button click
        if animate_button:
            for skill, proficiency in skills.items():
                st.write(f"{skill}:")
                progress_bar = st.progress(0)
                for i in range(101):
                    time.sleep(0.009)  # Adjust the speed of the animation
                    progress_bar.progress(i)
                progress_bar.progress(proficiency)
    timeline()


    
def timeline():
    st.title("Your Resume Portfolio")

    # Sidebar for Vertical Timeline
    st.sidebar.title("Timeline")
    add_timeline_event("2015 - 2018", "Bachelor's Degree", "University of XYZ")
    add_timeline_event("2018 - 2020", "Software Engineer", "Tech Company A")
    add_timeline_event("2020 - Present", "Senior Software Engineer", "Tech Company B")

    # Main Content
    st.write("## About Me")
    st.write("Welcome to my resume portfolio! I am a passionate and experienced software engineer...")
    
    
def add_timeline_event(date, title, description):
    st.sidebar.text(date)
    st.sidebar.text(title)
    st.sidebar.text(description)
    st.sidebar.markdown("---")





if __name__ == "__main__":
    main()
   


