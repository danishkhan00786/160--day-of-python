from collections import Counter
sentence = input("enter sentence").replace(" ","" ).lower()
set_of_sentence = Counter(sentence)

for charactor_sentence in set_of_sentence:
   match charactor_sentence:
      case 'a'|'e'|'i'|'o'|'u':
       print(f"{charactor_sentence} : {set_of_sentence[charactor_sentence]}")
