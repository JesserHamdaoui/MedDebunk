import requests

API_URL = "https://api-inference.huggingface.co/models/dstefa/roberta-base_topic_classification_nyt_news"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	