from typing import List

import sqlalchemy as sa
from gino import Gino

from data import config

db = Gino()


class BaseModel(db.Model):
    __abstract__ = True

    def __str__(self):
        model = self.__class__.__name__
        table: sa.Table = sa.inspect(self.__class__)
        primary_key_columns: List[sa.Column] = table.columns
        values = {
            column.name: getattr(self, self._column_name_map[column.name])
            for column in primary_key_columns
        }
        values_str = " ".join(f"{name}={value!r}" for name, value in values.items())
        return f"<{model} {values_str}>"


async def connect_base(dp):
    await db.set_bind(config.POSTGRES_URI)
    print('Database connected!')


async def close_base(dp):
    bind = db.pop_bind()
    await bind.close()
    print('Database closed!')
