from ninja import Schema


class ADUserOut(Schema):
    username: str
    email: str
    display_name: str
    enabled: bool
