List = [1,1,1,2,2,2,2,3]
top = 2

def topKFrequent(nums, k):
    # unrepeated = {}
    #
    # for num in nums:
    #     if num in unrepeated:
    #         unrepeated[num] += 1
    #     else:
    #         unrepeated[num] = 1
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    maxFreq = 0

    for num in nums:
        count[num] = 1 + count.get(num, 0) # We add this ocurrence of the number. The comma is the default if num not in the list
        if count[num] > maxFreq:
            maxFreq = count[num]
    for num, c in count.items():
        freq[c].append(num)

    result = []
    for i in range(maxFreq, 0, -1):
        for num in freq[i]:
            result.append(num)
            if len(result) == k:
                return result


print(topKFrequent(List, top))