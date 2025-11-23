import uvicorn # type: ignore
import logging
import uuid
from fastapi import FastAPI, Request # type: ignore
from prometheus_fastapi_instrumentator import Instrumentator # type: ignore

# Configure logging
# This will print logs in a structured way
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI()

# --- Observability: Tracing ---
# Middleware to add a unique trace ID to every request
@app.middleware("http")
async def add_trace_id(request: Request, call_next):
    # Generate a unique trace ID
    trace_id = str(uuid.uuid4())
    request.state.trace_id = trace_id

    # --- Observability: Logging ---
    # Log the incoming request with the trace ID
    logger.info(
        f"request received: method={request.method} "
        f"path={request.url.path} trace_id={trace_id}"
    )

    response = await call_next(request)

    # Add the trace ID to the response headers
    response.headers["X-Trace-ID"] = trace_id
    logger.info(
        f"request completed: status_code={response.status_code} "
        f"trace_id={trace_id}"
    )

    return response


# --- Observability: Metrics ---
@app.on_event("startup")
async def startup():
    Instrumentator().expose(app)

@app.get("/")
async def read_root(request: Request):
    # You can access the trace ID in your endpoints
    trace_id = request.state.trace_id
    return {"message": "Hello, DevOps World!", "trace_id": trace_id}


@app.get("/health")
async def health_check(request: Request):
    trace_id = request.state.trace_id
    return {"status": "ok", "trace_id": trace_id}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
