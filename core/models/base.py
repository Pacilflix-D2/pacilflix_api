from datetime import datetime
from typing import Any


class BaseModel:

    def to_json(self) -> dict[str, Any]:
        def convert(value: Any) -> str | Any:
            if isinstance(value, datetime):
                return value.strftime('%Y-%m-%dT%H:%M:%S.%f%zZ')
            return value

        return {key: convert(getattr(self, key)) for key in self.__dict__.keys() if not key.startswith("_")}
