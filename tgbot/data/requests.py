from sqlalchemy import select

from tgbot.data import models_sql


async def get_keyboard():
    async with models_sql.async_session() as session:
        result = await session.execute(select(models_sql.Keyboard))
        keyboards = result.scalars().all()
        return keyboards