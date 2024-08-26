class Solution(object):
    def mergeTriplets(self, triplets, target):
        # relevant = []
        # # get all relevant triplets
        # for triplet in triplets:
        #     valid = True
        #     for i in range(3):
        #         if triplet[i] > target[i]:
        #             valid = False
        #             break
        #     if valid:
        #         relevant.append(triplet)

        # # Check if we have all the pieces
        # for i in range(3):
        #     valid = False
        #     for triplet in relevant:
        #         if triplet[i] == target[i]:
        #             valid = True
        #             break
        #     if not valid:
        #         return False

        # return True

        # # Cleaner solution
        valid = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for (
                i,
                v,
            ) in enumerate(t):
                if v == target[i]:
                    valid.add(i)

        return len(valid) == 3


answer = Solution()
print(
    answer.mergeTriplets(
        triplets=[[2, 5, 3], [1, 8, 4], [1, 7, 5], [9, 7, 2], [8, 9, 5]],
        target=[2, 7, 5],
    )
)
