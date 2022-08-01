class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n>>i)&1 #get last bit
            res = res | (bit<<(31-i)) #shift last bit to first pos
        return res