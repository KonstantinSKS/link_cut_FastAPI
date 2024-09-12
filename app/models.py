from sqlalchemy import Column, Integer, String

from .db import Base


class URLMap(Base):
    """URL model for DB."""

    __tablename__ = "urls"

    id = Column(Integer, primary_key=True)
    original_url = Column(String)
    short_url = Column(String)
