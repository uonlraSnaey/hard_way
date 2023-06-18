# 二分查找
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# 合并排序
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

# 用户输入数组
arr = input("请输入要排序的数组（以空格分隔）：").split()
arr = [int(num) for num in arr]

target = int(input("请输入要查找的目标元素："))

sorted_arr = merge_sort(arr)
index = binary_search(sorted_arr, target)

print("排序后的数组：", sorted_arr)
if index != -1:
    print("目标元素的索引：", index)
else:
    print("目标元素未找到")