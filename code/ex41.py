import random
from urllib.request import urlopen
import sys
WORD_URL = "http://learncodethehardway.org/words.txt"

WORDS = []

PHPASES = {
    "class %%%(%%):":
        "Make a class named %% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "set *** to an instance of class %%%.",
    "***.***(@@@)": 
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."        
}
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip(),encodeing="utf-8")

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
    random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.cout("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))
    for word in other_names:
        result = result.replace("***",word,1)

    for word in param_names:
        result = result.replace("@@@",word,1)

    results.append(result)

    return results

try:
    while True:
        snippets = list(PHRASES.keys())
        randon.shuffle(snippetss)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer= convert(snippet, phrase)

            print(question)

            input(">")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")