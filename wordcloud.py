import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# Example data
responses = [
    "The courses were excellent and very informative.",
    "I didn't like the courses; they were too difficult.",
    "The courses were okay, but there is room for improvement.",
    # ... add more responses
]
"Quels enseignements, présents dans votre formation, vous paraissent inutiles ?"
# Create a DataFrame
df = pd.DataFrame({'responses': responses})

# Tokenize the text
df['tokenized'] = df['responses'].apply(word_tokenize)

# Calculate word frequency
all_words = [word for tokens in df['tokenized'] for word in tokens]
fdist = FreqDist(all_words)

# Create a bar chart of word frequency
fdist.plot(30, cumulative=False)
plt.show()

# Create a word cloud
wordcloud = WordCloud(width=800, height=400, random_state=21, max_font_size=110).generate_from_frequencies(fdist)
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis('off')
plt.show()
