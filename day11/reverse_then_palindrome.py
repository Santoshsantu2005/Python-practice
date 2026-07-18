arr2 = list(map(int,input().split()))
arr = arr2.copy()
left=0
right=len(arr)-1

while left<right:
    arr[left],arr[right] = arr[right],arr[left]
    left+=1
    right-=1

if arr == arr2:
    print("Palindrome")
else:
    print("Not a palindrome")