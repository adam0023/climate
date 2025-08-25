import streamlit as st

# Icons: vegetables and grains for banner
banner_icons = [
    "https://cdn-icons-png.flaticon.com/512/415/415733.png",    # carrot
    "https://cdn-icons-png.flaticon.com/512/414/414738.png",    # leafy greens
    "https://cdn-icons-png.flaticon.com/512/135/135663.png",    # rice grain
    "https://cdn-icons-png.flaticon.com/512/1715/1715926.png"   # lentils / bowl
]

# Icons for key metrics
ghg_icon = "https://cdn-icons-png.flaticon.com/512/4360/4360942.png"   # greenhouse gas icon
time_icon = "https://cdn-icons-png.flaticon.com/512/2089/2089676.png"  # clock/time icon

st.set_page_config(page_title="Vegan Carbon Impact Calculator", layout="centered")

# Banner: display healthy veggies and grains side by side
st.markdown(
    "<div style='display:flex; justify-content:center; gap:40px; margin-bottom:20px;'>"
    + "".join([f"<img src='{icon}' width='60'/>" for icon in banner_icons])
    + "</div>",
    unsafe_allow_html=True,
)

# Title in professional font and color
st.markdown("<h1 style='text-align:center; font-family:Verdana; color:#2d6a4f;'>Vegan Carbon Emissions & Climate Impact Calculator</h1>", unsafe_allow_html=True)

st.markdown("<hr style='border:1px solid #95d5b2;'>", unsafe_allow_html=True)

# Layout - two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Set veganism adoption level")
    percent_vegan = st.slider(
        "Percentage of global population adopting veganism",
        0, 100, 0, 5,
        help="Estimate the share of global population going vegan"
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.info("Animal agriculture contributes about 14.5% of global greenhouse gas emissions.")

with col2:
    st.subheader("Global Impact")

    total_emissions = 7.3  # GT CO2e from animal agriculture
    carbon_budget_1_5 = 130  # GT CO2 budget for 1.5°C

    emissions_saved = total_emissions * (percent_vegan / 100)
    added_years = carbon_budget_1_5 / total_emissions * (percent_vegan / 100)

    # Emissions reduced card with GHG icon
    st.markdown(
        f"""
        <div style="
            background-color:#d8f3dc;
            border-radius:12px;
            padding:20px;
            display:flex;
            align-items:center;
            margin-bottom:20px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        ">
            <img src="{ghg_icon}" width="65" style="margin-right:20px;" />
            <div>
                <div style="font-weight:bold; font-size:18px; color:#40916c;">
                    Estimated Emissions
