from string import ascii_letters, digits
from random import choices

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import URLMap

RANDOM_CHARACTERS = 6


async def get_unique_short_id(session: AsyncSession) -> str:
    """The function of converting a long link into a short one
    by random method."""
    while True:
        short_id = ''.join(
            choices(ascii_letters + digits, k=RANDOM_CHARACTERS))
        result = await session.execute(
            select(URLMap).filter_by(short_url=short_id))
        if not result.scalars().first():
            return short_id
