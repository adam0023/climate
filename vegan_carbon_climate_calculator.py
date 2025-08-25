import streamlit as st

# Vegetable image URLs (clean SVG icons hosted online)
carrot_img = "https://upload.wikimedia.org/wikipedia/commons/7/7f/Carrot_icon.svg"
broccoli_img = "https://upload.wikimedia.org/wikipedia/commons/2/28/Broccoli_icon.svg"
veggies_icon = "https://upload.wikimedia.org/wikipedia/commons/1/1a/Vegetables_icon.svg"

st.set_page_config(page_title="Vegan Carbon Impact Calculator", layout="centered")

# Title with vegetable icon
st.image(veggies_icon, width=60)
st.title("Vegan Carbon Emissions & Climate Impact Calculator")

st.write("---")

# Layout: two columns for input and output
col1, col2 = st.columns(2)

with col1:
    st.header("Adjust veganism level")
    percent_vegan = st.slider("Percentage of global population adopting veganism", 0, 100, 0, 5)

with col2:
    st.header("Global Impact")

    total_emissions = 7.3  # GT CO2e from animal ag
    carbon_budget_1_5 = 130  # GT CO2 budget

    emissions_saved = total_emissions * (percent_vegan / 100)
    added_years_1_5 = carbon_budget_1_5 / total_emissions * (percent_vegan / 100)

    # Show emissions saved metric with icon
    st.image(carrot_img, width=50)
    st.metric("Estimated Emissions Reduced", f"{emissions_saved:.2f} GT CO2e/year")

    # Show added years metric with icon
    st.image(broccoli_img, width=50)
    st.metric("Added Years Until 1.5°C Threshold", f"{added_years_1_5:.1f} years")

st.write("---")

st.write(
    "Animal agriculture contributes ~14.5% of global greenhouse gas emissions. "
    "This tool estimates emissions saved and additional time gained toward climate goals "
    "based on your veganism adoption level.\n\nSmall changes add up to big impact! 🌱"
)
