# 📚 Library Management System – DevOps Project

## 📌 Project Overview
This project is a simple **Library Management System** built using **Flask** and implemented with a complete **DevOps workflow**. It demonstrates version control, containerization, CI/CD automation, and infrastructure as code (IaC).

---
## 🏗️ Architecture

User → Flask Application → Docker Container → GitHub Repository → GitHub Actions CI/CD → Terraform (IaC Simulation)

---

## 🚀 Features

- Add books to library system  
- View list of books  
- Simple REST API endpoint  
- Docker containerization  
- CI/CD automation using GitHub Actions  
- Infrastructure simulation using Terraform  

---

## 🛠️ Technologies Used

- Python (Flask)  
- HTML / CSS  
- Git & GitHub  
- Docker  
- GitHub Actions (CI/CD)  
- Terraform  

---

## 📂 Project Structure


library-devops-project/
├── app.py
├── requirements.txt
├── Dockerfile
├── terraform/
│ └── main.tf
├── templates/
│ └── index.html
├── static/
│ └── style.css
└── .github/
└── workflows/
└── ci.yml

---

## ▶️ How to Run Locally

### 1. Clone repository
```bash
git clone https://github.com/Nadia1222/Library---DevOps---Final-Project.git
cd Library---DevOps---Final-Project
2. Install dependencies
pip install -r requirements.txt
3. Run Flask app
python app.py

Open:

http://localhost:5000
🐳 Run with Docker
Build image
docker build -t library-app .
Run container
docker run -p 5000:5000 library-app
⚙️ CI/CD Pipeline (GitHub Actions)

This project uses GitHub Actions to automate:

Dependency installation
Build verification
Docker image build
Workflow file:
.github/workflows/ci.yml
🏗️ Infrastructure as Code (Terraform)

Terraform is used to simulate infrastructure setup locally.

What it does:
Creates a local file resource
Demonstrates Infrastructure as Code (IaC)
Run commands:
cd terraform
terraform init
terraform apply
📸 Screenshots
Flask application running
Docker container running
GitHub Actions pipeline success
Terraform output
🧠 Challenges Faced
Docker networking issues
Git authentication
Terraform configuration errors
CI/CD pipeline debugging
🎯 Learning Outcomes
DevOps lifecycle understanding
Docker containerization
CI/CD automation
Terraform basics
Git version control
🏁 Conclusion
This project demonstrates a complete DevOps workflow from development to deployment using modern tools and practices.

👨‍💻 Author
GitHub: Nadia1222
