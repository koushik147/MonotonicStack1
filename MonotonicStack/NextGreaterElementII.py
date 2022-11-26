
#TimeComplexity: O(n)
#SpaceComplexity: O(n)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1]*len(nums) # creating resultant array with len of nums with value -1
        mstack = [] # creating a empty array
        
        for i in range(2*(len(nums))):
            while (len(mstack)!=0 and nums[mstack[-1]]<nums[i%len(nums)]): # run until length of mstack is not equal to 0 and array of last value in array is less than length of nums
                greater = nums[i%len(nums)] # assigning the length of nums modules i to greater
                result[mstack[-1]] = greater # assigning greater to mstack of last index of array
                mstack.pop() # popping the mstack array
                
            if (i<len(nums)): # if i is less than length of nums
                mstack.append(i) # appending the i to mstack
        return result # returning the result
    
