name: Docker CI/CD - Build, Push & Run Container

on:
  push:
    branches: ["main"]

jobs:
  build_push_run:
    runs-on: ubuntu-latest

    steps:
      # 1. Checkout source code
      - name: Checkout code
        uses: actions/checkout@v4

      # 2. Login to Docker Hub
      - name: Login to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      # 3. Build Docker image
      - name: Build Docker Image
        run: |
          docker build -t ${{ secrets.DOCKER_USERNAME }}/flask-app:latest ./app

      # 4. Push image to Docker Hub
      - name: Push Docker Image
        run: |
          docker push ${{ secrets.DOCKER_USERNAME }}/flask-app:latest

      # 5. Run the image as a container inside GitHub Actions
      - name: Run Docker Container
        run: |
          docker run -d --name flaskapp -p 8080:8080 ${{ secrets.DOCKER_USERNAME }}/flask-app:latest
          sleep 5  # give the container time to start

      # 6. Test the running Flask app using curl
      - name: Test Flask App
        run: |
          curl --retry 5 --retry-delay 2 --fail http://localhost:8080

