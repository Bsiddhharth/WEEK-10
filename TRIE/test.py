# def c(arr):
#  i=0
#  while i<len(arr)-1:
#      if arr[i]==0:
#          arr.insert(i+1,0)
#          arr.pop()
#          i+=2
#      else:
#          i+=1
         
# arr=       [1,0,2,3,0,4,5,0] 
# c(arr)
# print(arr)
             
             
# def weigh(w):
#     w.sort()           
#     ans=0
#     t=0
    
#     for i in w:
#         if t+i > 5000:
#             break
        
#         t+=i
#         ans+=1
#     return ans

# def ss(nums):
#         a=set()
#         b=set()
#         n=0
#         for i in nums:
#             if i  in a:
#                 b.add(i)
#             else:
#                 a.add(i) 
#         c=a-b
#         for i in c:
#             n+=i
#         print(c)   
        
        
# nums=[1,2,3,2]        
# ss(nums)