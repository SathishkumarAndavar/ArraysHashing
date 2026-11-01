class Solution:

    def encode(self, strs:List(str)) -> str:
        sizes = []

        for i in strs:
            sizes.append(str(len(i)))
            sizes.append(",")
        
        sizes.append("#")
        sizes.extend(strs)

        return ''.join(sizes)

    def decode(self,s:str) -> List(str):
        strings = []
        L = []
        i = 0
        while s[i] != '#':

            j = i

            while s[j] != ',':
                j +=1

            
            strings.append(int(s[i:j]))

            i = j+1

        i += 1
        print(i)
        for sz in strings:
            L.append(s[i:i+sz])
            i = i + sz

        return L