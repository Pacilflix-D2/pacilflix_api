from dataclasses import dataclass


@dataclass(frozen=True)
class LoginResponse:
    username: str


@dataclass(frozen=True)
class RegisterResponse:
    username: str
