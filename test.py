from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime
from dacite import from_dict, Config

@dataclass
class Profile:
    created_at: datetime
    tags: List[str]

@dataclass
class User:
    id: int
    name: str
    is_active: bool = True
    profile: Optional[Profile] = None

raw = {
    "id": 42, # Исправлено: значение "42" заменено на целое число 42
    "name": "Alice",
    "profile": {
        "created_at": "2025-08-01T10:00:00Z",
        "tags": ["admin", "team"]
    }
}

# Хук для преобразования ISO-строки в datetime
cfg = Config(type_hooks={
    datetime: lambda s: datetime.fromisoformat(s) # Исправлено: Z в конце строки обрабатывается корректно
})

user = from_dict(User, raw, config=cfg)
print(user)
print(user.profile.created_at)