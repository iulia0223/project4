from alembic import context
import config
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig
from your_database_models import Base, Playlist, PlaylistTrack, Track, User  # Замініть на імпорт ваших моделей бази даних

# Записуємо конфігурацію логування з файлу
if context.config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Визначаємо об'єкт метаданих для міграцій
target_metadata = Base.metadata

# Функція для виконання міграцій в режимі "offline"
def run_migrations_offline():
    url = context.config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# Функція для виконання міграцій в режимі "online"
def run_migrations_online():
    connectable = engine_from_config(
        context.config.get_section(context.config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# Перевіряємо, в якому режимі запущено міграції
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig
from your_database_models import Playlist, PlaylistTrack, Track, User  # Замініть на імпорт ваших моделей бази даних
