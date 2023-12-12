# portfolio_app.py
import streamlit as st

def main():
    st.title("Abhinav Kumar's Portfolio")

    st.header("Work Experience - Cimpress India Pvt. Ltd.")
    st.write("Software Developer | Bangalore, India | Aug 2021 - Present")
    st.markdown("Orchestrated the migration of data storage to AWS S3, optimising data retrieval time by 40% and enhancing scalability for the company's growing customer base.")
    st.markdown("Implemented AWS Step Functions to streamline and automate complex workflows, reducing processing time by 50% and improving overall system efficiency.")
    st.makdown("Experience in deploying Fargate and EC2 tasks from Docker containers, showcasing the ability to manage containerized applications efficiently, whether through serverless container orchestration (Fargate) or traditional virtual machines.")
    st.makdown("Proficiency in CI/CD pipelines involving automating code integration, testing and deployment feedback and reliable software delivery. Also, used scheduler to automate routine tasks and workflows on schedules, enhancing efficiency and reducing manual effort.")
    st.makdown("Building data pipelines using AWS Step Functions and Lambda functions to automate the flow of data, facilitating data processing and storage in a structured and efficient manner, ensuring scalability and reliability.")
    st.makdown("Adeptness in Snowflake and an in-depth understanding of its capabilities, including data warehouse management and analytic execution.")
    st.makdown("Hands-on experience with Serverless computing, developing and deploying applications without the need of managing server infrastructure, resulting in cost-efficiency and scalable solutions.")
    st.makdown("Handling, managing, processing and enriching vast datasets, often in order of millions of records, to extract valuable insights, optimised data storage, and enhanced data-driven decision-making processes.")
    st.makdown("Practical involvement with AWS APIs, including conversion of lambda functions into API Gateway endpoints, and the creation of robust test cases to ensure the reliability and functionality of the API layer.")
    st.makdown("Proficiency in utilising testing framework such as karate for API testing and jest for testing of react applications, ensuring the thorough validation of software components across various layers of development.")
    st.makdown("Engaged in GPT integration and leveraging its capabilities to address specific business use cases, demonstrating AI integration in solving real-world challenges.")
    st.makdown("In-Depth expertise in DynamoDB, including practical experience in implementing parallel scan techniques to optimise search operation, having proficiency in designing efficient and scalable NoSQL database solutions, particularly for large-scale data retrieval and analysis.")
    st.makdown("Practical experience in developing and working with Flask APIs, demonstrating proficiency in building web applications and services using lightweight and flexible python framework.")
    st.makdown("Engaged in Slack integration for applications, demonstrating the ability to seamlessly incorporate Slack functionality into software solutions, enabling efficient communication and collaboration within teams and applications.")
    
    
    
    st.header("Education - Siddaganga Institute of Technology")
    st.write("Computer Science and Engineering")

    # Expander to reveal/hide project details
    with st.beta_expander("Project Experience - NoChinano.com"):
        st.write(
            "Co-Founder and Developer | Tumakuru, India<br>"
            "Graduation Date: Aug 2021<br>"
            "Inspired by India's endeavors to boycott Chinese brands, developed a website...<br>"
            "• More than 1k active users<br>"
            "• Fetching real-time data from Firebase for products and Amazon API for price updates..."
            # (Include all other project details)
        )

    st.header("Skills")
    st.write(
        "• Python<br>"
        "• AWS (Step-Functions, S3, Lambda, EC2, Fargate, DynamoDB)<br>"
        "• Serverless Computing<br>"
        "• CI/CD<br>"
        "• Snowflake<br>"
        "• Docker<br>"
        "• Pytest"
    )

if __name__ == "__main__":
    main()
