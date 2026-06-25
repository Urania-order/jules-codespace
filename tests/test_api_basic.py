import httpx
import time
import subprocess
import os

def test_api():
    # Start server in background
    proc = subprocess.Popen(
        ["uvicorn", "smos.api.main:app", "--host", "127.0.0.1", "--port", "8000"],
        env=dict(os.environ, PYTHONPATH=".")
    )
    time.sleep(3) # Wait for server to start

    try:
        # 1. Root
        response = httpx.get("http://127.0.0.1:8000/")
        print(f"Root: {response.json()}")
        assert response.status_code == 200

        # 2. Create Event
        # First ensure a user exists
        from smos.core.database import SessionLocal
        from smos.models.models import User
        db = SessionLocal()
        user = db.query(User).first()
        if not user:
            user = User(display_name="Test User")
            db.add(user)
            db.commit()
            db.refresh(user)
        user_id = user.id
        db.close()

        event_data = {
            "user_id": user_id,
            "type": "clipboard",
            "content": {"text": "Hello Co-SMOS"}
        }
        response = httpx.post("http://127.0.0.1:8000/event", json=event_data)
        print(f"Create Event: {response.json()}")
        assert response.status_code == 200
        assert response.json()["type"] == "clipboard"

    finally:
        proc.terminate()

if __name__ == "__main__":
    test_api()
