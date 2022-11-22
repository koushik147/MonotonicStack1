class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mstack = [] # creating a empty array
        result = [0] * len(temperatures) # creating a array with values 0 in length of temperatures
        
        for i in range(len(temperatures)):
            while mstack and temperatures[mstack[-1]]<temperatures[i]: # run until mstack is not null and temperatures of last value is less than ith value of temperatures 
                nextWarmer = i-mstack[-1] # subtracting the mstack last element from ith value and store in next warmer
                result[mstack[-1]] = nextWarmer # assigning the next warmer to result array
                mstack.pop() # popping the mstack value
            mstack.append(i) # appending the ith value in mstack
        return result # returning the result