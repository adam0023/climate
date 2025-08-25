import streamlit as st

st.title("Carbon Emissions Reduction & Climate Impact Calculator for Global Veganism")

# Input slider for veganism adoption %
percent_vegan = st.slider("Percentage of Global Population Converting to Veganism", 0, 100, 0)

# Constants
total_animal_ag_emissions = 7.3  # gigatons CO2e per year (14.5% global emissions)
carbon_budget_1_5C = 130  # Approximate remaining carbon budget in gigatons CO2 for 1.5°C

# Calculate emissions reduction
emissions_saved = total_animal_ag_emissions * (percent_vegan / 100)

# Calculate added years to carbon budget for 1.5°C
if total_animal_ag_emissions > 0:
    added_years_1_5 = carbon_budget_1_5C / total_animal_ag_emissions * (percent_vegan / 100)
else:
    added_years_1_5 = 0

# Display results
st.write(f"At {percent_vegan}% veganism adoption, estimated global carbon emissions reduction is:")
st.write(f"**{emissions_saved:.2f} gigatons of CO2 equivalent per year**")

st.write(f"Estimated additional time gained before reaching the 1.5°C warming threshold:")
st.write(f"**{added_years_1_5:.1f} years** (theoretical estimate based on carbon budget)")

st.markdown("""
---
Animal agriculture accounts for approximately 14.5% of global greenhouse gas emissions, or about 7.3 gigatons CO2e annually.  
The remaining carbon budget for 1.5°C warming is around 130 gigatons CO2.  
This calculator estimates proportional emissions savings and added time to the climate threshold based on global veganism adoption.  
Note: This is a simplified estimate ignoring feedback loops and other greenhouse gases.
""")