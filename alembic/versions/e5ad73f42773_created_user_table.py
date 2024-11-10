"""created user table

Revision ID: e5ad73f42773
Revises: 
Create Date: 2024-11-10 18:38:35.837205

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e5ad73f42773'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('User', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                            sa.Column('email', sa.String(), nullable=False, primary_key=True),
                            sa.Column('password', sa.String(), nullable=False, primary_key=True),
                            sa.Column('created_at', sa.TIMESTAMP(), nullable=False, primary_key=True),
                    )
    

def downgrade() -> None:
    op.drop_table('User')
    
