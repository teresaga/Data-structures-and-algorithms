def house_robber(nums): # O(n) space complexity = O(1)

    for i in range(1,len(nums)):
        # nums[i] is the maximum amount that can be rob from the first i houses
        # there are two options here:
        # 1- rob the house "i", sum up the value of house[i] and house[i-2] (not adjacent to house[i]) to get the max amount that can be robbed
        # 2- dont rob house "i", take the accumulated amount that is in the house[i-1]
        # we choose the option that give us the greatest value 
        nums[i] = max(nums[i-1], nums[i-2] + nums[i])

    return nums[len(nums)-1]

def memoization_house_robber(): # O(n) space complexity = O(n)
    cache = {}
    def house_robber_recursive(nums, i):
        if i in cache:
            return cache[i]
        
        if i < 0:
            return 0
        
        cache[i] = max(house_robber_recursive(nums, i-1), nums[i] + house_robber_recursive(nums, i-2))

        return cache[i]
    
    return house_robber_recursive

nums = [1,2,3,1]
nums2 = [2,7,9,3,1]
#print(house_robber(nums))
#print(house_robber(nums2))

nums = [1,2,3,1]
nums2 = [2,7,9,3,1]

robber = memoization_house_robber()
print(robber(nums, len(nums)-1))
robber2 = memoization_house_robber()
print(robber2(nums2, len(nums2)-1))