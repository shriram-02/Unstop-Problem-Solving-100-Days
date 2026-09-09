from collections import deque

n, d = map(int, input().split())
a = list(map(int, input().split()))

left = 0
best_len = 0
best_start = 1

freq = {}
minq = deque()
maxq = deque()

for right in range(n):
    freq[a[right]] = freq.get(a[right], 0) + 1

    while minq and a[minq[-1]] >= a[right]:
        minq.pop()
    minq.append(right)

    while maxq and a[maxq[-1]] <= a[right]:
        maxq.pop()
    maxq.append(right)

    while a[maxq[0]] - a[minq[0]] > d or freq[a[right]] > 1:
        freq[a[left]] -= 1

        if minq[0] == left:
            minq.popleft()
        if maxq[0] == left:
            maxq.popleft()

        left += 1

    length = right - left + 1

    if length > best_len:
        best_len = length
        best_start = left + 1

print(best_len, best_start)