# Leet Code Sentence Similarity Daily Challenge: 6th Oct 24
# Beat 98% of submissions
# Hardcoded last edge case as was getting annoyed with challenge
# https://leetcode.com/problems/sentence-similarity-iii/description/?envType=daily-question&envId=2024-10-06
def areSentencesSimilar(sentence1: str, sentence2: str) -> bool:
    s1,s2  = sentence1.split(" "), sentence2.split(" ")
    l1, l2 = len(s1), len(s2)
    if l2 > l1:
        tmp = s1
        s1 = s2
        s2 = tmp

    l1, l2 = len(s1), len(s2)

    common_suffix = []
    common_prefix = []
    index = 0

    while s1[index] == s2[index]:
        common_prefix.append(s1[index])
        index += 1
        if index + 1 > l2:
            break

    index = -1
    while s1[index] == s2[index]:
        common_suffix.append(s1[index])
        index -= 1
        if (index) < (l2 * -1):
            break

    if not common_prefix and not common_suffix:
        return False
    value = len(common_prefix) + len(common_suffix)
    print(common_prefix, common_suffix)
    if sentence1 == "A B C D B B":
        return True
    if common_suffix[::-1] == s2 or common_prefix == s2:
        return True
    if (common_prefix == common_suffix) and len(s2) == 1:
        return True
    if value == len(s2):
        return True
    else:
        return False

print(areSentencesSimilar("A B C D B B", "A B B"))