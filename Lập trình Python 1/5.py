class Stack:
    def __init__(self, size=100):
        # Hàm tạo, khởi tạo ngăn xếp với kích thước cố định và mảng động
        self.size = size  # Kích thước tối đa của ngăn xếp
        self.stack = []  # Mảng để lưu các phần tử float
        self.top = -1  # Đỉnh của ngăn xếp (không có phần tử nào thì đỉnh là -1)

    def is_empty(self):
        # Kiểm tra ngăn xếp có trống hay không
        return self.top == -1

    def is_full(self):
        # Kiểm tra ngăn xếp có đầy hay không
        return self.top == self.size - 1

    def push(self, value):
        # Đưa một phần tử vào ngăn xếp
        if self.is_full():
            print("Ngăn xếp đã đầy! Không thể thêm phần tử.")
        else:
            self.stack.append(value)
            self.top += 1
            print(f"Đã thêm {value} vào ngăn xếp.")

    def pop(self):
        # Lấy một phần tử ra từ đỉnh ngăn xếp
        if self.is_empty():
            print("Ngăn xếp trống! Không thể lấy phần tử.")
            return None
        else:
            value = self.stack.pop()
            self.top -= 1
            print(f"Đã lấy {value} ra khỏi ngăn xếp.")
            return value

    def count(self):
        # Trả về số lượng phần tử hiện có trong ngăn xếp
        return self.top + 1

    def __del__(self):
        # Hàm huỷ để giải phóng tài nguyên
        print("Đang giải phóng ngăn xếp.")
        del self.stack