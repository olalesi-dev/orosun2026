import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Orosun Health", page_icon="🏥", layout="wide")

# Ro-style High-End CSS
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; font-family: 'Inter', sans-serif; }
    .hero { 
        background: linear-gradient(135deg, #002868 0%, #001233 100%);
        padding: 60px; border-radius: 0 0 30px 30px; text-align: center; color: white; 
    }
    .hero h1 { font-size: 3.5rem; font-weight: 800; margin: 0; letter-spacing: -2px; }
    .card { padding: 30px; border: 1px solid #F0F0F0; border-radius: 24px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
    .stButton>button { border-radius: 50px; background-color: #002868; color: white; width: 100%; height: 3.5em; font-weight: 600; border: none; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="hero"><h1>OROSUN HEALTH</h1><p>Modern Telehealth • Elite Radiology • Precision Longevity</p></div>', unsafe_allow_html=True)

st.write("##")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="card"><h3>Weight Loss</h3><p>GLP-1 Programs</p></div>', unsafe_allow_html=True)
    if st.button("Select Weight Loss"): st.session_state.path = "Weight Loss"
with col2:
    st.markdown('<div class="card"><h3>Radiology</h3><p>2nd Opinions</p></div>', unsafe_allow_html=True)
    if st.button("Select Radiology"): st.session_state.path = "Radiology"
with col3:
    st.markdown('<div class="card"><h3>Wellness</h3><p>Longevity</p></div>', unsafe_allow_html=True)
    if st.button("Select Wellness"): st.session_state.path = "Wellness"

if 'path' in st.session_state:
    st.divider()
    st.subheader(f"Intake: {st.session_state.path}")
    st.text_input("Full Name")
    st.text_area("Clinical History")
    if st.button("Proceed to Payment"):
        components.html('<script async src="https://js.stripe.com/v3/pricing-table.js"></script><stripe-pricing-table pricing-table-id="prctbl_1SvBvdAwzTkFdWZ3nkZccoTf" publishable-key="pk_live_51SpJwRAwzTkFdWZ3n9aOWy8NnXX8tv1IVKAuZ7CCuQXQNLUOXRSH8gk8IarM5AOdgaoHQGZAmUjWhINKsJfjJf9U00z5ZusTia"></stripe-pricing-table>', height=600)

st.markdown('<div style="background:#F8F9FA; padding:50px; border-radius:24px; border-left:10px solid #BF0A30; margin-top:50px;"><h2>Olalesi Osunsade, MD, DABR®</h2><p><b>Dual Board-Certified Radiologist</b></p><p>Founder of Orosun Health. Graduate of GWU Medical School. Licensed: NY, CA, FL, TX, MD, MI, DC, OH, WI.</p></div>', unsafe_allow_html=True)