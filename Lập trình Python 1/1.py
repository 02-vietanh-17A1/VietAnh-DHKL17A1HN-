class Rectangle:
    def __init__(self):
        self.length = 0
        self.width = 0

    def input_data(self):
        self.length = float(input("Nhập độ dài cạnh của hình chữ nhật: "))
        self.width = float(input("Nhập độ dài chiều rộng của hình chữ nhật: "))

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def calculate_area(self):
        return self.length * self.width

    def display_info(self):
        perimeter = self.calculate_perimeter()
        area = self.calculate_area()
        print(f"\nThông tin hình chữ nhật:")
        print(f"Độ dài cạnh: {self.length}")
        print(f"Chiều rộng: {self.width}")
        print(f"Chu vi: {perimeter}")
        print(f"Diện tích: {area}")


# Chương trình chính
if __name__ == "__main__":
    rectangle = Rectangle()
    rectangle.input_data()
    rectangle.display_info()