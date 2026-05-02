"""add priority column

Revision ID: 7f8e9d0c1b2a
Revises: 1a2b3c4d5e6f
Create Date: 2026-05-01 12:30:00.000000

"""
from alembic import op
import sqlalchemy as sa


revision = "7f8e9d0c1b2a"
down_revision = "1a2b3c4d5e6f"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "tasks",
        sa.Column("priority", sa.Integer(), nullable=True),
    )


def downgrade() -> None:
    op.drop_column("tasks", "priority")
