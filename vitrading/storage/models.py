from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass



class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    instrument_id: Mapped[int] = mapped_column()

