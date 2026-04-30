import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Telecom Insights Hub", layout="wide")

# Title and Description
st.title("📊 Telecom Customer Analytics Dashboard")
st.markdown("""
This project showcases a full data pipeline: 
1. **Data Engineering** (Python/Pandas) 
2. **Business Intelligence** (Power BI) 
3. **Web Deployment** (Streamlit)
""")

# Sidebar Navigation
page = st.sidebar.selectbox("Navigate", ["Python Insights", "Power BI Report"])

if page == "Python Insights":
    st.header("🐍 Python-Driven Analysis")
    try:
        df = pd.read_csv('cleaned_churn_data.csv')
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Churn by Contract Type")
            fig = px.histogram(df, x="Contract", color="Churn", barmode="group", template="plotly_dark")
            st.plotly_chart(fig, use_container_width=True)
            
        with col2:
            st.subheader("Monthly Charges vs. Tenure")
            fig2 = px.scatter(df, x="tenure", y="MonthlyCharges", color="Churn", opacity=0.5)
            st.plotly_chart(fig2, use_container_width=True)
            
        st.write("### Data Preview")
        st.dataframe(df.head(10))
    except FileNotFoundError:
        st.error("Please run data_analysis.py first to generate the cleaned CSV file.")

elif page == "Power BI Report":
    st.header("📊 Interactive Power BI Report")
    st.info("Ensure your Power BI report is published to the web and paste the link below.")
    
    # The Power BI Embed URL (Replace this with your actual link)
    # Get this via: File -> Embed Report -> Publish to Web (Public)
    pbi_url = "https://app.powerbi.com/view?r=YOUR_REAL_EMBED_CODE_HERE"
    
    # Display the report in an iframe
    st.components.v1.iframe(pbi_url, height=600, scrolling=True)
    
    st.markdown("---")
    st.markdown("### Key Metrics Explained")
    st.write("- **Churn Rate:** Percentage of customers who left last month.")
    st.write("- **Customer Lifetime Value:** Estimated total revenue per customer.")
