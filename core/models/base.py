from typing import Any


class BaseModel:

    def to_json(self) -> dict[str, Any]:
        return {key: getattr(self, key) for key in self.__dict__.keys() if not key.startswith("_")}
