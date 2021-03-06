"""empty message

Revision ID: 92dc23bba992
Revises: 7feb275f4285
Create Date: 2020-07-14 01:46:02.650068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92dc23bba992'
down_revision = '7feb275f4285'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('weather',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city_name', sa.String(length=30), nullable=True),
    sa.Column('description', sa.String(length=30), nullable=True),
    sa.Column('icon', sa.String(length=30), nullable=True),
    sa.Column('main', sa.String(length=30), nullable=True),
    sa.Column('temperature', sa.Float(), nullable=True),
    sa.Column('humidity', sa.Float(), nullable=True),
    sa.Column('timezone', sa.Integer(), nullable=True),
    sa.Column('wind_speed', sa.Float(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('time', sa.Time(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('weather')
    # ### end Alembic commands ###
