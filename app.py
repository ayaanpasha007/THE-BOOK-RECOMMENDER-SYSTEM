
from flask import Flask, render_template, request
from model import load_model, recommend

app = Flask(__name__)

pt, similarity, books = load_model()

@app.route("/")
def index():
    book_list = list(pt.index[:50])
    return render_template("index.html", books=book_list)

@app.route("/recommend", methods=["POST"])
def recommend_books():
    book = request.form.get("book")
    recs = recommend(book, pt, similarity, books)
    return render_template("recommend.html", recs=recs)

if __name__ == "__main__":
    app.run(debug=True)
