# 📦 UrbanRoute Delivery Optimizer

## 📌 Problem Statement
Delivery startups struggle to optimise routes in dense urban areas where traffic patterns vary widely by time and locality. This project answers the question: *How might real-time and historical data reveal the most efficient delivery pathways?*

## 💡 Our Solution
Instead of just looking at the shortest physical distance, we use historical urban traffic data to predict **how long a delivery will take** based on the time of day and the distance. By leveraging Machine Learning, delivery dispatchers can identify peak traffic hours and optimize rider routes for maximum efficiency.

We used NYC Taxi data as a proxy for urban delivery vehicles, as they navigate the exact same dense urban bottlenecks.

## 🛠️ Features
- **Exploratory Data Analysis (EDA):** Discovered that Fridays are the busiest days and travel times spike during specific rush hours.
- **Machine Learning Model:** A predictive model trained on historical data to estimate trip duration based on time and distance.
- **Interactive Web App:** A Streamlit dashboard where dispatchers can plan routes and get instant time estimates.

## 🚀 How to Run the Project Locally

### 1. Setup Virtual Environment
Open your terminal and create a python virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install pandas matplotlib seaborn scikit-learn streamlit jupyter
```

### 3. Start the Delivery Optimizer Web App
To launch the interactive dashboard, run:
```bash
streamlit run app.py
```
*The app will automatically open in your web browser!*

### 4. View the Data Analysis (Optional)
If you want to view the data analysis and model training steps:
```bash
jupyter notebook
```
*(Open `Step1_Data_Loading.ipynb` in your browser)*


### Python Installmen

Python and Anaconda were successfully installed and validated using terminal-based version checks to ensure proper configuration and accessibility. A dedicated Pull Request was created to provide verifiable proof of environment readiness and repository integration. The setup was further demonstrated through a concise screen-recorded walkthrough covering installation verification and environment validation. The submission also addresses collaborative development practices by emphasizing the use of consistent Conda environments, dependency management, and aligned Python versions to minimize cross-machine compatibility issues during the sprint.