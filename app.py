import streamlit as st
import streamlit.components.v1 as components

# --- 1. PREMIUM BRANDING & CSS ---
st.set_page_config(page_title="Orosun Health", page_icon="🏥", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    
    .stApp { background-color: #FFFFFF; font-family: 'Inter', sans-serif; }
    
    /* Global Styles */
    h1, h2, h3 { color: #111111; font-weight: 800 !important; }
    p { color: #444444; line-height: 1.6; }

    /* Ro-style Header */
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 0;
        border-bottom: 1px solid #F0F0F0;
        margin-bottom: 40px;
    }
    
    /* Service Cards */
    .service-card {
        padding: 40px;
        border: 1px solid #F0F0F0;
        border-radius: 20px;
        background-color: #FFFFFF;
        text-align: center;
        transition: all 0.3s ease;
    }
    .service-card:hover {
        border-color: #002868;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    }
    
    /* Bio Section */
    .bio-container {
        background-color: #F9F9F9;
        padding: 60px;
        border-radius: 30px;
        margin-top: 80px;
    }
    
    /* Custom Buttons */
    .stButton>button {
        border-radius: 50px;
        padding: 12px 30px;
        background-color: #111111;
        color: white;
        border: none;
        font-weight: 600;
        width: 100%;
        height: 3.5em;
    }
    .stButton>button:hover { background-color: #333333; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. HEADER & LOGO ---
# Replace LOGO_URL with the actual URL of your uploaded Orosun logo
LOGO_URL = "https://placehold.co/200x50/white/002868?text=OROSUN+HEALTH"

st.markdown(f"""
    <div class="header-container">
        <img src="{LOGO_URL}" width="180">
        <div style="font-weight: 600; color: #666;">Modern Care. American Excellence.</div>
    </div>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("Orosun Admin")
    view = st.radio("Navigation", ["Patient Portal", "Doctor Dashboard"])
    st.divider()
    st.success("Sovereign EMR: Online")

if view == "Patient Portal":
    # --- HERO SECTION ---
    st.markdown("<h1 style='text-align: center; font-size: 3.5rem;'>The healthcare you deserve.</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #666;'>Expert diagnostic and interventional care, delivered virtually.</p>", unsafe_allow_html=True)
    st.write("##")

    # --- SERVICES GRID ---
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="service-card"><h3>Weight Loss</h3><p>GLP-1 programs managed by expert clinicians.</p></div>', unsafe_allow_html=True)
        if st.button("Get Started", key="wl"): st.session_state.path = "Weight Loss"
        
    with col2:
        st.markdown('<div class="service-card"><h3>Radiology</h3><p>Expert second opinions on your imaging scans.</p></div>', unsafe_allow_html=True)
        if st.button("Consult Now", key="rad"): st.session_state.path = "Radiology"
        
    with col3:
        st.markdown('<div class="service-card"><h3>Wellness</h3><p>Hormone optimization and longevity protocols.</p></div>', unsafe_allow_html=True)
        if st.button("Explore", key="hrt"): st.session_state.path = "Wellness"

    if 'path' in st.session_state:
        st.divider()
        st.subheader(f"Start your {st.session_state.path} Consultation")
        name = st.text_input("Full Patient Name")
        history = st.text_area("Tell us about your medical goals...")
        if st.button("Submit & Proceed to Checkout"):
            st.info("Securing clinical record... Opening payment.")
            # Your Stripe Pricing Table
            components.html('<script async src="https://js.stripe.com/v3/pricing-table.js"></script><stripe-pricing-table pricing-table-id="prctbl_1SvBvdAwzTkFdWZ3nkZccoTf" publishable-key="pk_live_51SpJwRAwzTkFdWZ3n9aOWy8NnXX8tv1IVKAuZ7CCuQXQNLUOXRSH8gk8IarM5AOdgaoHQGZAmUjWhINKsJfjJf9U00z5ZusTia"></stripe-pricing-table>', height=600)

    # --- 4. ABOUT ME (RO-STYLE BIO) ---
    # Replace PHOTO_URL with the URL of your uploaded AI headshot
    PHOTO_URL = "https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?auto=format&fit=crop&q=80&w=600"

    st.markdown(f"""
        <div class="bio-container">
            <div style="display: flex; align-items: center; gap: 50px; flex-wrap: wrap;">
                <div style="flex: 1; min-width: 300px;">
                    <img src="{PHOTO_URL}" style="width: 100%; border-radius: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
                </div>
                <div style="flex: 2; min-width: 350px;">
                    <h2 style="margin-top: 0;">Olalesi Osunsade, MD, DABR®</h2>
                    <p style="color: #002868; font-weight: 600; letter-spacing: 1px; text-transform: uppercase;">Dual Board-Certified Radiologist</p>
                    <p>Dr. Osunsade graduated from <b>George Washington University School of Medicine</b> in 2012. 
                    Born in Washington, D.C. and raised internationally across the Philippines, Tanzania, Kenya, and Nigeria, 
                    he brings a unique global perspective to precision diagnostics. With fellowship training in Vascular 
                    and Interventional Radiology, "Dr. O" founded Orosun Health to merge elite clinical expertise with 
                    modern telehealth accessibility.</p>
                    <p><b>Expertise & Credentials:</b><br>
                    • ABR Certified: Interventional & Diagnostic Radiology<br>
                    • Licensed in: MI, MD, TX, FL, CA, DC, OH, WI, NY<br>
                    • NPI: 1568720266</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

else:
    # --- 5. DOCTOR DASHBOARD ---
    st.title("👨‍⚕️ Orosun Worklist")
    st.info("Securely connected to Google Cloud FHIR Store: emr_records")
    
    st.write("### Patient Queue")
    with st.container(border=True):
        colA, colB = st.columns([3, 1])
        with colA:
            st.write("**Patient:** Test Patient")
            st.caption("Status: Paid - Awaiting Review")
        with colB:
            st.link_button("🎥 Launch OHIF PACS", "https://ohif-viewer-894403495720.us-central1.run.app")
