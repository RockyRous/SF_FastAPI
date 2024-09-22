from pydantic import BaseModel


class SnippetCreate(BaseModel):
    title: str
    content: str

class SnippetRead(BaseModel):
    id: int
    title: str
    content: str
    owner_id: int

    class Config:
        orm_mode = True
