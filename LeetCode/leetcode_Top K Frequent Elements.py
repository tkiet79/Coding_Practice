nums = [1,2,2,3,3,3,4,5,5,6,6,6,6,7,8,8,7,6,9]
k = 2
check_list = dict.fromkeys(nums,0)
for s in nums:
    check_list[s] +=1

count = []
for k, v in check_list.items():
    count.append(v)
    
count.sort()
for i in range(k):
    print([check_list.keys()]) 

#keys = [k  if v == target_value]

    
 


