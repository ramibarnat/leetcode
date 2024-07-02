def myAtoi(s):
    new_str = []
    s = s.lstrip()
    seen_num = False
    neg = False
    # INT32_MIN = -2_147_483_648
    INT32_MAX = 2147483647

    for i, char in enumerate(s):
        if char == '+' and i == 0:
            continue
        if char == '-' and i == 0:
            neg = True
        elif char == '0' and seen_num:
            new_str.append(char)
        elif char.isdigit():
            seen_num = True
            new_str.append(char)
        else:
            break
    
    res = "".join(new_str)
    if not res.isdigit(): 
        return 0
    
    res = int(res)
    if neg:
        if res > INT32_MAX + 1:
            return -1 * (INT32_MAX + 1)
        return -1 * res
    if res > INT32_MAX:
        return INT32_MAX
    return res


print(myAtoi("+1"))
            