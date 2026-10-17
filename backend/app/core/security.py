from datetime import datetime, timedelta, timezone
from typing import Optional

# Minimal placeholder; real auth can be added later
class DemoAuth:
    @staticmethod
    def get_demo_user() -> dict:
        return {"id": "demo-student-1", "role": "student", "name": "Demo Student"}
