"""empty message

Revision ID: c50cd723e7b3
Revises: e5ad73f42773
Create Date: 2024-11-12 18:50:29.850249

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c50cd723e7b3'
down_revision: Union[str, None] = 'e5ad73f42773'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('User', sa.Column('username', sa.String(), nullable=False))

def downgrade() -> None:
    pass
