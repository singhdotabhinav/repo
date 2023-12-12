# portfolio_app.py
import streamlit as st

def main():
    st.title("Abhinav Kumar's Portfolio")

    st.header("Work Experience - Cimpress India Pvt. Ltd.")
    st.write(
        "Software Developer | Bangalore, India | Aug 2021 - Present\n"
        "• Orchestrated migration to AWS S3, optimizing data retrieval time by 40%...\n"
        "• Implemented AWS Step Functions to streamline workflows, reducing processing time by 50%...\n"
        "• Experience in deploying Fargate and EC2 tasks from Docker containers..."
        # (Include all other work experience details)
    )

    st.header("Education - Siddaganga Institute of Technology")
    st.write("Computer Science and Engineering")

    # Button to reveal/hide project details
    show_projects = st.button("Show Projects")

    if show_projects:
        st.header("Project Experience - NoChinano.com")
        st.write(
            "Co-Founder and Developer | Tumakuru, India\n"
            "Graduation Date: Aug 2021\n"
            "Inspired by India's endeavors to boycott Chinese brands, developed a website...\n"
            "• More than 1k active users\n"
            "• Fetching real-time data from Firebase for products and Amazon API for price updates..."
            # (Include all other project details)
        )

    st.header("Skills")
    st.write(
        "• Python\n"
        "• AWS (Step-Functions, S3, Lambda, EC2, Fargate, DynamoDB)\n"
        "• Serverless Computing\n"
        "• CI/CD\n"
        "• Snowflake\n"
        "• Docker\n"
        "• Pytest"
    )

if __name__ == "__main__":
    main()
