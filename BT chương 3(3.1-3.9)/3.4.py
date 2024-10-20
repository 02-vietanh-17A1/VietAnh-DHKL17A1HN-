import numpy as np

# Câu 1: Tạo arr_zeros có 10 phần tử 0 và cập nhật phần tử ở vị trí thứ 5 thành 1
arr_zeros = np.zeros(10, dtype=int)
arr_zeros[4] = 1  # Cập nhật phần tử ở vị trí thứ 5 (index 4)
print("arr_zeros sau khi cập nhật:", arr_zeros)


# Câu 2: Tạo arr_h có giá trị từ 10 đến 24 và in danh sách các phần tử theo thứ tự đảo ngược
arr_h = np.arange(10, 25)
arr_h_reversed = arr_h[::-1]
print("arr_h theo thứ tự đảo ngược:", arr_h_reversed)


# Câu 3: Tạo arr_h có giá trị từ 10 đến 24 và in danh sách các phần tử theo thứ tự đảo ngược
arr_h = np.arange(10, 25)
arr_h_reversed = arr_h[::-1]
print("arr_h theo thứ tự đảo ngược:", arr_h_reversed)


# Câu 4: Thêm 2 phần tử có giá trị 10 và 20 vào cuối arr_1
arr_1 = np.append(arr_1, [10, 20])
print("arr_1 sau khi thêm 10 và 20:", arr_1)


# Câu 5: Thêm phần tử có giá trị 100 vào vị trí có index = 5
arr_1 = np.insert(arr_1, 5, 100)
print("arr_1 sau khi thêm 100 vào vị trí index = 5:", arr_1)


# Câu 6: Xóa các phần tử tại vị trí index = 0, 1, 2 từ array của câu 5
arr_1 = np.delete(arr_1, [0, 1, 2])
print("arr_1 sau khi xóa phần tử tại các vị trí index = 0, 1, 2:", arr_1)