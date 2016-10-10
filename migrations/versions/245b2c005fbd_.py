"""empty message

Revision ID: 245b2c005fbd
Revises: 5687e4f528b9
Create Date: 2016-10-10 23:16:13.895125

"""

# revision identifiers, used by Alembic.
revision = '245b2c005fbd'
down_revision = '5687e4f528b9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chatid', sa.Integer(), nullable=True),
    sa.Column('last_name', sa.String(length=120), nullable=True),
    sa.Column('first_name', sa.String(length=120), nullable=True),
    sa.Column('lat', sa.String(length=50), nullable=True),
    sa.Column('lng', sa.String(length=50), nullable=True),
    sa.Column('cmd', sa.String(length=1000), nullable=True),
    sa.Column('bus_route', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    ### end Alembic commands ###