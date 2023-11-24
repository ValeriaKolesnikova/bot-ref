from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncAttrs, create_async_engine
from sqlalchemy.orm import relationship, Mapped, DeclarativeBase, mapped_column

from tgbot.config import SQLALCHEMY_URL


engine = create_async_engine(SQLALCHEMY_URL)

async_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Keyboard(Base):
    __tablename__ = 'keyboard'

    id: Mapped[str] = mapped_column(primary_key=True)
    level: Mapped[str] = mapped_column()
    button_name: Mapped[str] = mapped_column()
    template_name: Mapped[str] = mapped_column()


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
