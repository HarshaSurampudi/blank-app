import streamlit as st
import pandas as pd
from datetime import datetime

# Page config for wider layout
st.set_page_config(layout="wide")

# Load data
df = pd.read_csv('similar_texts_cleaned_filtered.csv')

# Center the title
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.title("Mulugu Astrology - Similar Predictions")

base_url = "https://www.mulugu.com/raasiphalaalu"

# Center the date selector
col1, col2, col3 = st.columns([1,2,1])
with col2:
    selected_date = st.selectbox("Select a date", df['Date 1'].unique())
    show_predictions = st.button("Show Results")

if show_predictions:
    # Get and sort filtered predictions by similarity score
    filtered_df = df[df['Date 1'] == selected_date].sort_values('Similarity', ascending=False)
    
    # Display selected date's prediction in the center
    col1, col2, col3 = st.columns([2,3,2])
    with col2:
        date_obj = datetime.strptime(selected_date, '%Y-%m-%d')
        formatted_date = date_obj.strftime('%B %d, %Y')
        st.subheader(f"Selected Date: {formatted_date}")
        main_url = f"{base_url}/{date_obj.year}/{date_obj.month}/{date_obj.day}.jpg"
        st.image(main_url, use_container_width=True)
    
    # Display similar predictions heading in the center
    st.header("Similar Predictions")
    
    # Create rows of 3 columns each
    for i in range(0, len(filtered_df), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(filtered_df):
                row = filtered_df.iloc[i + j]
                with cols[j]:
                    date_obj = datetime.strptime(row['Date 2'], '%Y-%m-%d')
                    formatted_date = date_obj.strftime('%B %d, %Y')
                    st.subheader(formatted_date)
                    url = f"{base_url}/{date_obj.year}/{date_obj.month}/{date_obj.day}.jpg"
                    st.image(url, use_container_width=True)
