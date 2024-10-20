# Câu 1
import numpy as np

# Câu 1: Tạo numpy array arr từ 0 đến 9
arr = np.arange(10)
print("Array arr:", arr)

# Hiển thị kiểu dữ liệu và kích thước của arr
print("Kiểu phần tử trong arr:", arr.dtype)
print("Kích thước của arr:", arr.shape)

 
 # Câu 2: Tạo arr_old (phần tử lẻ) và arr_even (phần tử chẵn)
arr_odd = arr[arr % 2 != 0]  # Các phần tử lẻ
arr_even = arr[arr % 2 == 0]  # Các phần tử chẵn
print("arr_odd:", arr_odd)
print("arr_even:", arr_even)


# Câu 3: Tạo arr_update_1, phần tử chẵn giữ nguyên, phần tử lẻ thay bằng 100
arr_update_1 = np.where(arr % 2 == 0, arr, 100)
print("arr_update_1:", arr_update_1)