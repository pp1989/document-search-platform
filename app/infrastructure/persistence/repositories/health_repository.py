from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


class HealthRepository:
    def __init__(self, db: AsyncSession):
        self.db = db  # This is the AsyncSession object!

    async def check_db_health(self) -> str:
        try:
            # Execute a simple query to verify the database connection works
            # Remember to ALWAYS await self.db methods
            result = await self.db.execute(text("SELECT 1"))

            # Extract the actual value from the result object
            value = result.scalar()

            if value == 1:
                return "connected"
            return "unexpected response"
        except Exception as e:
            return f"disconnected: {str(e)}"
