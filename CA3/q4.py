def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    for i in range(1, len(pattern)):
        while length > 0 and pattern[i] != pattern[length]:
            length = lps[length - 1]
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
    return lps

n = int(input())
words = input().split()
result = words[0]

for word in words[1:]:
    combined = word + '#' + result[-min(len(result), len(word)):]
    lps = compute_lps(combined)
    max_prefix = lps[-1]
    result += word[max_prefix:]

print(result)