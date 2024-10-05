# Leet Code Permutations Daily Challenge: 5th Oct 24
# 1799ms Completion time - reduced from 5000
# getCount is inefficent
# https://leetcode.com/problems/permutation-in-string/description/?envType=daily-question&envId=2024-10-05
def getCount(letters) -> dict:
    lcount = {}
    counted_letters = []
    while len(letters) >= 1:
        lcount.update({letters[0]: letters.count(letters[0])})
        letters = letters.replace(letters[0], "")
    return lcount
def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    s1_count = getCount(s1)
    win_size = len(s1)
    for x in range(len(s2) - len(s1) + 1):
        window = s2[x:win_size + x]
        win_count = getCount(window)
        if win_count == s1_count:
            return True
    return False

s1 = "ab"
s2 = "eidboaoo"
print(checkInclusion(s1,s2))