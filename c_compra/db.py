from typing import Annotated, Iterator

from fastapi import Depends
from sqlmodel import Session

from engine import engine


def get_session() -> Iterator[Session]:
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

