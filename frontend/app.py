import streamlit as st

st.set_page_config(
    page_title="NovaFlow AI",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 NovaFlow AI")
st.subheader("AI Business Automation Platform")

st.success("Project bootstrap completed successfully!")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Documents", "0")

with col2:
    st.metric("AI Calls", "0")

with col3:
    st.metric("Workflows", "0")

st.markdown("---")
st.write("Welcome to NovaFlow AI Enterprise Edition v0.2")