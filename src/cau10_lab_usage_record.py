ma_phien = input("nhap ma phien")
ma_may = input("nhap ma may")
cong_suat = float(input("nhap cong suat "))
thoi_gian = float(input("nhap thoi gian "))
don_gia = float(input("nhap don gia "))
dien_nang = cong_suat * thoi_gian / 60 / 1000
chi_phi = dien_nang * don_gia
boolean = thoi_gian > 60
from datetime import datetime
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
print (f"ma phien {ma_phien}")
print (f"ma may {ma_may}")
print (f"cong suat {cong_suat}")
print (f"thoi luong {thoi_gian}")
print (f"dien nang {dien_nang}")
print (f"chi phi {chi_phi}")
print (f"tren 60 phut {boolean}")
print (f"ghi nhan luc {thoi_diem_text}")