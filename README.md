# 📚 Book Recommender System

A Machine Learning-powered Book Recommender System that suggests similar books based on user rating patterns using Collaborative Filtering and Cosine Similarity.

## 🚀 Project Overview

This application helps users discover books similar to their interests by analyzing historical user ratings and identifying relationships between books.

The recommendation engine uses Collaborative Filtering techniques to generate personalized suggestions from a large collection of books.

---

## 🎯 Features

- Book Recommendation Engine
- Collaborative Filtering
- Cosine Similarity-Based Matching
- Flask Web Interface
- Dynamic Recommendation Generation
- Clean and User-Friendly Design

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Scikit-Learn

### Web Framework
- Flask

### Frontend
- HTML
- CSS

---

## 📂 Project Structure

```text
BOOK-RECOMMENDER-SYSTEM/
│
├── app.py
├── model.py
├── requirements.txt
│
├── dataset/
│   ├── Books.csv
│   ├── Ratings.csv
│   └── Users.csv
│
├── templates/
│   ├── index.html
│   └── recommend.html
│
├── screenshots/
│   ├── home-page.png
│   └── recommendations.png
│
├── README.md
└── LICENSE
```

## ⚙️ Working Process

### Step 1: Data Loading

The system loads:

- Books Dataset
- Ratings Dataset
- Users Dataset

### Step 2: Data Filtering

Only:

- Active users with more than 200 ratings
- Books with more than 50 ratings

are considered.

### Step 3: Pivot Table Creation

A User-Book Matrix is generated where:

Rows = Books

Columns = Users

Values = Ratings

### Step 4: Similarity Calculation

Cosine Similarity is applied to identify books with similar rating patterns.

### Step 5: Recommendation Generation

When a user selects a book:

- Similar books are identified
- Top recommendations are returned

---

## 📊 Machine Learning Concepts Used

- Recommendation Systems
- Collaborative Filtering
- Similarity Measures
- Data Cleaning
- Feature Engineering

---

## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/book-recommender-system.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

## 📸 Screenshots

### Home Page

(Add screenshot)

### Recommendation Page

(Add screenshot)

---

## 📈 Future Enhancements

- Book Cover Display
- Author Information
- User Authentication
- Hybrid Recommendation System
- Deep Learning Recommendation Engine
- Streamlit Deployment
- Cloud Deployment

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

- Recommendation Systems
- Machine Learning Workflows
- Data Preprocessing
- Flask Development
- Model Integration
- User Interface Development

---

## 👨‍💻 Author

**Ayaan Pasha**

B.E. Artificial Intelligence & Machine Learning

Aspiring Data Analyst | Machine Learning Engineer

### Connect With Me

- LinkedIn: https://www.linkedin.com/in/ayaan-pasha-6278bb29b/
- GitHub: https://github.com/ayaanpasha007/THE-BOOK-RECOMMENDER-SYSTEM/new/main?filename=README.md

---

⭐ If you found this project useful, please consider starring the repository.
