# portfolio_app.py
import streamlit as st

def main():
    st.title("Abhinav Kumar's Portfolio")

    st.header("Work Experience - Cimpress India Pvt. Ltd.")
    st.write("Software Developer | Bangalore, India | Aug 2021 - Present")
    st.write("• Orchestrated migration to AWS S3, optimizing data retrieval time by 40%...")
    st.write("• Implemented AWS Step Functions to streamline workflows, reducing processing time by 50%")
    st.write("• Experience in deploying Fargate and EC2 tasks from Docker containers")
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
