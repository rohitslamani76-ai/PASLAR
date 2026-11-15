Proactive AI companion for a safer independent living.
README.md – Quick‑start guide

  # PASLAR Daily Life Assistant – FastAPI + AWS CDK + React UI

  ## Prerequisites
  - Python 3.11+ (recommended)
  - Node 20+ (for the front‑end)
  - AWS credentials configured (`aws configure`) – required for CDK
  - VS Code (or any IDE)

  ## 1️⃣ Set up the Python back‑end

  ```bash
  cd daily_life_assistant
  python -m venv .venv
  source .venv/bin/activate   # Windows: .venv\Scripts\activate.bat
  pip install -r requirements.txt

  Run the API locally:

  uvicorn app.main:app --reload
  # → http://127.0.0.1:8000/docs shows the Swagger UI

  2️⃣ (Optional) Spin up the AWS infra with CDK

  cd infra
  python -m venv .venv && source .venv/bin/activate
  pip install -r requirements.txt
  cdk synth          # preview CloudFormation
  cdk deploy         # creates resources in your AWS account

  The stack creates:
  - Cognito User Pool (for UI auth)
  - S3 bucket with a 12‑minute lifecycle rule
  - Lambda that runs the FastAPI app
  - HTTP API Gateway exposing /api/*

  3️⃣ (Optional) Launch the React UI

  cd ../frontend
  npm install
  npm run dev        # → http://localhost:5173

  The UI currently contains placeholder pages that call the API endpoints (still 501).
  Replace the placeholder calls with real fetch requests once the back‑end logic is ready.

  4️⃣ Run tests

  cd ../tests
  pytest -vv

  All tests should pass (they only verify that the stub endpoints return 501).

  Next Steps

  - Implement the voice pipeline (app/services/voice.py) – hook up Transcribe → Bedrock → Polly.
  - Add safety checks (app/utils/safety.py) to all endpoints.
  - Flesh out business services in app/services/*.py.
  - Extend the CDK stack: add EventBridge rule for medication reminders, IAM policies for Bedrock/Transcribe/Polly, etc.
  - Build the UI screens using the shadcn/ui components you already have.