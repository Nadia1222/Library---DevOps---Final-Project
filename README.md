Library Management System – DevOps Project Report 

Project Overview:
My Project name is Library Management System which is a sample web based application.  The tool used to develop this application is flask associated with complete DevOps work flow. The project represent the most significant DevOps concepts like version control continues integration, continues deployment (CI/CD), infrastructure as a code and containerization. 
The application allow user to add book and view the list of the books inside the library via a sample and user friendly interface. The project is designed to simulate a real world environment by using several modern technologies and tools. 
Architecture: 
I Use below applications:
-	Flask Application 
-	Docker Container 
-	GitHub Repository 
-	GitHub Actions CI/CD
-	Terraform (IaC Simulation)
Features
- Add books to library system  
- View list of books  
- Simple REST API endpoint  
- Docker containerization  
- Automated CI/CD pipeline using GitHub Actions  
- Infrastructure simulation using Terraform  

Technologies Used

- Python (Flask)  
- HTML / CSS  
- Git & GitHub  
- Docker  
- GitHub Actions (CI/CD)  
- Terraform  
Project Structure
library-devops-project
├── app.py
├── requirements.txt
├── Dockerfile
├── terraform/
│   └── main.tf
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── .github/
    └── workflows/
        └── ci.yml
Application Development
Flask structure in Python was used to develop using the project. As long as Flask is simple, lightweight, and appropriate for minor web applications was used to develop the project. 
The project includes:
•	A homepage interface 
•	A form to add books 
•	A book listing feature 
•	A simple API endpoint for retrieving data 
I used HTML and CSS to produce a clean and simple user interface.
Version Control Using GitHub
GitHub and Git were used for better version control and project management. The repository stores all project files and tracks changes during development.
GitHub Repository:
Library DevOps Final Project Repository
Benefits of using GitHub:
-	Source code management
-	Collaboration support
-	Version tracking
-	Integration with GitHub Actions
Docker Containerization
Docker in the project was used to containerize the Flask application. Containerization guarantees the application runs reliably through different environments.
The Dockerfile Functions:
-	Uses a Python base image
-	Copies application files
-	Installs dependencies
-	Run the Flask application 
Docker Commands: 
Build Docker Image
-	docker build -t library-app .
Run Docker Container
-	docker run -p 5000:5000 library-app
The application becomes accessible at:
-	http://localhost:5000
CI/CD Pipeline Using GitHub Actions
GitHub Actions was used to implement the CI/CD workflow.
CI/CD Workflow, the pipeline automatically:
-	Installs project dependencies
-	Verifies application build
-	Builds Docker image
-	Checks for workflow success
-	Workflow file location:
-	.github/workflows/ci.yml
This computerization progresses develop proficiency and decreases guidebook deployment tasks.
Infrastructure as Code. 
In the project Terraform was used to simulate Infrastructure as Code (IaC). Even though the project does not use cloud infrastructure, Terraform determines how infrastructure can be accomplished through code.
Terraform Functions
Builds a local file resource, simulates infrastructure provisioning Establishes basic Terraform workflow
Terraform Commands: 
-	cd terraform
-	terraform init
-	terraform apply
How to Run The project Locally
1. Clone repository
``bash git clone https://github.com/Nadia1222/Library---DevOps---Final-Project.git
cd Library---DevOps---Final-Project
2. Install dependencies
pip install -r requirements.txt
3. Run Flask app
python app.py
Open in browser : http://localhost:5000
Screenshots
The following screenshots are included at the end of the report:
-	Flask application running
-	Docker container running
-	GitHub Actions successful pipeline
-	Terraform apply output
Challenges Faced
During the project running I have faced to several technical challenges. 
-	Docker 
The application firstly failed to connect correctly by Docker because the port configuration was not correct. This problem was fixed by plotting the container port properly.
-	GitHub
GitHub authentication errors happened during pushing code to GitHub. The problem was fixed by  using updated GitHub authentication techniques and repository permissions.
-	Terraform 
During the project running some Terraform commands failed due to syntax and configuration errors. This problem was resolved by fixing the Terraform configuration file.
-	CI/CD Pipeline 
In the project the GitHub Actions workflow required several fixing attempts before successfully running all phases automatically.
These challenges developed my troubleshooting skills and delivered practical DevOps practice.
Learning Outcomes:
This project helped me to develop the most important technical and practical skill associated to DevOps engineering and software development.
Skills Learned:
-	Flask web application development
-	Docker containerization
-	Git and GitHub version control
-	CI/CD automation using GitHub Actions
-	Terraform basics and Infrastructure as Code
-	DevOps workflow understanding
-	Debugging and troubleshooting
Besides, this project also developed my understanding of how software utilization processes work and how automation techniques functions in a professional development environment. 
Conclusion
My project the Library management system has been successfully run and shows the implementation of complete DevOps work flow using technologies such as Docker, Flask, Local host, Python GitHub platform, and terraform which integrate and provided a significant experience in my software development journey like automation and deployment of these tools. 
My project achieved its goal by successfully developing functional web application and performing the important DevOps concepts like containerization, CI/CD automation infrastructure as a code. In all, this project developed my knowledge of DevOps and provided hands on experience with the tools and technologies that are mostly used in cloud based environment and software engineering field.  
Author
GitHub: Nadia1222
