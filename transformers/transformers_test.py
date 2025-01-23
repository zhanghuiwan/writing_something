from transformers import pipeline

classifier = pipeline("sentiment-analysis")
print(classifier("I've been waiting for a HuggingFace course my whole life."))
# [{'label': 'POSITIVE', 'score': 0.9598049521446228}]