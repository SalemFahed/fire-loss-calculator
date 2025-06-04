import streamlit as st

st.set_page_config(page_title="حاسبة الخسائر", layout="centered")

st.title("🔥 حاسبة تقدير الخسائر من الحريق")
st.markdown("احسب عدد القطع المحترقة وقيمة الخسارة.")

site_length = st.number_input("طول الموقع (م)", min_value=0.0)
site_width = st.number_input("عرض الموقع (م)", min_value=0.0)

item_length = st.number_input("طول القطعة (م)", min_value=0.0)
item_width = st.number_input("عرض القطعة (م)", min_value=0.0)
item_price = st.number_input("سعر القطعة (ريال)", min_value=0.0)

if st.button("احسب"):
    site_area = site_length * site_width
    item_area = item_length * item_width

    if item_area > 0:
        count = int(site_area // item_area)
        loss = count * item_price
        st.success(f"العدد التقريبي: {count} قطعة")
        st.success(f"الخسارة الكلية: {loss:,.2f} ريال")
    else:
        st.error("❌ تأكد من أبعاد القطعة.")
