"""empty message

Revision ID: 99c401c383d2
Revises: dbf170abb6c0
Create Date: 2024-11-15 11:21:07.020064

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '99c401c383d2'
down_revision: Union[str, None] = 'dbf170abb6c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('User', sa.Column('profile_pic', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('User', 'profile_pic')
