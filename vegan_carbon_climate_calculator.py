import streamlit as st

# Healthy vegetable and grain icons for banner (mix of veggies and grains)
veggie_and_grain_icons = [
    "https://cdn-icons-png.flaticon.com/512/415/415733.png",  # carrot
    "https://cdn-icons-png.flaticon.com/512/414/414738.png",  # leafy greens
    "https://cdn-icons-png.flaticon.com/512/135/135663.png",  # rice grain
    "https://cdn-icons-png.flaticon.com/512/1715/1715926.png", # lentils/bowl
]

# Icons for the data points
ghg_icon = "https://cdn-icons-png.flaticon.com/512/4360/4360942.png"  # greenhouse gas / CO2 icon
time_icon = "https://cdn-icons-png.flaticon.com/512/2089/2089676.png"  # clock/time icon

st.set_page_config(page_title="Vegan Carbon Impact Calculator", layout="centered")

# Banner with vegetable and grain icons in a row
st.markdown(
    "<div style='display: flex; gap: 30px; justify-content: center; margin-bottom: 20px;'>"
    + "".join([f"<img src='{icon}' width='60' />" for icon in veggie_and_grain_icons])
    + "</div>",
    unsafe_allow_html=True,
)
st.markdown("<h1 style='color:#2d6a4f; font-family:verdana; font-weight:bold; text-align:center;'>Vegan Carbon Emissions & Climate Impact Calculator</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border:1px solid #95d5b2;'>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Set veganism adoption level")
    percent_vegan = st.slider(
        "Percentage of global population adopting veganism",
        min_value=0,
        max_value=100,
        value=0,
        step=5,
        help="Slide to estimate global vegan adoption"
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.info("Animal agriculture contributes ~14.5% of global GHG emissions.")

with col2:
    st.subheader("Global Impact")

    total_emissions = 7.3  # GT CO2e from animal ag
    carbon_budget_1_5 = 130  # GT CO2 budget

    emissions_saved = total_emissions * (percent_vegan / 100)
    added_years_1_5 = carbon_budget_1_5 / total_emissions * (percent_vegan / 100)
    
    st.markdown(
        f"""
        <div style="
            background-color:#d8f3dc;
            border-radius:15px;
            display:flex;
            align-items:center;
            padding:20px;
            margin-bottom:20px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        ">
            <img src="{ghg_icon}" width="70" style="margin-right:20px;"/>
            <div>
                <div style="font-weight:700; color:#40916c; font-size:18px;">Estimated Emissions Reduced</div
