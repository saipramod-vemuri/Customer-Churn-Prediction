import pandas as pd
import numpy as np

def run_telecom_analysis(input_csv):
    # 1. Load the raw dataset
    df = pd.read_csv(input_csv)
    
    # 2. Data Cleaning
    # Convert TotalCharges to numeric, replacing errors with NaN then filling with 0
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce').fillna(0)
    
    # 3. Feature Engineering (Adding Value for Power BI)
    # Create a 'Tenure Bracket' for easier visualization
    def tenure_bucket(t):
        if t <= 12: return '0-1 Year'
        elif t <= 24: return '1-2 Years'
        elif t <= 48: return '2-4 Years'
        else: return '4+ Years'
    
    df['Tenure_Group'] = df['tenure'].apply(tenure_bucket)
    
    # Calculate Average Revenue Per User (ARPU)
    df['ARPU'] = df['TotalCharges'] / df['tenure'].replace(0, 1)
    
    # 4. Statistical Summary (The 'Analysis' Part)
    churn_summary = df.groupby('Churn').agg({
        'MonthlyCharges': 'mean',
        'tenure': 'mean',
        'TotalCharges': 'sum'
    }).reset_index()
    
    # 5. Export Cleaned Data for Power BI
    df.to_csv('cleaned_churn_data.csv', index=False)
    print("Success: 'cleaned_churn_data.csv' is ready for Power BI.")
    return churn_summary

# Usage: run_telecom_analysis('telecom_churn.csv')
