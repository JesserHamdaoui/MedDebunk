import requests
from dotenv import load_dotenv
import os

load_dotenv()

inference_token = os.getenv("INFERENCE_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/dstefa/roberta-base_topic_classification_nyt_news"
headers = {"Authorization": "Bearer {inference_token}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	