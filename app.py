import streamlit as st
import datetime

# Set corporate page canvas settings
st.set_page_config(
    page_title="BhooKavach (भू-कवच) | Sovereign Land Securities",
    page_icon="🛡️",
    layout="centered"
)

# Custom Corporate Emerald CSS Styling
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #FAFAFA !important;
    }
    .top-bar {
        border-bottom: 1px solid #E2E8F0;
        padding-bottom: 15px;
        margin-bottom: 30px;
        text-align: center;
    }
    .brand-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #0F4A28;
        letter-spacing: -0.02em;
        margin: 0;
    }
    .brand-tagline {
        font-size: 0.9rem;
        color: #64748B;
        margin-top: 4px;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .info-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
        border-top: 4px solid #0F4A28;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 🏛️ CORPORATE BRAND TOP NAVIGATION BAR
# ==========================================
st.markdown("""
    <div class="top-bar">
        <h1 class="brand-title">BhooKavach (भू-कवच)</h1>
        <div class="brand-tagline">Sovereign Land Securities & Anti-Fraud Infrastructure</div>
    </div>
""", unsafe_allow_html=True)

# Initialize a basic mock in-memory database to store early access requests
if "waitlist_records" not in st.session_state:
    st.session_state["waitlist_records"] = []

# ==========================================
# 📝 EDITORIAL VALUE PROPOSITION
# ==========================================
st.markdown("""
    <div class="info-card">
        <p style="font-size: 1.05rem; line-height: 1.6; color: #334155; margin: 0;">
            Project BhooKavach is engineered to eliminate real estate information asymmetry and eradicate property title fraud. 
            Our immediate Phase 1 deployment targets <strong>Pillar 1: Core Verification & Legal Firewalls</strong>, 
            utilizing advanced natural language processing (NLP) to audit historical 30-year link-deed lineages, 
            cross-check active Power of Attorney (PoA) channels, and isolate counterfeit developer website scams 
            before consumer capital is irreversibly committed.
        </p>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# 🔐 THE STEALTH WAITING LIST GATEWAY
# ==========================================
st.markdown("### 🔐 Request Secure Vault Access Allocation")
st.write("Our operational verification sandboxes are currently locked. Request early access below based on your ecosystem profile role.")

with st.form("stealth_waitlist_form", clear_on_submit=True):
    user_role = st.selectbox(
        "Select Account Category Identity:", 
        ["Property Buyer / Landowner", "Registered Ecosystem Vendor (Fencing/Insurance)", "Enterprise API Partner (Banks/Lenders)"]
    )
    user_name = st.text_input("Full Legal Name / Entity Designation:")
    user_email = st.text_input("Secure Corporate Email Address:")
    target_location = st.text_input("Primary Tracking Market Area (e.g., Gachibowli, Shadnagar, Amaravati):")
    
    st.markdown("<br>", unsafe_allow_html=True)
    submit_request = st.form_submit_button("REQUEST SECURED ACCESS ALLOCATION", use_container_width=True)
    
    if submit_request:
        if not user_name or not user_email or not target_location:
            st.error("❌ Authorization Error: Complete configuration fields are required.")
        else:
            new_entry = {
                "Timestamp": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "Name": user_name,
                "Email": user_email,
                "Role": user_role,
                "Market": target_location
            }
            st.session_state["waitlist_records"].append(new_entry)
            st.success("🟢 Access Token Reserved! Your account routing priority is queued. Our technical team will review your profile credentials.")

# ==========================================
# 🔒 LEGAL PROTECTION SHIELD FOOTER
# ==========================================
st.markdown("<br><br>---", unsafe_allow_html=True)
st.markdown("""
    <div style='background-color: #FFF3CD; padding: 15px; border-left: 6px solid #FFC107; border-radius: 4px;'>
        <h4 style='color: #856404; margin-top: 0; font-size:0.9rem; font-weight:700;'>⚠️ Global Launch Operational Terms & Liability Protection Shield</h4>
        <p style='color: #856404; font-size: 0.8rem; line-height: 1.4; margin-bottom: 0;'>
            <strong>Information Aggregator Disclaimer:</strong> BhooKavach operates strictly as an autonomous centralized civic data aggregation network. This application does not produce certified legal opinions, formal title insurance policies, or official property brokerage counsel. All data layers, metrics, and spatial calculations remain confidential under the core founder equity framework agreement (2026).
        </p>
    </div>
""", unsafe_allow_html=True)
