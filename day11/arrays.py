arr = [2, 4, 7, 11, 15]
target = 18
left=0
right=len(arr)-1
while left<right:
    sum = arr[left] + arr[right]
    if sum == target:
        print(arr[left],arr[right])
        break

    elif sum < target:
        left +=1
    else:
        right -= 1
