import streamlit as st

# Healthy vegetable and grain icons for banner
banner_icons = [
    "https://cdn-icons-png.flaticon.com/512/415/415733.png",    # carrot
    "https://cdn-icons-png.flaticon.com/512/414/414738.png",    # leafy greens
    "https://cdn-icons-png.flaticon.com/512/135/135663.png",    # rice grain
    "https://cdn-icons-png.flaticon.com/512/1715/1715926.png"   # lentils / bowl
]

# Icons for the data points
ghg_icon = "https://cdn-icons-png.flaticon.com/512/4360/4360942.png"   # greenhouse gas icon
time_icon = "https://cdn-icons-png.flaticon.com/512/2089/2089676.png"  # clock/time icon

# App config
st.set_page_config(page_title="Vegan Carbon Impact Calculator", layout="centered")

# Display banner icons in a row centrally aligned
cols = st.columns(len(banner_icons))
for col, icon_url in zip(cols, banner_icons):
    col.image(icon_url, width=60)

st.title("Vegan Carbon Emissions & Climate Impact Calculator")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Set veganism adoption level")
    percent_vegan = st.slider(
        "Percentage of global population adopting veganism",
        min_value=0,
        max_value=100,
        value=0,
        step=5
    )
    st.info("Animal agriculture contributes about 14.5% of global greenhouse gas emissions.")

with col2:
    st.subheader("Global Impact")
    
    total_emissions = 7.3  # GT CO2e from animal agriculture
    carbon_budget_1_5 = 130  # GT CO2 budget for 1.5°C
    
    emissions_saved = total_emissions * (percent_vegan / 100)
    added_years = carbon_budget_1_5 / total_emissions * (percent_vegan / 100)
    
    st.image(ghg_icon, width=65, caption="Greenhouse Gas Emissions")
    st.metric("Estimated Emissions Reduced (GT CO2e/year)", f"{emissions_saved:.2f}")
    
    st.image(time_icon, width=65, caption="Time Added")
    st.metric("Added Years Until 1.5°C Threshold", f"{added_years:.1f}")

st.markdown("---")

st.write(
    "This calculator estimates how much global greenhouse gas emissions could be reduced "
    "by different levels of veganism adoption worldwide.\n\n"
    "Small lifestyle shifts can lead to meaningful climate benefits! 🌱"
)
