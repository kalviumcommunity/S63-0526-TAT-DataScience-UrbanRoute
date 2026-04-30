import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="UrbanRoute Optimizer", page_icon="📦", layout="wide")

st.title("📦 UrbanRoute Delivery Optimizer")
st.markdown("Predicting delivery travel times in dense urban areas using historical traffic data.")

@st.cache_data
def load_data_and_model():
    df = sns.load_dataset('taxis')
    df = df.dropna()
    df = df[(df['distance'] > 0)]
    df['duration_minutes'] = (df['dropoff'] - df['pickup']).dt.total_seconds() / 60
    df = df[df['duration_minutes'] > 0]
    df['pickup_hour'] = df['pickup'].dt.hour
    
    X = df[['distance', 'pickup_hour']]
    y = df['duration_minutes']
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Calculate average duration by hour for the chart
    hourly_avg = df.groupby('pickup_hour')['duration_minutes'].mean().reset_index()
    return model, hourly_avg

model, hourly_avg = load_data_and_model()

# Sidebar for inputs makes it look fancy
st.sidebar.header("🗺️ Plan a Route")
distance = st.sidebar.slider("Route Distance (miles):", 0.5, 20.0, 3.0, 0.5)
hour = st.sidebar.slider("Time of Day (Hour):", 0, 23, 17, 1)

# Main content layout
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("⏱️ Prediction")
    if st.sidebar.button("Predict Delivery Time", type="primary"):
        prediction = model.predict([[distance, hour]])
        st.metric(label="Estimated Travel Time", value=f"{prediction[0]:.0f} mins", delta=f"{distance} miles at {hour}:00")
        st.success("Optimal route time calculated based on historical traffic!")
        st.balloons()
    else:
        st.info("👈 Adjust the sliders in the sidebar and click Predict!")

with col2:
    st.subheader("📊 City Traffic Trends")
    st.markdown("Average historical delivery time across different hours of the day:")
    st.bar_chart(hourly_avg.set_index('pickup_hour'))
