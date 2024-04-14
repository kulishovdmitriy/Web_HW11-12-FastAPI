"""Init birthday

Revision ID: 493d8568042c
Revises: 9a665485bb8c
Create Date: 2024-04-14 19:00:25.137077

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '493d8568042c'
down_revision: Union[str, None] = '9a665485bb8c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('contacts', 'birthday',
               existing_type=sa.DATE(),
               type_=sa.String(length=10),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('contacts', 'birthday',
               existing_type=sa.String(length=10),
               type_=sa.DATE(),
               existing_nullable=False)
    # ### end Alembic commands ###