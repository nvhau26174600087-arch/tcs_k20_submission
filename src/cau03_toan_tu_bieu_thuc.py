#9
tong_phut = 135
so_gio = tong_phut // 60
so_phut_con_lai = tong_phut % 60
print(f"Số giờ: {so_gio}, Số phút còn lại: {so_phut_con_lai}")

#10
su_dung_lau = tong_phut > 60
print(f"Sử dụng lâu: {su_dung_lau}")

#11
cong_suat_w = 250
du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print(f"Dữ liệu hợp lệ: {du_lieu_hop_le}")

#12
bieu_thuc_1 = 100 + 20 * 3
bieu_thuc_2 = (100 + 20) * 3
print(f"Biểu thức 1: {bieu_thuc_1}")
print(f"Biểu thức 2: {bieu_thuc_2}")
# Dự đoán 
# dòng 1: 160
# dòng 2: 360

