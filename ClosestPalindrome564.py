# 123

# 13 -> 131
# 11 -> 111
# 12 -> 121
# len(123) = 3 -> '9' * 2 = 99
# len(123) = 3 -> '1' + '0'*2 + '1' = '1001'


def nearestPalindromic(n: str) -> str:
    def generatePalindrome(num):
        if len(n) % 2 == 0:
            return num + num[::-1]
        else:
            return num[:-1] + num[::-1]
    
    number = int(n[:(len(n)+1)//2])
    candidates = {
        generatePalindrome(str(number)),
        generatePalindrome(str(number+1)),
        generatePalindrome(str(number-1)),
        '9' * (len(n)-1),
        '1' + '0'*(len(n)-1) + '1'
    }

    candidates.discard(n)
    res = float('inf')
    minimum = float('inf')
    for candidate in candidates:
        dif = abs(int(n)-int(candidate))
        if dif < minimum or (dif == minimum and int(candidate) < int(res)):
            minimum = dif
            res = candidate

    return res



print(nearestPalindromic("19974"))