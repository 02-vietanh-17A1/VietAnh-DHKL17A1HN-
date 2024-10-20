import numpy as np

# Khởi tạo arr_a và arr_b
arr_a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
arr_b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

# Câu 1: Tạo array arr_c chỉ lấy duy nhất các phần tử xuất hiện ở cả arr_a và arr_b
arr_c = np.intersect1d(arr_a, arr_b)
print("arr_c (các phần tử chung của arr_a và arr_b):", arr_c)


# Câu 2: Tạo arr_d chứa các phần tử chỉ xuất hiện ở arr_a
arr_d = np.setdiff1d(arr_a, arr_b)
print("arr_d (các phần tử chỉ xuất hiện ở arr_a):", arr_d)


# Câu 3: Lọc các phần tử có giá trị từ 5 đến 10 của arr_c
arr_c_2 = np.array([2, 6, 1, 9, 10, 3, 27, 8, 6, 25, 16])
arr_f = arr_c_2[(arr_c_2 >= 5) & (arr_c_2 <= 10)]
print("arr_f (các phần tử từ 5 đến 10 của arr_c):", arr_f)