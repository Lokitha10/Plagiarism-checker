# 📄 Plagiarism Detection System

A web-based **Plagiarism Detection System** built using **Python**, **Flask**, and **Scikit-learn**. The application allows users to upload two text files, compares their content using **TF-IDF Vectorization** and **Cosine Similarity**, and displays the similarity percentage.

---
## 🌐 Live Demo

🔗 **Hosted Application:** (https://plagiarism-checker-15wk.onrender.com)

> **Note:** This application currently supports **.txt** files only.

## 🚀 Features

- 📂 Upload two text files (.txt)
- 📊 Calculate similarity percentage
- ⚡ Uses TF-IDF Vectorization
- 📐 Uses Cosine Similarity algorithm
- 🌐 User-friendly Flask web interface
- 🎯 Displays plagiarism percentage instantly

---

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- HTML5
- CSS3

---

## 📂 Project Structure

```
PlagiarismChecker/
│
├── app.py
├── requirements.txt
├── README.md
│
├── uploads/
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── venv/
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Lokitha10/Plagiarism-checker-Python-master.git
```

### 2. Navigate to the Project

```bash
cd Plagiarism-checker-Python-master
```

### 3. Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate the virtual environment

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 📝 How It Works

1. Upload two text files.
2. The application reads both files.
3. Text is converted into numerical vectors using **TF-IDF**.
4. Cosine Similarity is calculated between the vectors.
5. The similarity percentage is displayed on the webpage.

---

## 🔄 Project Workflow

```
Upload Two Text Files
          │
          ▼
Read File Contents
          │
          ▼
TF-IDF Vectorization
          │
          ▼
Cosine Similarity
          │
          ▼
Calculate Similarity
          │
          ▼
Display Result
```

---

## 📊 Sample Output

| File 1 | File 2 | Similarity |
|---------|---------|------------|
| john.txt | juma.txt | 57.13% |
| john.txt | fatma.txt | 16.22% |

---

## 💡 Future Enhancements

- Support PDF and DOCX files
- Highlight matching sentences
- User Authentication
- Upload multiple files
- Download comparison reports
- Store comparison history
- Responsive Bootstrap UI

---

## 📷 Screenshots

### Home Page
<img width="1919" height="958" alt="image" src="https://github.com/user-attachments/assets/e4e17110-bfbe-4925-a057-e33224a4702a" />


### Result Page

<img width="1919" height="942" alt="image" src="https://github.com/user-attachments/assets/c806ec9a-d5ad-4d17-a23c-646d88761c62" />

---

## 👨‍💻 Author

**Lokitha**

- GitHub: https://github.com/Lokitha10
- LinkedIn: https://www.linkedin.com/in/thathireddylokitha/

---

## 📄 License

This project is developed for educational and learning purposes.
