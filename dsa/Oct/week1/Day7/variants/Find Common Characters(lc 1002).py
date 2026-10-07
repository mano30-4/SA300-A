class Solution:
    def commonChars(self, words: list[str]):
        output = []
        minimum_hashmap = {}
        for i in words[0]:
            if i not in minimum_hashmap:
                minimum_hashmap[i] = 1
            else:
                minimum_hashmap[i] += 1

        for i in range(1, len(words)):
            hashmap = {}
            for j in words[i]:
                if j not in hashmap:
                    hashmap[j] = 1
                else:
                    hashmap[j] += 1
            for k in minimum_hashmap:
                if k not in hashmap:
                    minimum_hashmap[k] = 0
                else:
                    minimum_hashmap[k] = min(minimum_hashmap[k], hashmap[k])
        for key in minimum_hashmap:
            for i in range(minimum_hashmap[key]):
                output.append(key)

        return output


'''
test cases 
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
'''







