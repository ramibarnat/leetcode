def containsDuplcate(nums):
    appearences = {}
    for num in nums:
        if num in appearences:
            appearences[num] += 1
        else:
            appearences[num] = 1
        if appearences[num] == 2:
            return True
    return False

def slightlyBetter(nums):
    app = set()
    for num in nums:
        if num in app:
            return True
        app.add(num)
    return False