from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Finds the length of the longest consecutive elements sequence.
        Time Complexity: O(N) - Each number is visited at most twice.
        Space Complexity: O(N) - To store the hash set.
        """
        nums_set = set(nums)
        max_len = 0

        for n in nums_set:
            # Only start counting if 'n' is the beginning of a sequence
            if n - 1 not in nums_set:
                current_value = n
                current_len = 1

                # Expand the sequence
                while current_value + 1 in nums_set:
                    current_value += 1
                    current_len += 1

                max_len = max(max_len, current_len)

        return max_len

# ====== Required Testing Section ======
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Standard example
    input1 = [100, 4, 200, 1, 3, 2]
    assert sol.longestConsecutive(input1) == 4
    
    # Test Case 2: Unsorted with duplicates
    input2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    assert sol.longestConsecutive(input2) == 9
    
    # Test Case 3: Empty list
    assert sol.longestConsecutive([]) == 0
    
    # Test Case 4: Single element
    assert sol.longestConsecutive([1]) == 1
    
    print("All test cases passed!")