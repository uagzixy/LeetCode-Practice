# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
def lengthOfLongestSubstring(s):
    l = len(s)
    if s != '' and len(s) != 1:
        left = 0
        d = []
        newDict = dict()
        for i in range(l):
            if s[i] in newDict and newDict[s[i]] >= left:
                d.append(i - left)
                left = newDict[s[i]] + 1
            newDict[s[i]] = i
        d.append(l - left)
        d.sort()
        return d[-1]
    elif len(s) == 1:
        return 1
    else:
        return 0

if __name__ == '__main__':
    print(lengthOfLongestSubstring(eval(input())))