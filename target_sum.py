#!/usr/bin/env python
import fileinput

k = 0
total = 0
integers = []

for idx,line in enumerate(fileinput.input()):
    if idx == 0:
        k = int(line)
    elif idx == 1:
        total = int(line)
    else:
        integers.append(int(line))

integers = sorted(integers)


# # Brute force method
# Get all combination of sets of size k and try adding them to see if matches total
# Running time, generate all sets and adding all of them
# Time complexity for combinations: O(n!/[(n-k)!k!] * k^2)
# Checking for sums, O(n)
# def ksum(num, k, total):
#     import itertools
#     # for i in xrange(1, len(num) + 1):
#     k_sets = list(itertools.combinations(num, k))
#     for k_set in k_sets:
#         k_set_list = list(k_set)
#         if sum(k_set_list) == total:
#             for number in k_set_list:
#                 print number
#
# ksum(integers, k, total)


# More time efficient method
# O(n^(k-1))
# This is probably close to optimal. We may be able to reduce iterations by using generators
def ksum(num, k, target):
    i = 0
    result = set()
    if k == 2:
        j = len(num) - 1
        while i < j:
            if num[i] + num[j] == target:
                result.add((num[i], num[j]))
                i += 1
            elif num[i] + num[j] > target:
                j -= 1
            else:
                i += 1
    else:
        while num and i < len(num) - k + 1:
            newtarget = target - num[i]
            subresult = ksum(num[i + 1:], k - 1, newtarget)
            if subresult:
                result = result | set((num[i],) + nr for nr in subresult)
            i += 1

    return result

for t in ksum(integers, k, total):
    print '\n'.join(map(str, list(t)))
