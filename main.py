from collections import Counter

def is_anagram(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    return Counter(s1) == Counter(s2)

def group_anagrams(words):
    groups = {}
    for word in words:
        key = tuple(sorted(word.lower()))
        groups.setdefault(key, []).append(word)
    return list(groups.values())

def find_anagrams_in_text(text, pattern):
    """Matndagi barcha anagramma pozitsiyalarini topadi."""
    n, p = len(text), len(pattern)
    pc = Counter(pattern)
    wc = Counter(text[:p])
    result = [0] if wc == pc else []
    for i in range(1, n - p + 1):
        wc[text[i-1]] -= 1
        if wc[text[i-1]] == 0: del wc[text[i-1]]
        wc[text[i+p-1]] += 1
        if wc == pc: result.append(i)
    return result

if __name__ == "__main__":
    print(is_anagram("listen", "silent"))   # True
    print(is_anagram("hello",  "world"))    # False

    words = ["eat","tea","tan","ate","nat","bat"]
    print(group_anagrams(words))
    # [['eat','tea','ate'], ['tan','nat'], ['bat']]

    print(find_anagrams_in_text("cbaebabacd", "abc"))  # [0, 6]
