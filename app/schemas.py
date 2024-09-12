from pydantic import BaseModel, AnyHttpUrl


class URLCreate(BaseModel):
    """Schema for create URL."""
    original_url: AnyHttpUrl


class URLDB(URLCreate):
    """Schema for response from DB using ORM."""
    id: int
    short_url: str

    class Config:
        from_attributes = True
