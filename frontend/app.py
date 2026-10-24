import os
import requests
import streamlit as st

# backend url may come from environment when starting the containers
DEFAULT_BACKEND_URL = "http://backend:7860"
PREDICT_URL = f'{os.getenv("BACKEND_URL", DEFAULT_BACKEND_URL)}/v1/predict'

# streamlit config
st.set_page_config(
    page_title = "SuperKart Online Prediction"
)

st.title("SuperKart Online Prediction")

# Input fields for product and store data
api_data = {
    "Product_Weight": st.number_input("Product Weight", min_value=0.0, value=12.25),
    "Product_Sugar_Content": st.selectbox("Product Sugar Content", ["Low Sugar", "Regular", "No Sugar"], index=0),
    "Product_Allocated_Area": st.number_input("Product Allocated Area", min_value=0.0, value=0.04),
    "Product_Type": st.selectbox("Product Type", ['Snack Foods', 'Soft Drinks', 'Frozen Foods', 'Fruits and Vegetables',
                                                  'Starchy Foods', 'Household', 'Dairy', 'Meat', 'Baking Goods', 'Health and Hygiene',
                                                  'Canned', 'Breads', 'Hard Drinks', 'Seafood', 'Others', 'Breakfast'], index=10),
    "Product_MRP": st.number_input("Product MRP", min_value=0.0, value=160.42),
    "Store_Size": st.selectbox("Store Size", ["Low", "Medium", "High"], index=1),
    "Store_Location_City_Type": st.selectbox("Store Size", ["Tier 1", "Tier 2", "Tier 3"], index=1),
    "Store_Type": st.selectbox("Store Size", ["Departmental Store", "Supermarket Type 1", "Supermarket Type 2", "Food Mart"], index=2),
    "Store_Age": st.number_input("Store Age (Years)", min_value=0, value=17),
    "Model_Name": st.selectbox("Model Name", ["superkart_adaboost_model_v1_0.joblib", "superkart_bagging_model_v1_0.joblib"])
}

# when "Predict" button is clicked, call the API
if st.button("Predict", type='primary'):
    # timeout=(connect_timeout, read_timeout) in seconds
    response = requests.post(PREDICT_URL, json=api_data, timeout=(10, 30))
    if response.status_code == 200:
        result = response.json()
        predicted_sales = result["Sales"]
        st.markdown(f"**Predicted Product Store Sales Total: ${predicted_sales:,.2f}**")
    else:
        st.error("Error in API request")
