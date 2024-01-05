import csv
import os
def doc_danh_sach(list_dict): #Định nghĩa hàm
    list_dict.clear() #Xóa toàn bộ phần tử trong danh sách list_dict để chuẩn bị cho việc đọc dữ liệu mới
    current_path = os.getcwd() #lấy đường dẫn thư mục làm việc hiện tại
    csv_path = current_path  # tạo đường dẫn đầy đủ với tệp csv mà ta muốn đọc
    with open(csv_path, mode='r', encoding='utf-8') as csv_file: #mở tệp tin csv trong chế độ đọc
        csv_reader = csv.DictReader(csv_file) #đọc nội dung của tệp tin csv được mở
        for row in csv_reader: #lặp qua từng dòng trong tệp tin, mỗi dòng được đọc là một từ điển, biến row được sử dụng để lưu trữ dictionary hiện tại
            list_dict.append(row) #thêm dictionary row vào danh sách list_dict

def nhap_thong_tin():
    file = open("danh_sach_hs.txt", "a")
    n = int(input("Nhập số lượng học sinh cần thêm: "))
    for i in range(n):
        ten = input("Nhập tên học sinh: ")
        ma_so = input("Nhập mã số học sinh: ")
        diem_toan = float(input("Nhập điểm Toán: "))
        diem_ly = float(input("Nhập điểm Lý: "))
        diem_hoa = float(input("Nhập điểm Hoá: "))
        dtb = (diem_toan + diem_ly + diem_hoa) / 3
        if dtb >= 9:
            xep_loai = "Xuất sắc"
        elif dtb >= 8:
            xep_loai = "Giỏi"
        elif dtb >= 7:
            xep_loai = "Khá"
        elif dtb >= 5:
            xep_loai = "Trung bình"
        else:
            xep_loai = "Yếu"
        file.write(f"{ten},{ma_so},{diem_toan},{diem_ly},{diem_hoa},{dtb},{xep_loai}\n")
    
    file.close()

def luu_file_csv():
    file = open("danh_sach_hoc_sinh.txt", "r")
    content = file.read()
    file.close()
    file_csv = open("files/ds_hoc_sinh.csv", "w")
    file_csv.write("Tên,Mã số,Điểm Toán,Điểm Lý,Điểm Hoá,Điểm TB,Xếp loại\n")
    file_csv.write(content)
    file_csv.close()

def sap_xep():
    file = open("danh_sach_hoc_sinh.txt", "r")
    lines = file.readlines()
    file.close()
    students = []
    for line in lines:
        fields = line.split(",")
        student = {}
        student["ten"] = fields[0]
        student["ma_so"] = fields[1]
        student["diem_toan"] = float(fields[2])
        student["diem_ly"] = float(fields[3])
        student["diem_hoa"] = float(fields[4])
        student["dtb"] = float(fields[5])
        student["xep_loai"] = fields[6].strip()
        students.append(student)
    print("Danh sách các học sinh trước khi sắp xếp:")
    for student in students:
        print(student)
    students.sort(key=lambda x: x["dtb"], reverse=True)
    print("Danh sách các học sinh sau khi sắp xếp:")
    for student in students:
        print(student)

def thoat():
    print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
    exit()

options = ["Mở file danh sách học sinh", "Nhập thông tin các học sinh", "Lưu danh sách các học sinh vào file csv", "Sắp xếp các học sinh theo thứ tự giảm dần của điểm trung bình", "Thoát chương trình"]

while True:
    print("Chào mừng bạn đến với chương trình quản lý học sinh version1. Vui lòng chọn một trong các chức năng sau:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    choice = input("Nhập tùy chọn của bạn: ")
    if choice == "1":
        mo_file()
    elif choice == "2":
        nhap_thong_tin()
    elif choice == "3":
        luu_file_csv()
    elif choice == "4":
        sap_xep()
    elif choice == "5":
        thoat()