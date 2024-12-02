from transformers import pipeline

# Load the model explicitly
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
sentiment_model = pipeline('sentiment-analysis', model=model_name)

# Text to analyze
text = "The company has shown exceptional growth this quarter."
result = sentiment_model(text)
print(result)
