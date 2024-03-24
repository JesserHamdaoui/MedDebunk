from flask import Flask, request, jsonify
import requests
from tools.healthcare_sentence_data import get_sentence_data
from tools.sentence_segmentation import split_into_sentences
from tools.topic_classification import get_topic_certainty

app = Flask(__name__)

@app.route("/topic", methods=["GET"])
def topic_certainty():
    sentence = request.args.get('sentence')
    response = get_topic_certainty(sentence)
    return jsonify(response)


@app.route("/split_sentences", methods=["GET"])
def split_sentences():
    paragraph = request.args.get('paragraph')
    sentences = split_into_sentences(paragraph)
    return jsonify(sentences)


@app.route("/data", methods=["GET"])
def get_data():
    statement = request.args.get('statement')
    output = get_sentence_data(statement)
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)