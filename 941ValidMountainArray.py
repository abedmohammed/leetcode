class Solution(object):
    def validMountainArray(self, arr):
      length = len(arr)

      if(length < 3):
         return False
      
      left = 0
      right = length - 1

      while(True):
        if(left == right or arr[left+1] == arr[left]):
            return False
        if(arr[left+1] > arr[left]):
            left += 1
        elif(arr[left+1] < arr[left]):
           break
      
      if(left == 0):
         return False

      while(right > left):
         if(arr[right - 1] == arr[right]):
            return False
         if(arr[right - 1] > arr[right]):
            right -= 1
         else: 
            return False

      return True

answer = Solution()
print(answer.validMountainArray([9,8,7,6,5,4,3,2,1,0]))
