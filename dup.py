from typing import List


def containsDuplicate(nums:List[int])->bool:  
    hash_map = {}  

    for i in nums:  
        if i in hash_map:  
            return True  
        hash_map[i] = 1  
    
    return False  

ans = containsDuplicate([1,2,3])
print(ans)