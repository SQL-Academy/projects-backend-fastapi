"""add owner_id to tasks

Revision ID: b5c6d7e8f9a0
Revises: a4b5c6d7e8f9
Create Date: 2026-05-02 14:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


revision = "b5c6d7e8f9a0"
down_revision = "a4b5c6d7e8f9"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("tasks", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "fk_tasks_owner_id_users", "tasks", "users", ["owner_id"], ["id"]
    )


def downgrade() -> None:
    op.drop_constraint("fk_tasks_owner_id_users", "tasks", type_="foreignkey")
    op.drop_column("tasks", "owner_id")
