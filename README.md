# gherkinized-api 🚀

A simple Flask-based API built with Behavior-Driven Development (BDD) using **Gherkin + Behave**, containerized using **Docker**, and tested with **GitHub Actions** CI/CD.

---

## 🧠 Project Features

- ✅ Flask REST API (`/tasks`)
- ✅ BDD tests using Gherkin + Behave
- ✅ Dockerfile for containerized execution
- ✅ CI pipeline with GitHub Actions
- ✅ Clean, testable DevOps-friendly architecture

---

## 🛠️ Setup Instructions

### 1. Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/Scripts/activate  # Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧪 Run BDD Tests Locally

Make sure your Flask app is running:

```bash
python app/main.py
```

Then in a separate terminal:

```bash
behave
```

---

## 🐳 Run with Docker

### 1. Build the Docker image:

```bash
docker build -t gherkinized-api .
```

### 2. Run the container:

```bash
docker run -p 5000:5000 gherkinized-api
```

Then test in your browser or terminal:

```bash
curl http://localhost:5000/tasks
```

---

## 🔁 Continuous Integration (CI)

Every push to `main` triggers:

- ✅ Python environment setup
- ✅ Dependencies install
- ✅ Automated `behave` test execution

See it in the [Actions tab](https://github.com/bhatshalesh/gherkinized-api/actions)

---

## 📦 To-Do / Next Steps

- [ ] Add `docker-compose.yml`
- [ ] Deploy to Heroku / Render / Railway
- [ ] Add database (SQLite or PostgreSQL)
- [ ] Add CI badge to this README

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
