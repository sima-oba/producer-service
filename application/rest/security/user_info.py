from dataclasses import dataclass
from typing import List, Optional


@dataclass
class UserInfo:
    id: str
    username: str
    doc: Optional[str]
    active: bool
    email_verified: bool
    roles: List[str]
