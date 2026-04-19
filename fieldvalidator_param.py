from pydantic import BaseModel, field_validator

class User(BaseModel):
    username: str
    password: str

    @field_validator("username")
    def username_must_not_have_space(cls, value):
        if " " in value:
            raise ValueError("Username must not contain spaces")
        return value

    @field_validator("password")
    def password_length(cls, value):
        if len(value) < 6:
            raise ValueError("Password must be at least 6 characters")
        return value

user = User(username="saif123", password="secret123")
print(user)