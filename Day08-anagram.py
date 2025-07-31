char1, char2 = input("Enter two words for anagram: ").split()

def same_elements(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

if same_elements(char1, char2):
    def check_anagram(charactor1, charactor2):
        count = 0
        for i, charactor in  enumerate(charactor1.lower()):
            match charactor:
                case 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | \
                     'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z':
                    if charactor in charactor2.lower():
                        count += 1
        if count == len(charactor1):
            print(f"✅ Your given '{char1}' and '{char2}' are anagrams.")
        else:
            print(f"❌ Your given '{char1}' and '{char2}' are not anagrams.")
    check_anagram(char1, char2)
else:
    print("❌ There is no anagram found.")
