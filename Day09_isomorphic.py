def is_isomorphic(word1, word2):
    # Step 1: Check if both words are of the same length
    if len(word1) != len(word2):
        return False

    # Step 2: Create two dictionaries for mapping
    map1 = {}
    map2 = {}

    # Step 3: Iterate over both words simultaneously
    for c1, c2 in zip(word1, word2):
        # Check mapping from word1 to word2
        if c1 in map1:
            if map1[c1] != c2:
                return False
        else:
            map1[c1] = c2

        # Check mapping from word2 to word1
        if c2 in map2:
            if map2[c2] != c1:
                return False
        else:
            map2[c2] = c1

    # Step 4: If no mismatches found, the words are isomorphic
    return True


# Main logic with input handling
try:
    words = input("Enter two words to check isomorphic condition (space-separated): ").lower().split()

    if len(words) != 2:
        print("❌ Please enter exactly two words separated by space.")
    else:
        word1, word2 = words
        if is_isomorphic(word1, word2):
            print("✅ Given words are isomorphic.")
        else:
            print("❌ Given words are not isomorphic.")
except Exception as e:
    print(f"Error: {e}")
