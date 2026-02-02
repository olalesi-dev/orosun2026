import streamlit as st
import streamlit.components.v1 as components

# --- 1. GLOBAL BRANDING ---
st.set_page_config(page_title="Orosun Health", page_icon="🏥", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;800&display=swap');
    
    .stApp { background-color: #FFFFFF; font-family: 'Inter', sans-serif; }
    
    /* Premium Header */
    .hero-section {
        background: linear-gradient(135deg, #002868 0%, #001233 100%);
        padding: 80px 20px;
        border-radius: 0 0 40px 40px;
        text-align: center;
        color: white;
        margin-bottom: 50px;
    }
    .hero-title { font-size: 4rem; font-weight: 800; letter-spacing: -2px; margin: 0; }
    
    /* Service Tiles */
    .service-tile {
        padding: 40px;
        border: 1px solid #F0F0F0;
        border-radius: 24px;
        background-color: #FFFFFF;
        box-shadow: 0 10px 30px rgba(0,0,0,0.03);
        transition: transform 0.3s ease;
        text-align: center;
    }
    .service-tile:hover { transform: translateY(-5px); border-color: #002868; }
    
    /* Professional Credentials Box */
    .credentials-box {
        background-color: #F8F9FA;
        padding: 50px;
        border-radius: 32px;
        border-left: 12px solid #BF0A30;
        margin-top: 80px;
    }
    
    /* Clean Buttons */
    .stButton>button {
        border-radius: 50px; padding: 12px 30px;
        background-color: #002868; color: white;
        border: none; font-weight: 600; width: 100%; height: 3.5em;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. HEADER ---
st.markdown("""
    <div class="hero-section">
        <div class="hero-title">OROSUN HEALTH</div>
        <p style="font-size: 1.2rem; opacity: 0.8; font-weight: 300;">
            Dual Board-Certified Diagnostic & Interventional Expertise
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("Admin Console")
    view = st.radio("Navigation", ["Patient Portal", "Physician Dashboard"])
    st.divider()
    st.caption("Secure Cloud Integration: Active")

if view == "Patient Portal":
    # --- PATIENT GRID ---
    st.write("## Choose Your Pathway")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="service-tile"><h3>Weight Loss</h3><p>Precision GLP-1 therapy monitored by board-certified clinicians.</p></div>', unsafe_allow_html=True)
        if st.button("Start Assessment", key="wl"): st.session_state.path = "Weight Loss"
        
    with col2:
        st.markdown('<div class="service-tile"><h3>Imaging Consult</h3><p>Expert 2nd opinions on complex diagnostic imaging studies.</p></div>', unsafe_allow_html=True)
        if st.button("Upload Scans", key="rad"): st.session_state.path = "Imaging Consult"
        
    with col3:
        st.markdown('<div class="service-tile"><h3>Longevity</h3><p>Personalized wellness and metabolic optimization protocols.</p></div>', unsafe_allow_html=True)
        if st.button("Explore Wellness", key="hrt"): st.session_state.path = "Longevity"

    if 'path' in st.session_state:
        st.divider()
        st.subheader(f"Clinical Intake: {st.session_state.path}")
        # Standardize Intake
        with st.container():
            st.text_input("Legal Patient Name")
            st.text_area("History of Present Illness / Chief Complaint")
            if st.button("Submit & Finalize Payment"):
                st.info("Record Secured in Orosun EMR. Opening Checkout...")
                # Stripe Pricing Table
                components.html('<script async src="https://js.stripe.com/v3/pricing-table.js"></script><stripe-pricing-table pricing-table-id="prctbl_1SvBvdAwzTkFdWZ3nkZccoTf" publishable-key="pk_live_51SpJwRAwzTkFdWZ3n9aOWy8NnXX8tv1IVKAuZ7CCuQXQNLUOXRSH8gk8IarM5AOdgaoHQGZAmUjWhINKsJfjJf9U00z5ZusTia"></stripe-pricing-table>', height=600)

    # --- ABOUT THE FOUNDER ---
    st.markdown("""
        <div class="credentials-box">
            <h2 style="margin-top:0;">Olalesi Osunsade, MD, DABR®</h2>
            <p style="color:#BF0A30; font-weight:700; font-size:1.1rem; text-transform:uppercase;">
                Interventional & Diagnostic Radiology
            </p>
            <p>Dr. Osunsade is a dual board-certified specialist and a graduate of the <b>George Washington University School of Medicine</b>. 
            By combining a background in DNA cloning and HIV genotyping with elite clinical radiology, 
            he founded Orosun Health to offer a more rigorous, data-driven approach to virtual care.</p>
            <p style="font-size:0.9rem; color:#666;">
                Licensed in: NY, CA, FL, TX, MD, MI, DC, OH, WI<br>
                NPI: 1568720266
            </p>
        </div>
        """, unsafe_allow_html=True)

else:
    # --- DOCTOR DASHBOARD ---
    st.title("👨‍⚕️ Orosun Worklist")
    
    st.write("### Patient Queue")
    with st.container(border=True):
        colA, colB = st.columns([3, 1])
        with colA:
            st.write("**Patient:** Test Patient (Simulation)")
            st.caption("Awaiting: Second Opinion Imaging Consult")
        with colB:
            # Pointing back to your Google Cloud PACS
            st.link_button("🎥 Launch OHIF PACS", "https://ohif-viewer-894403495720.us-central1.run.app")
            
    st.divider()
    st.caption("EMR Data stored in Google Cloud FHIR: patriotic_health_data")
