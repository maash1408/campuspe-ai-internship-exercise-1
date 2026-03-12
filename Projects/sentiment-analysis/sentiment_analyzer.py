"""
Sentiment Analysis using Transformer
"""

from transformers import pipeline

#Loading Pretrained sentiment analysis model
classifier = pipeline('sentiment-analysis')

#Test
texts = [
    "I love Gen AI",
    "My Mentor sucks",
    "Eh it's okay"
]

for text in texts:
    result = classifier(text)[0]
    print(f"{text}")
    print(f" ->{result['label']}: {result['score']:.2%}\n")