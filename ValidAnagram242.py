def isAnagram(s,t):
    dic = {}
    if len(s) != len(t):
        return False
    
    for char in s:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
    for char in t:
        if char in dic and dic[char] != 0:
            dic[char] -= 1
        else:
            return False
    return True