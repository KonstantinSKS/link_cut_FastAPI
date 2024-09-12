from http import HTTPStatus
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession

from .db import get_async_session
from .schemas import URLCreate, URLDB
from .crud import create_short_url, get_original_url


router = APIRouter()


@router.post('/', response_model=URLDB, status_code=HTTPStatus.CREATED)
async def shorten_url(
    url_item: URLCreate, session: AsyncSession = Depends(get_async_session)
):
    """Endpoint for creation short URL."""
    short_url_data = await create_short_url(session, url_item)
    return short_url_data


@router.get('/{short_url_id}',
            response_class=RedirectResponse,
            status_code=HTTPStatus.TEMPORARY_REDIRECT)
async def redirect_to_original(
    short_url_id: str, session: AsyncSession = Depends(get_async_session)
):
    """Endpoint to get original URL and redirect to the adress."""
    url_item = await get_original_url(session, short_url_id=short_url_id)
    if url_item:
        return RedirectResponse(
            url=url_item.original_url,
            status_code=HTTPStatus.TEMPORARY_REDIRECT
        )
    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND, detail='URL not found'
    )
