import spacy

nlp = spacy.load('en_core_web_sm')

garden_path_sentences = ["The old man the boat.",
                         "The complex houses married and single soldiers and their families.",
                         "The British left waffles on the Falkland Islands.",
                         "The cotton clothing is usually made of grows in the southern U.S.",
                         "Mary gave the child the dog bit a Band-Aid.",
                         "When Fred eats food gets thrown.",
                         "The cotton clothing is made of grows in Mississippi."]

# tokenize and perform Entity recognition for each of the sentences
for sentence in garden_path_sentences:
    words = nlp(sentence)
    print("\n" + sentence)
    # print pos for each token
    print([(token.orth_, token.pos_) for token in words if not token.is_punct | token.is_space])

    # print Entities if found
    if len(words.ents) > 0:
        print([(i, i.label_, i.label) for i in words.ents])

# @ Task 4. At the bottom of your file, write a comment about two unusual entities
#           you found that spaCy gave one of the words of your sentences - did you expect this?
# It is quite difficult to find garden-path sentences that have many entities let alone 'unusual' ones.
# So unless I am missing something there is nothing unexpected in the output provided by spaCy.
