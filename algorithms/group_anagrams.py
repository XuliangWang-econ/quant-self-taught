from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups anagrams using a hash map.
        Time Complexity: O(N * K log K), where N is number of strings and K is max string length.
        Space Complexity: O(N * K) to store the groups.
        """
        anagram_map = {}
        
        for word in strs:
            # Sort characters to generate the key
            sorted_word = sorted(word)
            key = tuple(sorted_word)
            
            # If key does not exist, create a new list
            if key not in anagram_map:
                anagram_map[key] = []
            
            # Append the word to the corresponding list
            anagram_map[key].append(word)
        
        # Return all groups
        return list(anagram_map.values())

# ====== Required Testing Section ======
if __name__ == "__main__":
    sol = Solution()
    
    # Helper function to normalize output for comparison (order varies)
    def normalize(result):
        return sorted([sorted(group) for group in result])

    # Test Case 1
    input1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected1 = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert normalize(sol.groupAnagrams(input1)) == normalize(expected1)
    
    # Test Case 2
    assert sol.groupAnagrams([""]) == [[""]]
    
    # Test Case 3
    assert sol.groupAnagrams(["a"]) == [["a"]]
    
    print("All test cases passed!")