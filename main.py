def twosum(arr,target):
  
  l = 0
  r = len(arr)-1

  while l < r:
    if arr[l] + arr[r] == target:
      return[l,r]

    elif arr[l] + arr[r] < target:
      l += 1 

    else:
      r -= 1


target = 7
arr = [1,3,4,5,7]

print(twosum(arr,target))