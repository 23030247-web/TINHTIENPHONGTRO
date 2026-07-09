import streamlit as st
import pandas as pd

st.title("🏠 Quản lý tiền phòng trọ (10 phòng)")

# Giá cố định
gia_dien = 3500      # VNĐ/kWh
gia_nuoc = 25000     # VNĐ/m3
gia_wifi = 100000    # VNĐ
gia_rac = 30000      # VNĐ

ket_qua = []

for i in range(1, 11):
    with st.expander(f"📍 Phòng {i}", expanded=False):

        gia_phong = st.number_input(
            f"Tiền phòng {i}",
            min_value=0,
            value=3000000,
            key=f"phong_{i}"
        )

        so_dien = st.number_input(
            f"Số điện tiêu thụ phòng {i} (kWh)",
            min_value=0,
            value=100,
            key=f"dien_{i}"
        )

        so_nuoc = st.number_input(
            f"Số nước tiêu thụ phòng {i} (m³)",
            min_value=0,
            value=10,
            key=f"nuoc_{i}"
        )

        so_nguoi = st.slider(
            f"Số người phòng {i}",
            1,
            6,
            3,
            key=f"nguoi_{i}"
        )

        tien_dien = so_dien * gia_dien
        tien_nuoc = so_nuoc * gia_nuoc

        tong = (
            gia_phong
            + tien_dien
            + tien_nuoc
            + gia_wifi
            + gia_rac
        )

        moi_nguoi = tong / so_nguoi

        st.success(f"💰 Tổng tiền phòng {i}: {tong:,.0f} VNĐ")
        st.info(f"👥 Mỗi người đóng: {moi_nguoi:,.0f} VNĐ")

        tin_nhan = f"""
🏠 THÔNG BÁO PHÒNG {i}

- Tiền phòng: {gia_phong:,.0f}đ
- Điện: {so_dien} kWh = {tien_dien:,.0f}đ
- Nước: {so_nuoc} m³ = {tien_nuoc:,.0f}đ
- Wifi: {gia_wifi:,.0f}đ
- Rác: {gia_rac:,.0f}đ

====================
TỔNG: {tong:,.0f}đ

Mỗi người đóng: {moi_nguoi:,.0f}đ

Các bạn vui lòng chuyển khoản sớm. Xin cảm ơn!
"""

        st.text_area(
            f"Tin nhắn phòng {i}",
            value=tin_nhan,
            height=220,
            key=f"text_{i}"
        )

        ket_qua.append({
            "Phòng": i,
            "Tiền phòng": gia_phong,
            "Điện": tien_dien,
            "Nước": tien_nuoc,
            "Wifi": gia_wifi,
            "Rác": gia_rac,
            "Tổng tiền": tong,
            "Số người": so_nguoi,
            "Mỗi người": moi_nguoi
        })

st.divider()

st.subheader("📋 Bảng tổng hợp 10 phòng")

df = pd.DataFrame(ket_qua)
st.dataframe(df, use_container_width=True)

st.metric("💰 Tổng doanh thu", f"{df['Tổng tiền'].sum():,.0f} VNĐ")
