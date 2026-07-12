import os
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def calculate_similarity(text1, text2):
    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform([text1, text2])

    similarity = cosine_similarity(vectors)[0][1]

    return round(similarity * 100, 2)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/compare", methods=["POST"])
def compare():

    file1 = request.files["file1"]
    file2 = request.files["file2"]

    text1 = file1.read().decode("utf-8")
    text2 = file2.read().decode("utf-8")

    similarity = calculate_similarity(text1, text2)

    return render_template(
        "index.html",
        similarity=similarity
    )


if __name__ == "__main__":
    app.run(debug=True)