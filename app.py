# portfolio_app.py
import streamlit as st

def main():
    st.title("Abhinav Kumar's Portfolio")

    st.header("Work Experience - Cimpress India Pvt. Ltd.")
    st.write(
        "Software Developer, Bangalore, India\n"
        "Aug 2021 - Present\n"
        "Orchestrated the migration of data storage to AWS S3, optimizing data retrieval time by 40%..."
        # (Include all other work experience details)
    )

    st.header("Education - Siddaganga Institute of Technology")
    st.write("Computer Science and Engineering")

    st.header("Project Experience - NoChinano.com")
    st.write(
        "Co-Founder and Developer, Tumakuru, India\n"
        "Graduation Date: Aug 2021\n"
        "Inspired by India's endeavors to help India boycott Chinese brands..."
        # (Include all other project details)
    )

    st.header("Skills")
    st.write(
        "Python, AWS (Step-Functions, S3, Lambda, EC2, Fargate, DynamoDB), "
        "Serverless Computing, CI/CD, Snowflake, Docker, Pytest"
    )

if __name__ == "__main__":
    main()
