from typing import Optional
from pydantic import BaseModel


class FtTokenMetadata(BaseModel):
    spec: str
    name: str
    symbol: str
    icon: Optional[str] = None
    reference: Optional[str] = None
    reference_hash: Optional[str] = None
    decimals: int
