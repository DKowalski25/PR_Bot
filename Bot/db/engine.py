from typing import Union

from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


def create_engine(url: Union[URL, str]) -> AsyncEngine:
    """The function creates an engin."""
    return create_async_engine(
        url=url,
        echo=True,
        pool_pre_ping=True
    )


async def proceed_schemas(engin: AsyncEngine, metadata) -> None:
    """The function creates schemas in Date Base."""
    async with engin.begin() as conn:
        conn.run_sync(metadata.create_all)


def get_session_maker(engine: AsyncEngine) -> sessionmaker:
    """The function creates a sessionmaker."""
    return sessionmaker(engine, class_=AsyncSession)
