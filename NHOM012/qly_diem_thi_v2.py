import libs.xu_li_diem_thi

# Nhập tên file danh sách điểm thí sinh
ten_file = input("Nhập tên file danh sách điểm thí sinh: ")

# Mở file và đọc danh sách thí sinh
ds_thi_sinh = xu_ly_diem_thi.mo_file_diem_thi(ten_file)

# In danh sách thí sinh
xu_ly_diem_thi.in_danh_sach_thi_sinh(ds_thi_sinh)

# Thêm thông tin một thí sinh mới
print("Thêm thông tin một thí sinh mới:")
# Nhập các thông tin của thí sinh
ma_thi_sinh = input("Nhập mã thí sinh: ")
ten_thi_sinh = input("Nhập tên thí sinh: ")
khu_vuc = input("Nhập khu vực: ")
diemmon1 = float(input("Nhập điểm môn 1: "))
diemmon2 = float(input("Nhập điểm môn 2: "))
diemmon3 = float(input("Nhập điểm môn 3: "))
# Tính tổng điểm
tong_diem = diemmon1 + diemmon2 + diemmon3
# Tạo một từ điển để lưu trữ thông tin của thí sinh
thi_sinh = {'ma_thi_sinh': ma_thi_sinh, 'ten_thi_sinh': ten_thi_sinh, 'khu_vuc': khu_vuc, 'diemmon1': diemmon1, 'diemmon2': diemmon2, 'diemmon3': diemmon3, 'tong_diem': tong_diem}
# Thêm thí sinh vào danh sách
ds_thi_sinh = xu_ly_diem_thi.them_thi_sinh(ds_thi_sinh, thi_sinh)

# In danh sách thí sinh sau khi thêm
print("Danh sách thí sinh sau khi thêm:")
