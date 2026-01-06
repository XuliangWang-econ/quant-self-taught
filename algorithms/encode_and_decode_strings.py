from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string.
        Time Complexity: O(N) where N is total characters.
        Space Complexity: O(1) auxiliary (excluding output).
        """
        result = ""
        
        for s in strs:
            # 1. Get string length and convert to string
            length_str = str(len(s))
            
            # 2. Construct encoded string with delimiter
            encoded_str = length_str + ":" + s
            
            # 3. Append to result
            result += encoded_str
            
        return result

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string to a list of strings.
        Time Complexity: O(N) where N is total characters.
        Space Complexity: O(N) for result list.
        """
        result_list = []
        current_pos = 0
        
        while current_pos < len(s):
            # 1. Find the delimiter position
            colon_pos = s.find(":", current_pos)
            
            # 2. Parse the length from the substring before delimiter
            length_str = s[current_pos:colon_pos]
            length = int(length_str)
            
            # 3. Calculate content boundaries
            start_pos = colon_pos + 1
            end_pos = start_pos + length
            
            # 4. Extract content and append to list
            content = s[start_pos:end_pos]
            result_list.append(content)
            
            # 5. Update current position
            current_pos = end_pos
        
        return result_list

# ====== Required Testing Section ======
if __name__ == "__main__":
    codec = Codec()
    
    # Test Case 1: Standard words
    input1 = ["Hello", "World"]
    assert codec.decode(codec.encode(input1)) == input1
    
    # Test Case 2: Empty string
    input2 = [""]
    assert codec.decode(codec.encode(input2)) == input2
    
    # Test Case 3: Mixed empty and non-empty strings
    input3 = ["", "hello", "", "world", ""]
    assert codec.decode(codec.encode(input3)) == input3
    
    # Test Case 4: Strings containing delimiters
    input4 = ["a:b", "c:d:e", "f"]
    assert codec.decode(codec.encode(input4)) == input4
    
    # Test Case 5: Strings containing numbers
    input5 = ["123", "4567", "89"]
    assert codec.decode(codec.encode(input5)) == input5
    
    print("All test cases passed!")