import streamlit as st

# Use a cleaner vegetable icon style
VEGETABLE_IMAGE_URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Vegetables_icon.svg/512px-Vegetables_icon.svg.png"

st.set_page_config(page_title="Vegan Carbon Impact Calculator", layout="centered")

# Title with vegetable icon
st.markdown(
    f"""
    <div style="display:flex; align-items:center;">
        <img src="{VEGETABLE_IMAGE_URL}" width="60" style="margin-right:15px"/>
        <h1 style="color:#2E7D32;">Vegan Carbon Emissions & Climate Impact Calculator</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("---")

# Use columns to separate input and output for cleaner presentation
input_col, output_col = st.columns(2)

with input_col:
    st.subheader("Adjust veganism level")
    percent_vegan = st.slider(
        "Percentage of global population adopting veganism", 0, 100, 0, 5
    )

with output_col:
    st.subheader("Your impact")
    total_emissions = 7.3  # GT CO2e from animal ag
    carbon_budget_1_5 = 130  # GT CO2 budget
    
    emissions_saved = total_emissions * (percent_vegan / 100)
    added_years_1_5 = carbon_budget_1_5 / total_emissions * (percent_vegan / 100)

    st.metric(
        label="Estimated Emissions Reduced (GT CO2e/year)",
        value=f"{emissions_saved:.2f}"
    )
    st.metric(
        label="Added Years Until 1.5°C Threshold",
        value=f"{added_years_1_5:.1f}"
    )

st.markdown(
    """
    ---
    Animal agriculture contributes ~14.5% of global greenhouse gas emissions.
    This tool estimates emissions saved and additional time gained toward climate goals based on your veganism adoption level.

    Small changes add up to big impact! 🌱
    """
)

