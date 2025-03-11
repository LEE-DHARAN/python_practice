from typing import List


def containsDuplicate(nums:List[int])->bool:  
    freq = {}  

    for num in nums:  
        if num in freq:  
            return True  
        freq[num] = 1  
    
    return False  

ans = containsDuplicate([1,2,3])
print(ans)