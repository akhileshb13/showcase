import json
from difflib import get_close_matches

data = json.load(open("data.json"))                   # Load the json file containing the dictionary

def translate(w):
    w = w.lower()                                     # Convert the input word to lower case to match with data in json file
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:  # Use getclosematches to provide suggestions
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0]) # Display similar suggestions
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
output = translate(word)
if type(output) == list:                               # If there are multiple meanings to a single word, display all the meanings
    for item in output:
        print(item)
else:
    print(output)
