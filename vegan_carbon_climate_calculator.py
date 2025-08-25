import streamlit as st

# Vegetable & grain images - vegan healthy food icons
carrot_img = "https://cdn-icons-png.flaticon.com/512/415/415733.png"      # carrot
broccoli_img = "https://cdn-icons-png.flaticon.com/512/415/415735.png"    # broccoli
rice_img = "https://cdn-icons-png.flaticon.com/512/135/135663.png"        # rice grain icon
leafy_greens_img = "https://cdn-icons-png.flaticon.com/512/414/414738.png" # leafy greens icon
veggies_banner = "https://cdn-icons-png.flaticon.com/512/135/135619.png"  # Veggie basket icon

st.set_page_config(page_title="Vegan Carbon Impact Calculator", layout="centered", page_icon=veggies_banner)

# Banner and title section
st.image(veggies_banner, width=100)
st.markdown("<h1 style='color:#2d6a4f; font-family:verdana; font-weight:bold;'>Vegan Carbon Emissions & Climate Impact Calculator</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border:1px solid #95d5b2;'>", unsafe_allow_html=True)

# Two-column layout
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
    
    # Emissions Reduced: carrot icon - vegetable (healthy food)
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
            <img src="{carrot_img}" width="70" style="margin-right:20px;"/>
            <div>
                <div style="font-weight:700; color:#40916c; font-size:18px;">Estimated Emissions Reduced</div>
                <div style="font-size:28px; color:#2f855a;">{emissions_saved:.2f} GT CO2e/year</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Added Years Until Threshold: rice grain icon - healthy grain 
    st.markdown(
        f"""
        <div style="
            background-color:#d8f3dc;
            border-radius:15px;
            display:flex;
            align-items:center;
            padding:20px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        ">
            <img src="{rice_img}" width="70" style="margin-right:20px;"/>
            <div>
                <div style="font-weight:700; color:#40916c; font-size:18px;">Added Years Until 1.5°C Threshold</div>
                <div style="font-size:28px; color:#2f855a;">{added_years_1_5:.1f} years</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<hr style='border:1px solid #95d5b2;'>", unsafe_allow_html=True)

st.markdown(
    """
    <p style='font-family:Verdana; font-size:16px; color:#375a3f;'>
    This calculator estimates how much global greenhouse gas emissions could be reduced by different levels of veganism adoption worldwide.
    Small lifestyle shifts can lead to meaningful climate benefits! 🌱
    </p>
    """,
    unsafe_allow_html=True
)
