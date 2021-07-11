class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
            summary = collections.Counter(nums1)
            answer = list()
            for num in nums2:
                if num in summary:
                    if summary[num] > 0:
                        summary[num] -= 1
                        answer.append(num)
            return answer