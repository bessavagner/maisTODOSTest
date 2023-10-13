from pydantic import BaseModel


class CreditCardSchema(BaseModel):
    id: int = None
    exp_date: str = None
    holder: str = None
    number: str = None
    cvv: str = None
    brand: str = None

    class Config:
        orm_mode = True
