from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# для autogenerate Alembic-у нужно знать «правильную» схему:
# импорт моделей регистрирует их в Base.metadata.
import models
from database import Base

target_metadata = Base.metadata


# дальше всё, что сгенерировал alembic init, не трогаем
