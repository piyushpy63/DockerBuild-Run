🚀 Python App with Docker CI/CD Using GitHub Actions

This repository contains a simple Python application packaged with Docker and fully automated using GitHub Actions CI/CD.
Whenever code is pushed to the repository, GitHub Actions automatically:

1. Builds a Docker image
2. Runs the container for testing
3. Pushes the image to Docker Hub

├── .github/
│   └── workflows/
│       └── docker-ci.yml        # GitHub Actions CI/CD pipeline
│
├── app/                          # Application folder
│   ├── app.py                    # Python app source code
│   └── requirements.txt          # Python dependencies│
├── Dockerfile                    # Docker image build file
└── README.md

GitHub Actions executes workflow
1. Checks out repository
2. Builds Docker image
3. Logs into Docker Hub
4. Tags image
5. Pushes to Docker Hub


GitHub Secrets : stores sensitive credentials
Secret Name	        Purpose
DOCKERHUB_USERNAME	Your Docker Hub username
DOCKERHUB_TOKEN	    Docker Hub access token (or password)
