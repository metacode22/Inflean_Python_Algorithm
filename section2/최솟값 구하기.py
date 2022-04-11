arr = [5, 3, 7, 9, 2, 5, 2, 6]
# arr_min = arr[0]

# for i in range(1, len(arr)):
#     if arr[i] < arr_min:
#         arr_min = arr[i]

# print(arr_min)

arr_min = float('inf')              # python에서 가장 큰 무한대 값

for i in arr:
    if i < arr_min:
        arr_min = i

print(arr_min)