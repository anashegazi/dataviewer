import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Viewer", layout="wide")

# Custom CSS for PDF style
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap');

body {
    direction: rtl;
    text-align: right;
    font-family: 'Tajawal', sans-serif;
    background-color: #F8F9FA;
}
.stApp {
    background-color: #F8F9FA;
}

.report-card {
    background-color: #123C3A;
    border-radius: 12px;
    padding: 30px;
    margin-bottom: 30px;
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    color: white;
    position: relative;
    overflow: hidden;
    animation: fadeIn 0.8s ease-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.report-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255,255,255,0.1);
    padding-bottom: 20px;
    margin-bottom: 20px;
}

.company-info h2 {
    font-size: 32px;
    font-weight: 800;
    margin: 0 0 10px 0;
    color: white;
}

.company-info p {
    font-size: 18px;
    color: #A3B8B6;
    margin: 0;
}

.visits-box {
    text-align: left;
    border-right: 2px solid rgba(255,255,255,0.1);
    padding-right: 30px;
}

.visits-number {
    font-size: 64px;
    font-weight: 800;
    color: #E2EC6C;
    line-height: 1;
    margin-bottom: 5px;
}

.visits-label {
    font-size: 18px;
    color: white;
    font-weight: 500;
}

.details-section {
    background-color: white;
    border-radius: 8px;
    padding: 20px;
    color: #123C3A;
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}

.detail-item {
    flex: 1;
    min-width: 200px;
}

.detail-title {
    font-size: 14px;
    color: #6C757D;
    margin-bottom: 5px;
    font-weight: 700;
}

.detail-value {
    font-size: 16px;
    font-weight: 500;
}

.social-links {
    display: flex;
    gap: 10px;
    margin-top: 10px;
    flex-wrap: wrap;
}

.social-badge {
    background-color: #F1F3F5;
    color: #123C3A;
    padding: 5px 12px;
    border-radius: 20px;
    font-size: 14px;
    font-weight: 500;
    text-decoration: none;
    transition: all 0.2s;
}

.social-badge:hover {
    background-color: #E2EC6C;
    color: #123C3A;
}

.whatsapp-btn {
    background-color: #25D366;
    color: white;
    padding: 8px 16px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 700;
    display: inline-block;
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)

st.title("?? ???? ??????? ?????? ???????")
st.markdown("?? ???? ??? ??????? ???????? ?? ???? ???????? ????? ?????? ??????.")

uploaded_file = st.file_uploader("???? ??? ??????? ???", type=["xlsx", "csv"])

if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        try:
            df = pd.read_csv(uploaded_file, encoding='utf-8-sig')
        except UnicodeDecodeError:
            uploaded_file.seek(0)
            df = pd.read_csv(uploaded_file, encoding='windows-1256')
    else:
        df = pd.read_excel(uploaded_file)
        
    df.fillna('', inplace=True)
    
    st.markdown(f"### ?? ?????? ??? {len(df)} ????")
    
    for idx, row in df.iterrows():
        domain = row.get('???? ??????', '')
        name = row.get('??? ??????', domain)
        platform = row.get('???? ??????', '')
        visits = row.get('???????? ??????? ?????????', '0')
        revenue = row.get('?????? ?????? ???????? (SAR)', '')
        phones = row.get('????? ???????', '')
        whatsapp = row.get('???? ????????', '')
        emails = row.get('????? ?????? ??????????', '')
        
        # Socials
        social_html = ""
        for net in ['??????', '????????', '??? ???', '????? / X', '???? ???', '??????', '???????']:
            links = row.get(net, '')
            if links:
                first_link = links.split(' | ')[0]
                social_html += f'<a href="{first_link}" target="_blank" class="social-badge">{net}</a>'
                
        # HTML Structure
        html = f"""
        <div class="report-card">
            <div class="report-header">
                <div class="company-info">
                    <h2>{name if name else domain}</h2>
                    <p>{domain} • {platform}</p>
                </div>
                <div class="visits-box">
                    <div class="visits-label">???????? ??????? ????????</div>
                    <div class="visits-number">{visits}</div>
                    <div class="visits-label" style="font-size:14px; color:#A3B8B6;">?????? ???????: {revenue}</div>
                </div>
            </div>
            
            <div class="details-section">
                <div class="detail-item">
                    <div class="detail-title">????? ???????</div>
                    <div class="detail-value" dir="ltr" style="text-align: right;">{phones if phones else '?? ????'}</div>
        """
        
        if whatsapp:
            wa_link = whatsapp.split(' | ')[0]
            html += f'<a href="{wa_link}" target="_blank" class="whatsapp-btn">?? ????? ??????</a>'
            
        html += f"""
                </div>
                <div class="detail-item">
                    <div class="detail-title">?????? ??????????</div>
                    <div class="detail-value">{emails if emails else '?? ????'}</div>
                </div>
                <div class="detail-item">
                    <div class="detail-title">??????? ??????????</div>
                    <div class="social-links">
                        {social_html if social_html else '<span style="color:#999;">?? ????</span>'}
                    </div>
                </div>
            </div>
        </div>
        """
        
        st.markdown(html, unsafe_allow_html=True)
