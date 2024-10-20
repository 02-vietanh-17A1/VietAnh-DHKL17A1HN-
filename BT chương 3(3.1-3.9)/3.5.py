import numpy as np

# Bước 1: Đọc dữ liệu từ file heights_1.txt và weights_1.txt (giả sử các file chứa các giá trị theo hàng)
with open('Nguyen_Van_Nam_DHKL17A1HN_23174600055\\chương 3\\heights_1.txt', 'r') as f:
    height = [float(line.strip()) for line in f.readlines()]

with open('Nguyen_Van_Nam_DHKL17A1HN_23174600055\\chương 3\\weights_1.txt', 'r') as f:
    weight = [float(line.strip()) for line in f.readlines()]

# Câu 1: Tạo numpy array arr_height từ list height
arr_height = np.array(height)


# Câu 2: Tạo numpy array arr_weight từ list weight
arr_weight = np.array(weight)


# Câu 3: Tạo arr_height_m bằng cách quy đổi từ inch sang mét (1 inch = 0.0254 m)
inch_to_m = 0.0254
arr_height_m = arr_height * inch_to_m
print("Chiều cao (m):", arr_height_m)


# Câu 4: Tạo arr_weight_kg bằng cách quy đổi từ pound sang kg (1 pound = 0.453592 kg)
pound_to_kg = 0.453592
arr_weight_kg = arr_weight * pound_to_kg
print("Cân nặng (kg):", arr_weight_kg)


# Câu 5: Tính BMI = Cân nặng / (Chiều cao * Chiều cao)
arr_bmi = arr_weight_kg / (arr_height_m ** 2)
print("BMI:", arr_bmi)


# Câu 6: Lấy giá trị cân nặng ở vị trí index = 50
weight_at_index_50 = arr_weight_kg[50]
print("Cân nặng tại vị trí 50:", weight_at_index_50)


# Câu 7: Lấy chiều cao ở vị trí từ index 100 đến 110 (bao gồm 110) trong arr_height_m
height_from_100_to_110 = arr_height_m[100:111]
print("Chiều cao từ index 100 đến 110:", height_from_100_to_110)


# Câu 8: Lấy chiều cao ở vị trí từ index 100 đến 110 (bao gồm 110) trong arr_height_m
height_from_100_to_110 = arr_height_m[100:111]
print("Chiều cao từ index 100 đến 110:", height_from_100_to_110)


# Câu 9: Chiều cao trung bình và cân nặng trung bình của các cầu thủ
mean_height = np.mean(arr_height_m)
mean_weight = np.mean(arr_weight_kg)
print("Chiều cao trung bình:", mean_height)
print("Cân nặng trung bình:", mean_weight)


# Câu 10: Chiều cao và cân nặng lớn nhất của các cầu thủ
max_height = np.max(arr_height_m)
max_weight = np.max(arr_weight_kg)
print("Chiều cao lớn nhất:", max_height)
print("Cân nặng lớn nhất:", max_weight)


# Câu 11: Chiều cao và cân nặng nhỏ nhất của các cầu thủ
min_height = np.min(arr_height_m)
min_weight = np.min(arr_weight_kg)
print("Chiều cao nhỏ nhất:", min_height)
print("Cân nặng nhỏ nhất:", min_weight)