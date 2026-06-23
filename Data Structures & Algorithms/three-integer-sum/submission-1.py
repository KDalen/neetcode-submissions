class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
                
            target = -1*nums[i]
            l,r=i+1,len(nums)-1
            
            while l <r:
                if l==i:
                    l+=1
                if r==i:
                    r-=1
                if target > (nums[l]+ nums[r]):
                    l+=1
                elif target < (nums[l]+ nums[r]):
                    r-=1
                else:
                    output.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
        return output


