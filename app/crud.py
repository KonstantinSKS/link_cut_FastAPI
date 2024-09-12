from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import URLMap
from .schemas import URLCreate
from .utils import get_unique_short_id


async def create_short_url(
        session: AsyncSession,
        url_item: URLCreate
) -> URLMap:
    """Create short URL."""
    original_url = url_item.original_url
    short_id = await get_unique_short_id(session)
    short_url = f'{short_id}'
    short_url_data = URLMap(
        original_url=str(original_url),
        short_url=str(short_url),
    )

    session.add(short_url_data)
    await session.commit()
    await session.refresh(short_url_data)
    return short_url_data


async def get_original_url(
        session: AsyncSession,
        short_url_id: str) -> URLMap:
    """Get original URL."""
    result = await session.execute(
        select(URLMap).where(URLMap.short_url == f"{short_url_id}"))
    return result.scalars().first()
