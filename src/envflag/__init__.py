import os
from typing import Any


class EnvFlag:
    __slots__ = ("name",)

    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, instance: Any, owner: Any) -> bool:
        env_value: str = os.environ.get(self.name, "")
        match env_value.lower():
            case "1" | "true":
                return True
            case "0" | "false" | "":
                return False
            case _:
                return False

    def get(self) -> bool:
        return self.__get__(instance=None, owner=None)

    def __str__(self) -> str:
        return f"EnvFlag [{self.name}]: {self.get()}"

    def __repr__(self) -> str:
        return str(self)


__all__ = ["EnvFlag"]
