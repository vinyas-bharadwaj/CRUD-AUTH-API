"""empty message

Revision ID: 8fdb370bb86b
Revises: b9bb6509eb2b
Create Date: 2024-11-14 22:29:49.160943

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8fdb370bb86b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('User', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                        sa.Column('username', sa.String(), nullable=False),
                        sa.Column('email', sa.String(), nullable=False),
                        sa.Column('password', sa.String(), nullable=False),
                        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
                )


def downgrade() -> None:
    op.drop_table('User')
