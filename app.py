# Updated version with basic PDF export using streamlit components (placeholder logic)

import streamlit as st
from io import BytesIO
from fpdf import FPDF

st.set_page_config(page_title="حاسبة الخسائر الفنية", layout="centered")

st.title("🔥 حاسبة الخسائر الفنية")
st.markdown("ابدأ باختيار نوع الموقع، ثم أدخل تفاصيل القطع لتقدير الخسائر.")

site_type = st.selectbox("📍 نوع الموقع:", ["اختر", "منزل", "مركبة", "محل تجاري"])

items_by_site = {
    "منزل": ["كنب ثلاثي", "كنب ثنائي", "كنب فردي", "مكيف سبليت", "مكيف شباك", "شاشة", "دولاب", "فرشة", "دلة", "إبريق", "ثلاجة", "غسالة", "جوال", "لابتوب", "بوية"],
    "مركبة": ["مقاعد", "شاشة سيارة", "بطارية", "إطارات", "أغراض شخصية"],
    "محل تجاري": ["رف عرض", "كاشير", "كاميرا مراقبة", "ديكور", "بضاعة"]
}

losses = []
total_loss = 0

if site_type != "اختر":
    st.header("🧾 تفاصيل القطع:")
    selected_items = items_by_site.get(site_type, [])

    for item in selected_items:
        with st.expander(f"🛠️ {item}"):
            quantity = st.number_input(f"عدد {item}:", min_value=0, step=1, key=f"{item}_qty")
            price = st.number_input(f"سعر {item} (ريال):", min_value=0.0, step=10.0, key=f"{item}_price")
            item_loss = quantity * price
            total_loss += item_loss
            if quantity > 0:
                losses.append((item, quantity, price, item_loss))
                st.success(f"خسارة {item}: {item_loss:,.2f} ريال")

    st.subheader("💰 الإجمالي:")
    st.success(f"إجمالي الخسائر التقريبي: {total_loss:,.2f} ريال")

    # PDF generation
    def generate_pdf():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=14)
        pdf.cell(200, 10, txt="تقرير تقدير الخسائر الفنية", ln=1, align='C')
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"نوع الموقع: {site_type}", ln=1, align='R')

        for item, qty, price, loss in losses:
            pdf.cell(200, 10, txt=f"{item} - العدد: {qty}, السعر: {price} ريال, الخسارة: {loss:,.2f} ريال", ln=1, align='R')

        pdf.ln(5)
        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(200, 10, txt=f"الإجمالي: {total_loss:,.2f} ريال", ln=1, align='R')

        buffer = BytesIO()
        pdf.output(buffer)
        buffer.seek(0)
        return buffer

    if st.button("📄 تحميل تقرير PDF"):
        pdf_file = generate_pdf()
        st.download_button(label="اضغط لتحميل التقرير", data=pdf_file, file_name="تقرير_الخسائر.pdf", mime="application/pdf")
