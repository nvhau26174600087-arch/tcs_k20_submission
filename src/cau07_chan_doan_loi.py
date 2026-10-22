ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))
so_phut = int(input("Nhập số phút: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")

# chay thu lan 1
# ten tep: src/cau07_chan_doan_loi.py
# so dong: 6
# loai loi: SyntaxError
# thong bao loi: '(' was never closed

# chay thu lan 2
# ten tep: src/cau07_chan_doan_loi.py
# so dong: 4
# loai loi: TypeError
# thong bao loi: unsupported operand type(s) for /: 'str' and 'int'

# chay thu lan 3
# ten tep: src/cau07_chan_doan_loi.py
# so dong 6
# loai loi: NameError
# thong bao loi: name 'dien_nang' is not defined. Did you mean: 'dien_nang_kwh'?