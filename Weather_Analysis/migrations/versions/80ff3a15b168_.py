"""empty message

Revision ID: 80ff3a15b168
Revises: a29dee88ed52
Create Date: 2020-07-14 01:23:24.534989

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80ff3a15b168'
down_revision = 'a29dee88ed52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('weather', sa.Column('date', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('weather', 'date')
    # ### end Alembic commands ###
