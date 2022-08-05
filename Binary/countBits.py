class Solution:
    def countBits(self, n: int) -> List[int]:
        list1,result = [],[]
        for i in range(n+1):
            list1.append(i)
        for n in list1:
            count = 0
            for i in range(32):
                bit = (n>>i)&1
                if(bit == 1):
                    count +=1
            result.append(count)
        return result