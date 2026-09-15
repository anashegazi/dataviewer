import streamlit as st
import pandas as pd

st.set_page_config(page_title="عارض البيانات المستخرجة", layout="wide")

# Custom CSS for PDF style
st.markdown('''
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;700;800&family=Tajawal:wght@400;500;700;800&display=swap');
@import url('https://cdn.jsdelivr.net/gh/mokhtarbsaid/rare-arabic-fonts/theyearofhandicrafts/all.min.css');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

body {
    direction: rtl;
    text-align: right;
    font-family: "Tajawal", sans-serif;
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
    font-family: 'theyearofhandicrafts', sans-serif;
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
    font-family: 'Cairo', sans-serif;
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
    font-family: 'Cairo', sans-serif;
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
.social-badge i, .whatsapp-btn i {
    margin-left: 6px;
}

.hero-headline {
    font-family: 'theyearofhandicrafts', sans-serif !important;
    font-size: clamp(34px, 5.2vw, 62px);
    line-height: 1.45;
    margin-bottom: 18px;
    font-weight: 800;
}
.gradient-text {
    background: linear-gradient(135deg, #123C3A, #E2EC6C, #123C3A);
    background-size: 220% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline-block;
    animation: shine 6s linear infinite;
}
@keyframes shine { to { background-position: 220% center; } }

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

.social-badge i, .whatsapp-btn i {
    margin-left: 6px;
}

.hero-headline {
    font-family: 'theyearofhandicrafts', sans-serif !important;
    font-size: clamp(34px, 5.2vw, 62px);
    line-height: 1.45;
    margin-bottom: 18px;
    font-weight: 800;
}
.gradient-text {
    background: linear-gradient(135deg, #123C3A, #E2EC6C, #123C3A);
    background-size: 220% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline-block;
    animation: shine 6s linear infinite;
}
@keyframes shine { to { background-position: 220% center; } }
.gallery-container {
    display: flex;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    scroll-behavior: smooth;
    gap: 30px;
    padding-bottom: 20px;
}
.gallery-arrow {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(255,255,255,0.15);
    color: white;
    width: 45px;
    height: 45px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    text-decoration: none !important;
    font-size: 22px;
    transition: all 0.3s;
    z-index: 10;
    backdrop-filter: blur(5px);
}
.gallery-arrow:hover {
    background: #E2EC6C;
    color: #123C3A;
}
.arrow-left { left: -15px; }
.arrow-right { right: -15px; }
.gallery-container .report-card {
    min-width: 90%;
    scroll-snap-align: center;
    flex-shrink: 0;
}
.gallery-container::-webkit-scrollbar {
    height: 12px;
}
.gallery-container::-webkit-scrollbar-thumb {
    background: #123C3A;
    border-radius: 6px;
}
.stRadio > label {
    font-family: 'Cairo', sans-serif !important;
    font-weight: bold;
}
</style>
'''
, unsafe_allow_html=True)

st.markdown('<div style="text-align: center;"><div class="hero-headline gradient-text">عارض البيانات المستخرجة</div></div>', unsafe_allow_html=True)
st.markdown("قم برفع ملف الإكسيل المستخرج من أداة السكرابر لعرضه بتصميم تفاعلي.")

uploaded_file = st.file_uploader("ارفع ملف الإكسيل أو الـ CSV هنا", type=["xlsx", "csv"])

if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        try:
            df = pd.read_csv(uploaded_file, encoding='utf-8-sig')
        except UnicodeDecodeError:
            uploaded_file.seek(0)
            df = pd.read_csv(uploaded_file, encoding='windows-1256')
    else:
        df = pd.read_excel(uploaded_file)
        
    df.columns = df.columns.str.strip().str.replace('﻿', '')
    df = df.astype(str).replace('nan', '')
    df = df.replace('nan.0', '') # in case floats became strings like nan.0
    
    view_mode = st.radio("طريقة العرض:", ["قائمة عمودية", "معرض أفقي (سحب)"], horizontal=True)
    
    st.markdown(f"### تم العثور على {len(df)} متجر")
    
    all_cards_html = ""
    for idx, row in df.iterrows():
        domain = row.get('رابط الموقع', row.get('الموقع (Domain)', ''))
        name = row.get('اسم المتجر', row.get('عنوان المتجر', domain))
        platform = row.get('منصة المتجر', '')
        visits = row.get('الزيارات الشهرية التقريبية', row.get('الزيارات الشهرية التقديرية', row.get('الزيارات', '0')))
        revenue = row.get('العائد الشهري التقريبي (SAR)', row.get('العائد الشهري التقديري (SAR)', row.get('العائد', '')))
        phones = row.get('أرقام التواصل', '')
        whatsapp = row.get('رابط الواتساب', '')
        emails = row.get('رسائل البريد الإلكتروني', row.get('البريد الإلكتروني', ''))
        
        # Socials
        icon_map = {
            'فيسبوك': 'fab fa-facebook',
            'انستجرام': 'fab fa-instagram',
            'تيك توك': 'fab fa-tiktok',
            'تويتر / X': 'fa-brands fa-x-twitter',
            'سناب شات': 'fab fa-snapchat',
            'يوتيوب': 'fab fa-youtube',
            'لينكدإن': 'fab fa-linkedin'
        }
        social_html = ""
        for net in ['فيسبوك', 'انستجرام', 'تيك توك', 'تويتر / X', 'سناب شات', 'يوتيوب', 'لينكدإن']:
            links = row.get(net, '')
            if links and str(links) != 'nan':
                first_link = str(links).split(' | ')[0]
                icon = icon_map.get(net, '')
                social_html += f'<a href="{first_link}" target="_blank" class="social-badge"><i class="{icon}"></i> {net}</a>'
                
        wa_btn = ""
        if whatsapp and str(whatsapp) != 'nan':
            wa_link = str(whatsapp).split(' | ')[0]
            wa_btn = f'<a href="{wa_link}" target="_blank" class="whatsapp-btn"><i class="fab fa-whatsapp" style="font-size: 16px;"></i> تواصل واتساب</a>'
            
        phones_val = phones if phones else 'لا يوجد'
        emails_val = emails if emails else 'لا يوجد'
        social_val = social_html if social_html else '<span style="color:#999;">لا يوجد</span>'
        
        nav_arrows = ""
        if "معرض" in view_mode:
            next_idx = idx + 1 if idx < len(df) - 1 else 0
            prev_idx = idx - 1 if idx > 0 else len(df) - 1
            nav_arrows = f"""
            <a href="#card-{next_idx}" class="gallery-arrow arrow-left" title="التالي"><i class="fas fa-chevron-left"></i></a>
            <a href="#card-{prev_idx}" class="gallery-arrow arrow-right" title="السابق"><i class="fas fa-chevron-right"></i></a>
            """
            
        html = f"""
<div id="card-{idx}" class="report-card">
    {nav_arrows}
    <div class="report-header">
        <div class="company-info">
            <h2>{name if name else domain}</h2>
            <p>{domain} • {platform}</p>
        </div>
        <div class="visits-box">
            <div class="visits-label">الزيارات الشهرية المتوقعة</div>
            <div class="visits-number">{visits}</div>
            <div class="visits-label" style="font-size:14px; color:#A3B8B6;">العائد المتوقع: {revenue}</div>
        </div>
    </div>
    
    <div class="details-section">
        <div class="detail-item">
            <div class="detail-title">أرقام التواصل</div>
            <div class="detail-value" dir="ltr" style="text-align: right;">{phones_val}</div>
            {wa_btn}
        </div>
        <div class="detail-item">
            <div class="detail-title">البريد الإلكتروني</div>
            <div class="detail-value">{emails_val}</div>
        </div>
        <div class="detail-item">
            <div class="detail-title">الشبكات الاجتماعية</div>
            <div class="social-links">
                {social_val}
            </div>
        </div>
    </div>
</div>
"""
        all_cards_html += html.replace('\n', '')

    if "معرض" in view_mode:
        st.markdown(f'<div class="gallery-container">{all_cards_html}</div>', unsafe_allow_html=True)
    else:
        st.markdown(all_cards_html, unsafe_allow_html=True)