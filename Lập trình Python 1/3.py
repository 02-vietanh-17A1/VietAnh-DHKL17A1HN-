import math

class PhanSo:
    def __init__(self, tu_so=0, mau_so=1):
        # Khởi tạo tử số và mẫu số, mặc định mẫu số là 1 để tránh chia cho 0
        self.tu_so = tu_so
        self.mau_so = mau_so
        if not self.kiem_tra_hop_le():
            print("Phân số không hợp lệ. Mẫu số không thể bằng 0.")
    
    def kiem_tra_hop_le(self):
        # Kiểm tra tính hợp lệ của phân số (mẫu số không được bằng 0)
        return self.mau_so != 0

    def nhap_phan_so(self):
        # Nhập phân số từ người dùng, yêu cầu mẫu số không được bằng 0
        while True:
            self.tu_so = int(input("Nhập tử số: "))
            self.mau_so = int(input("Nhập mẫu số: "))
            if self.kiem_tra_hop_le():
                break
            else:
                print("Mẫu số không được bằng 0. Vui lòng nhập lại.")

    def rut_gon(self):
        # Rút gọn phân số bằng cách chia cho ước chung lớn nhất (UCLN) của tử và mẫu
        ucln = math.gcd(self.tu_so, self.mau_so)
        self.tu_so = self.tu_so // ucln
        self.mau_so = self.mau_so // ucln

    def in_phan_so(self):
        # Rút gọn trước khi in
        self.rut_gon()
        if self.mau_so == 1:
            print(f"Phân số: {self.tu_so}")
        else:
            print(f"Phân số: {self.tu_so}/{self.mau_so}")