def get_num_words(bookString):
    wordArray = bookString.split()
    num_words = len(wordArray)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

def get_letter_array(bookString):
    wordArray = bookString.split()
    letter_dict = {}

    for word in wordArray:
        word = word.lower()
        for char in word:
            if (not char.isalpha()):
                continue

            if char not in letter_dict:
                letter_dict[char] = 1
            else:
                letter_dict[char] += 1
    
    return letter_dict

def sort_on(dict):
    return dict["count"]


def sort_letter_dict(letterDict):
    countList = []
    
    for key, value in letterDict.items():
        countList.append({
            "letter":key,
            "count":value
        })

    countList = sorted(countList, key=lambda x: x['count'], reverse=True) 

    print("--------- Character Count -------")
    for wordDict in countList:
        print(f"{wordDict['letter']}: {wordDict['count']}")