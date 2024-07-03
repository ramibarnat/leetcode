def groupAnagrams(strs):
    res = []
    seen = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word in seen:
            res[seen[sorted_word]].append(word)
        else:
            res.append([word])
            seen[sorted_word] = len(res)-1
    
    return res

def groupAnagramsBetter(strs):
    res = {}

    for s in strs:
        count = [0] * 26

        for c in s: # increment each letter index
            count[ord(c.lower())-97] += 1

        # It is more efficient to convert a list to a tuple than a string
        # key = ",".join(map(str,count)) 

        key = tuple(count)
        if key in res:
            res[key].append(s)
        else:
            res[key] = [s]
    
    return res.values()
        
# a:1b:0c:0d:0e:1
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagramsBetter(strs))