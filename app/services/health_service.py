from datetime import datetime, timezone

class HealthService:

    async def get_status(self):

        return {
            "status": "healthy",
            "time": datetime.now(timezone.utc),
            "service": "Document Search Platform",
        }