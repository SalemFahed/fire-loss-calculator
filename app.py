# Version 1.0 - Fire Loss Estimator (Multi-Site Selector)
# Using Streamlit - basic version with site selection and dynamic item input

import streamlit as st

st.set_page_config(page_title="حاسبة الخسائر الفنية", layout="centered")

st.title("🔥 حاسبة الخسائر الفنية")
st.markdown("ابدأ باختيار نوع الموقع، ثم أدخل تفاصيل القطع لتقدير الخسائر.")

# اختيار نوع الموقع
site_type = st.selectbox("📍 نوع الموقع:", ["اختر", "منزل", "مركبة", "محل تجاري"])

# قائمة القطع بناء على نوع الموقع
items_by_site = {
    "منزل": ["كنب ثلاثي", "كنب ثنائي", "كنب فردي", "مكيف سبليت", "مكيف شباك", "شاشة", "دولاب", "فرشة", "دلة", "إبريق", "ثلاجة", "غسالة", "جوال", "لابتوب", "بوية"],
    "مركبة": ["مقاعد", "شاشة سيارة", "بطارية", "إطارات", "أغراض شخصية"],
    "محل تجاري": ["رف عرض", "كاشير", "كاميرا مراقبة", "ديكور", "بضاعة"]
}

if site_type != "اختر":
    st.header("🧾 تفاصيل القطع:")
    total_loss = 0
    selected_items = items_by_site.get(site_type, [])

    for item in selected_items:
        with st.expander(f"🛠️ {item}"):
            quantity = st.number_input(f"عدد {item}:", min_value=0, step=1, key=f"{item}_qty")
            price = st.number_input(f"سعر {item} (ريال):", min_value=0.0, step=10.0, key=f"{item}_price")
            item_loss = quantity * price
            total_loss += item_loss
            if quantity > 0:
                st.success(f"خسارة {item}: {item_loss:,.2f} ريال")

    st.subheader("💰 الإجمالي:")
    st.success(f"إجمالي الخسائر التقريبي: {total_loss:,.2f} ريال")
