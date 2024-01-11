import streamlit as st
import requests

st.title("Unified Categories Generator")

catalogue_ete = st.text_area("Catalogue Été")
catalogue_enfants = st.text_area("Catalogue Enfants")
catalogue_noel = st.text_area("Catalogue Noël")

if st.button("Generate Unified Categories"):
    data = {
        "catalogue_ete": catalogue_ete,
        "catalogue_enfants": catalogue_enfants,
        "catalogue_noel": catalogue_noel,
    }

    url = "http://127.0.0.1:5000/"
    response = requests.post(url, json=data)

    if response.status_code == 200:
        unified_categories = response.json().get("unified_categories")
        st.write("Unified Categories:")
        st.write(unified_categories)
    else:
        st.error("Failed to get response from the API")
