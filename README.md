# House Prices Prediction API 🏠💰

**Version:** 0.1.0  
**Tech Stack:** Python, scikit-learn, FastAPI, Docker  

A complete **Machine Learning API** that predicts house prices based on input features. This project demonstrates **ETL, model training, API creation, containerization, and deployment**.

---

## 🚀 Features

- Predict house prices using a **Random Forest Regressor**.
- Built with **FastAPI** for an interactive API.
- Containerized with **Docker** for easy deployment.
- Ready for **live deployment** (tested on Render.com).
- Clean and professional for your GitHub portfolio.

---

## 🗂️ Project Structure

House_Prices_ML/

│

├── src/ # Python scripts

│ ├── etl.py # Data processing

│ ├── train.py # Model training

│ └── app.py # FastAPI server

│

├── model/ # Trained model (optional)

│ └── model.joblib

│

├── data/ # Dataset

│ └── raw/ # Original CSV files

│

├── requirements.txt # Python dependencies

├── Dockerfile # Docker image definition

├── .gitignore # Files/folders to ignore

└── README.md # This file

---

## ⚡ Setup Instructions

### **1. Clone the repository**

```bash
git clone https://github.com/afgsuna/house-prices-api.git
cd house-prices-api

2. Install dependencies

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

3. Run the API locally

uvicorn src.app:app --reload --port 8000
Access Swagger UI: http://127.0.0.1:8000/docs

Example POST /predict payload:
{
  "OverallQual": 7,
  "GrLivArea": 1500,
  "YearBuilt": 2005
}

4. Using Docker


Build the Docker image:

docker build -t house-prices-api .

Run the container:

docker run -p 8000:80 house-prices-api

Access API: http://localhost:8000/docs

5. Live API Example

Deployed on Render.com:

https://house-prices-api-latest.onrender.com
Test with curl:

curl -X POST "https://house-prices-api-latest.onrender.com/predict" \
-H "Content-Type: application/json" \
-d '{"OverallQual":7,"GrLivArea":1500,"YearBuilt":2005}'

Response:
{"predicted_price": 214567.89}

📈 Model Details

Algorithm: Random Forest Regressor
Features used:
OverallQual – Overall quality rating
GrLivArea – Above-ground living area (sq ft)
YearBuilt – Year built
Evaluation metric: RMSE (Root Mean Squared Error)

🧰 Tools & Libraries
Python 3.9+
scikit-learn
pandas, numpy
FastAPI, Uvicorn
Docker

💡 Notes
.venv/, __pycache__/, large model/data files are ignored via .gitignore.

Free Render deployment may spin down after inactivity.

API can be extended to include more dataset features.

👨‍💻 Author / Portfolio:

Sasan Mousavi

https://afgsuna.github.io/Sacccan/
https://github.com/afgsuna
https://www.linkedin.com/feed/




Demonstrates ETL, ML modeling, API development, containerization, and deployment skills.
