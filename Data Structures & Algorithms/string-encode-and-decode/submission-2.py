class Solution:

    def encode(self,strs:List(str)) -> str:

        sizes = []

        for i in strs:
            sizes.append(str(len(i)))
            sizes.append(',')
        sizes.append("#")
        sizes.extend(strs)

        return ''.join(sizes)

    def decode(self,s:str) -> List(str):

        hashind = s.find('#')

        len_str = s[:hashind]
        res = []
        lens = [ int(x) for x in len_str.split(',') if x ]

        for i in lens:
            res.append(s[hashind+1:hashind+i+1])
            hashind = hashind + i

        return res