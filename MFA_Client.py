import streamlit as st

st.set_page_config(page_title="MFA Client")

st.markdown("# MFA Client")
st.sidebar.header("MFA Client")
st.write(
    """MFA Client is a multi-factor authentication (MFA) client based on Streamlit. 
    This application allows users to enter the MFA keys of multiple accounts, 
    displaying the MFA calculation results of all accounts on one interface.
     Users can also add and delete accounts."""
)

