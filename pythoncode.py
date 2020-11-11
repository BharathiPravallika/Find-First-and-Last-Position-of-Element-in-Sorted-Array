class Solution:
  def searchRange(self, nums: List[int],target:int)->List[int]:
    res = [-1,-1]
    N = len(nums)-1
    left = 0
    right = N
    #Sanity check
    if len(nums) == 0:
      return res
    #find starting
    while left < right-1:
      mid = left + (right-left)//2
      if nums[mid] == target:
        right = mid
      elif nums[mid]<target:
        left = mid+1
      else:
        right = mid-1
    if nums[left]==target:
      res[0] = left
    elif nums[right] == target:
      res[0]=right
    #Find ending 
    left = 0
    right = N
    while left < right-1:
      mid = left + (right-left)//2
      if nums[mid] == target:
        left = mid
      elif nums[mid]<target:
        left = mid+1
      else:
        right = mid-1
    if nums[right]==target:
      res[1] = right
    elif nums[left] == target:
      res[1]=left
    return res
