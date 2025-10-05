class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        hash = {}
        for i in range(0, len(numbers)):
            if numbers[i] in hash:
                hash[numbers[i]] += 1
            else:
                hash[numbers[i]] = 1

        for i in hash:
            if (target - i) in hash:
                c1 = 1
                c2 = 1
                for j in hash:
                    if j < i:
                        c1 += hash[j]
                for j in hash:
                    if j < (target - i):
                        c2 += hash[j]
                if i == (target - i):
                    c2 += 1
                return [c1,c2]