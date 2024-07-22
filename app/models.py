from pydantic import BaseModel
from typing import Optional

class TextRequest(BaseModel):
    text: str
    max_length: Optional[int] = 100
