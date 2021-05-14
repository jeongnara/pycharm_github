def solution(arr):
     left = 0
     right = len(arr) - 1

     while left < right:
         # arr[left]과 arr[right]의 값을 서로 바꿈

         arr[left], arr[right] = arr[right], arr[left]

         left += 1
         right -= 1
     return arr

arr = [1, 4, 2, 3]
ret = solution(arr)

print("Solution: return value of the function is", ret," .")