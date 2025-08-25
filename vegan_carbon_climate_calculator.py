import streamlit as st

VEGETABLE_IMAGES = {
    "carrot": "https://upload.wikimedia.org/wikipedia/commons/7/7f/Carrot_icon.svg",
    "broccoli": "https://upload.wikimedia.org/wikipedia/commons/2/28/Broccoli_icon.svg",
}

st.set_page_config(page_title="Vegan Carbon Impact Calculator", layout="centered")

st.markdown(
    """
    <div style="display:flex; align-items:center; margin-bottom: 10px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/1/1a/Vegetables_icon.svg" width="60" style="margin-right: 15px"/>
        <h1 style="color:#2E7D32; font-family: Arial, sans-serif;">Vegan Carbon Emissions & Climate Impact Calculator</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("---")

input_col, output_col = st.columns([1, 1])

with input_col:
    st.subheader("Adjust veganism level")
    percent_vegan = st.slider(
        "Percentage of global population adopting veganism", 0, 100, 0, 5
    )

with output_col:
    st.subheader("Global Impact")
    total_emissions = 7.3  # GT CO2e from animal ag
    carbon_budget_1_5 = 130  # GT CO2 budget
    
    emissions_saved = total_emissions
