# Leet Code Minimum Length Daily Challenge: 7th Oct 24
# 44ms Runtime - Beat 57% submissions
# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/?envType=daily-question&envId=2024-10-07
def minLength( s: str) -> int:
    suba , subb = "AB", "CD"
    flag = False
    atmpflag = False
    btmpflag = False
    while not flag:
        if suba in s:
            s = s.replace(suba, "",1)
        else:
            atmpflag = True
        if subb in s:
            s = s.replace(subb, "", 1)
        else:
            btmpflag = True
        if atmpflag and btmpflag:
            flag = True
        else:
            atmpflag = False
            btmpflag = False

    return (len(s))


print(minLength("GAABBK"))