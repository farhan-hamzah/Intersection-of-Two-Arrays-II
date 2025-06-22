from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Hitung kemunculan setiap elemen di nums1
        count1 = Counter(nums1)
        result = []

        # Iterasi elemen di nums2 dan cek apakah masih tersedia di count1
        for num in nums2:
            if count1[num] > 0:
                result.append(num)
                count1[num] -= 1  # Kurangi jumlahnya

        return result

# Contoh penggunaan:
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    output = solution.intersect(nums1, nums2)
    print("Hasil:", output)  # Output: [2, 2]
