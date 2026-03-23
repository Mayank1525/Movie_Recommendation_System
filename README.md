# 🎬 MayoFlix: Intelligent Movie Recommendation System

MayoFlix is a machine learning–driven movie recommendation system designed to deliver personalized movie suggestions based on content similarity. The system leverages **vector similarity metrics** to identify and recommend movies aligned with user preferences.

---

## 🚀 Key Features

* Content-based movie recommendation engine
* Similarity computation using **cosine similarity**
* Efficient data preprocessing and feature engineering
* Interactive web interface powered by **Streamlit**
* Real-time movie poster rendering using external data sources

---

## 🛠️ Technology Stack

* **Programming Language:** Python
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-learn
* **Frontend / UI:** Streamlit
* **Core Techniques:** Feature Vectorization, Similarity Analysis

---

## 📂 Repository Structure

MayoFlix/
│
├── app.py                      # Streamlit application entry point
├── movie_dict.pkl              # Processed movie dataset
├── similarity_small.pkl        # Precomputed similarity matrix
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation

---

## ⚙️ System Workflow

1. Raw movie metadata is processed and transformed using NLP techniques
2. Relevant attributes (genres, keywords, cast, crew) are consolidated into a unified feature space
3. Textual data is vectorized using **CountVectorizer**
4. Pairwise similarity scores are computed using **cosine similarity**
5. The system retrieves and displays the top relevant movie recommendations

---

## ▶️ Local Setup & Execution

### 1. Clone the Repository

git clone https://github.com/Mayank1525/mayoflix.git
cd mayoflix

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Launch the Application

streamlit run app.py

---

## 📊 Future Scope

* Integration of collaborative filtering techniques
* Hybrid recommendation system (content + user behavior)
* Model optimization using deep learning approaches
* Cloud deployment and scalability enhancements
* User profiling and personalization features

---

## 🙌 Acknowledgements

* Open-source machine learning ecosystem (Scikit-learn, Pandas)
* Public movie datasets and APIs for metadata enrichment

---

## 👤 Author

**Mayank Vishwakarma**
Aspiring Software Engineer | Machine Learning Enthusiast

---

## 📌 Note

This project is intended for educational and demonstration purposes, showcasing the practical implementation of recommendation system algorithms using real-world datasets.

---

⭐ If you find this project insightful, consider starring the repository.
