from datetime import datetime
from sqlalchemy import (
    ForeignKey,
    BigInteger,
    DateTime,
    Integer,
    String,
    Float
)
from sqlalchemy.orm import (
    DeclarativeBase,
    mapped_column,
    Mapped
)


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    username: Mapped[str] = mapped_column(String, default="NONE")
    balance: Mapped[float] = mapped_column(Float, default=0.0)
    uuid: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    expiry_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    current_tariff_id: Mapped[int] = mapped_column(Integer, ForeignKey("tariffs.id"), nullable=True)
    referrer_id: Mapped[int] = mapped_column(BigInteger, nullable=True)  # Кто пригласил (его tg_id)


class Tariff(Base):
    __tablename__ = 'tariffs'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Float)
    days: Mapped[int] = mapped_column(Integer)
    gb_limit: Mapped[int] = mapped_column(Integer)


class Feedback(Base):
    __tablename__ = 'feedback'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    user_name: Mapped[str] = mapped_column(String)
    message_text: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)


class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    tariff_name: Mapped[str] = mapped_column(String)
    amount_mandarins: Mapped[float] = mapped_column(Float)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
