ma_phien = input("nhap ma phien:")
ma_may = input("nhap ma may:")
cong_suat = float(input("nhap cong suat:"))
so_phut = int(input("nhap so phut:"))
don_gia = float(input("nhap don gia:"))

dien_nang = cong_suat * so_phut / 60 / 1000
chi_phi = dien_nang * don_gia
print (f"ma phien: {ma_phien}")
print (f"ma may: {ma_may}")
print (f"dien nang tieu thu: {dien_nang} kWh")
print (f"chi phi dien: {chi_phi} VND")