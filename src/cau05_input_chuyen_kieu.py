ma_may = input("nhap ma may:")
cong_suat = input("nhap cong suat:")
so_phut = input("nhap so phut:")
don_gia = input("nhap don gia:")
print (type(ma_may))
print (type(cong_suat))
print (type(so_phut))
print (type(don_gia))
cong_suat = float(cong_suat)
so_phut = int(so_phut)
don_gia = float(don_gia)

dien_nang = cong_suat * so_phut / 60 / 1000
chi_phi = dien_nang * don_gia
print (f"dien nang tieu thu: {dien_nang} kWh")
print (f"chi phi dien: {chi_phi} VND")