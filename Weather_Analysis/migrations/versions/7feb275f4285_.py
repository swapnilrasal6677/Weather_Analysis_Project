"""empty message

Revision ID: 7feb275f4285
Revises: 80ff3a15b168
Create Date: 2020-07-14 01:24:47.839225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7feb275f4285'
down_revision = '80ff3a15b168'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('weather', sa.Column('time', sa.Time(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('weather', 'time')
    # ### end Alembic commands ###
