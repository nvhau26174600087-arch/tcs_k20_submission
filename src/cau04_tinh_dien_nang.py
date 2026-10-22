cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
#dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
#chi_phi = dien_nang_kwh * don_gia_kwh
print (f"dien nang tieu thu: {dien_nang_kwh} kWh")
print (f"chi phi dien: {chi_phi} VND")

so_phut = 60

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
#dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
#chi_phi = dien_nang_kwh * don_gia_kwh
print (f"dien nang tieu thu: {dien_nang_kwh} kWh")
print (f"chi phi dien: {chi_phi} VND")