
import csv

def mo_file_diem_thi(ten_file):
    f = open(ten_file, 'r')
    reader = csv.reader(f)
    # Tạo một danh sách rỗng để lưu trữ các thí sinh
    ds_thi_sinh = []
    # Duyệt qua các dòng trong file
    for dong in reader:
        # Tạo một từ điển để lưu trữ thông tin của một thí sinh
        thi_sinh = {}
        # Gán các giá trị cho các khóa tương ứng
        thi_sinh['ma_thi_sinh'] = dong[0]
        thi_sinh['ten_thi_sinh'] = dong[1]
        thi_sinh['khu_vuc'] = dong[2]
        thi_sinh['diemmon1'] = float(dong[3])
        thi_sinh['diemmon2'] = float(dong[4])
        thi_sinh['diemmon3'] = float(dong[5])
        thi_sinh['tong_diem'] = float(dong[6])
        # Thêm thí sinh vào danh sách
        ds_thi_sinh.append(thi_sinh)
    # Đóng file
    f.close()
    # Trả về danh sách thí sinh
    return ds_thi_sinh

# Hàm thêm thông tin các thí sinh
def them_thi_sinh(ds_thi_sinh, thi_sinh):
    # Thêm thí sinh vào danh sách
    ds_thi_sinh.append(thi_sinh)
    # Trả về danh sách thí sinh đã cập nhật
    return ds_thi_sinh

# Hàm in danh sách các thí sinh với đầy đủ thông tin
def in_danh_sach_thi_sinh(ds_thi_sinh):
    # In tiêu đề
    print("Danh sách thí sinh:")
    print("Mã thí sinh\tTên thí sinh\tKhu vực\tĐiểm môn 1\tĐiểm môn 2\tĐiểm môn 3\tTổng điểm")
    # Duyệt qua các thí sinh trong danh sách
    for thi_sinh in ds_thi_sinh:
        # In thông tin của mỗi thí sinh
        print(thi_sinh['ma_thi_sinh'], thi_sinh['ten_thi_sinh'], thi_sinh['khu_vuc'], thi_sinh['diemmon1'], thi_sinh['diemmon2'], thi_sinh['diemmon3'], thi_sinh['tong_diem'], sep="\t")

# Hàm lưu file danh sách điểm thí sinh
def luu_file_diem_thi(ds_thi_sinh, ten_file):
    # Mở file csv với chế độ ghi
    f = open(ten_file, 'w')
    # Tạo một đối tượng writer để ghi dữ liệu vào file
    writer = csv.writer(f)
    # Duyệt qua các thí sinh trong danh sách
    for thi_sinh in ds_thi_sinh:
        # Tạo một danh sách để lưu trữ các giá trị của một thí sinh
        dong = [thi_sinh['ma_thi_sinh'], thi_sinh['ten_thi_sinh'], thi_sinh['khu_vuc'], thi_sinh['diemmon1'], thi_sinh['diemmon2'], thi_sinh['diemmon3'], thi_sinh['tong_diem']]
        # Ghi danh sách vào file
        writer.writerow(dong)
    # Đóng file
    f.close()

# Hàm tìm thí sinh có tổng điểm cao nhất
def tim_thi_sinh_max(ds_thi_sinh):
    # Giả sử thí sinh đầu tiên có tổng điểm cao nhất
    max_thi_sinh = ds_thi_sinh[0]
    # Duyệt qua các thí sinh còn lại trong danh sách
    for thi_sinh in ds_thi_sinh[1:]:
        # So sánh tổng điểm của thí sinh hiện tại với thí sinh có tổng điểm cao nhất
        if thi_sinh['tong_diem'] > max_thi_sinh['tong_diem']:
            # Cập nhật thí sinh có tổng điểm cao nhất
            max_thi_sinh = thi_sinh
    # Trả về thí sinh có tổng điểm cao nhất
    return max_thi_sinh

# Hàm xóa khỏi danh sách các thí sinh có tổng điểm < điểm chuẩn
def xoa_thi_sinh(ds_thi_sinh, diem_chuan):
    # Tạo một danh sách rỗng để lưu trữ các thí sinh đạt điểm chuẩn
    ds_thi_sinh_moi = []
    # Duyệt qua các thí sinh trong danh sách
    for thi_sinh in ds_thi_sinh:
        # Kiểm tra nếu thí sinh có tổng điểm >= điểm chuẩn
        if thi_sinh['tong_diem'] >= diem_chuan:
            # Thêm thí sinh vào danh sách mới
            ds_thi_sinh_moi.append(thi_sinh)
    # Trả về danh sách mới
    return ds_thi_sinh_moi

# Hàm sắp xếp danh sách thí sinh theo thứ tự giảm dần của tổng điểm
def sap_xep_thi_sinh(ds_thi_sinh):
    # Sử dụng hàm sorted() để sắp xếp danh sách theo tổng điểm giảm dần
    ds_thi_sinh_sap_xep = sorted(ds_thi_sinh, key=lambda thi_sinh: thi_sinh['tong_diem'], reverse=True)
    # Trả về danh sách đã sắp xếp
    return ds_thi_sinh_sap_xep

# File qlydiemthi_v2.py
# Nhập module xu_ly_diem_thi
import xu_ly_diem_thi

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
