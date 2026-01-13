# DevOps Project:

A simple FastAPI service built to demonstrate end-to-end DevOps practices, including CI/CD, containerization, Kubernetes deployment, security, and observability.

---

## Features

* REST API with `/` and `/health` endpoints.
* **Observability:** Exposes a `/metrics` endpoint for Prometheus.
* **Observability:** Generates structured JSON logs with a unique `trace_id` for every request.
* **Security:** CI pipeline includes SAST (CodeQL) scans.

## Tech Stack

* **Language:** Python 3.11
* **Framework:** FastAPI
* **Container:** Docker
* **CI/CD:** GitHub Actions
* **Deployment:** Kubernetes (minikube)
* **Security:** GitHub CodeQL (SAST), OWASP ZAP (DAST)
* **Observability:** Prometheus, OpenTelemetry (tracing)

---

## How to Run Locally

### Prerequisites

* Python 3.11+
* Docker
* minikube
* kubectl

### 1. Local Python Environment (Optional)

```bash
# Clone the repo
git clone [YOUR_REPO_URL]
cd [YOUR_REPO_NAME]

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn main:app --reload
```

### 2. Running with Docker

```bash
# Build the Docker image
docker build -t my-app .

# Run the container
docker run -p 8000:8000 my-app
```
Access the app at `http://localhost:8000`.

### 3. Running on Kubernetes (minikube)

```bash
# 1. Start minikube
minikube start

# 2. Apply the Kubernetes manifests
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# 3. Wait for the pod to be "Running"
kubectl get pods

# 4. Access the service
minikube service my-fastapi-service
```

---

## API Endpoints

* `GET /`
    * **Description:** Returns a hello message and trace ID.
    * **Example Response:**
        ```json
        {
          "message": "Hello, DevOps World!",
          "trace_id": "a1b2c3d4-..."
        }
        ```
* `GET /health`
    * **Description:** A simple health check endpoint.
    * **Example Response:**
        ```json
        {
          "status": "ok",
          "trace_id": "e5f6g7h8-..."
        }
        ```
* `GET /metrics`
    * **Description:** Exposes all application metrics for Prometheus.

---

## Security

* **SAST:** Static analysis is performed by **CodeQL** on every pull request. Results can be seen in the "Security" tab.
* **DAST:** Dynamic analysis can be run locally against the `minikube` service using **OWASP ZAP**. (Include your `zap-report.html` or a screenshot).
