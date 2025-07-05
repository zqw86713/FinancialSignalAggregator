from pydantic import BaseModel
from typing import List, Optional

class SignalRequest(BaseModel):
    symbols: List[str]
    include_volume: Optional[bool] = False
