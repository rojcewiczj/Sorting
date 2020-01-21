# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
   for i in range(len(arr)): 
  
        if arr[i] == target: 
            return i 
  
   
   return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  while low <= high:
    mid = low + (high - low) // 2
    mid_value = arr[mid]
    if mid_value == target:
      return mid
    elif mid_value < target:
      low = mid + 1
    else:
      high = mid -1


  # TO-DO: add missing code

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  if len(arr) == 0:
    return -1
  middle = (low+high)//2
  mid_value = arr[middle]

  if mid_value == target:
    return middle

  elif mid_value < target:
    return binary_search_recursive(arr, target, middle + 1, high)
    
  else:
    return  binary_search_recursive(arr, target, low, middle - 1)
  # array empty
  # TO-DO: add missing if/else statements, recursive calls
