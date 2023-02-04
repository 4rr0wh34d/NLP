# *******     Task 38            *******
# *******  Compulsory task 1     *******
# *******   semantic.py          *******
# ------------- xxx -------------------


# The following program is the collection of code snippets to compare the similarity of different things.

# importing the spacy module
import spacy

# Loading the spacy model into a variable nlp
nlp = spacy.load("en_core_web_md")

# passing the input to spacy model variable
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# Using similarity method to print out the similarity
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


# Here the cat and the monkey seems to be much similar then other combination as they are both mammals. The
# similarity between the monkey and banana is quite high as monkey tends to love banana which is not the same
# in the case of cat where the similarity is very low.
# Some more examples would be the high similarity between lion and leopard as they are both from the family of cat
# and low similarity between lion and carrot as lion are carnivores.

tokens = nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Here apple and banana seems to be the most similar items as they are both fruits while, apple and cat seems to be
# the least similar.

sentence_to_compare = "Why is my cat on the car"

sentences = ["Where did my dog go",
             "Hello, there is my car",
             "I've lost my car in my car",
             "I'd like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


# When you try to run the example.py with normal model 'en_core_web_sm' similarity will be based on tagger,
# parser and NER as the model does not include word vector and the similarity between two different complaints
# or two different recipes or even between recipes and complaints is less in compare to using the 'en_core_web_md' model
# as the model don't seem to distinguish properly. So the true similarity is not reflected when using the normal model.
