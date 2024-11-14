"""empty message

Revision ID: dbf170abb6c0
Revises: 8fdb370bb86b
Create Date: 2024-11-14 22:37:22.866459

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dbf170abb6c0'
down_revision: Union[str, None] = '8fdb370bb86b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('Doctor', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('username', sa.String(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
            )


def downgrade() -> None:
    pass
