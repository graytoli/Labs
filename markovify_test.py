import markovify

with open("/Desktop/bible.txt") as f:
    text = f.read()

text_model = markovify.Text(text)

for i in range(5):
    print(text_model.make_short_sentence(140))
