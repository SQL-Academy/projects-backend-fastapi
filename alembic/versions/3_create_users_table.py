"""create users table

Revision ID: a4b5c6d7e8f9
Revises: 7f8e9d0c1b2a
Create Date: 2026-05-02 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


revision = "a4b5c6d7e8f9"
down_revision = "7f8e9d0c1b2a"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password_hash", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )


def downgrade() -> None:
    op.drop_table("users")
