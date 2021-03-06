"""empty message

Revision ID: 3974d310ac43
Revises: edfc37a36914
Create Date: 2016-11-11 16:39:16.828429

"""

# revision identifiers, used by Alembic.
revision = '3974d310ac43'
down_revision = 'edfc37a36914'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('routes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('providerId', sa.Integer(), nullable=True),
    sa.Column('providerName', sa.String(length=120), nullable=True),
    sa.Column('routeName', sa.String(length=20), nullable=True),
    sa.Column('pathAttributeId', sa.Integer(), nullable=True),
    sa.Column('departure', sa.String(length=20), nullable=True),
    sa.Column('destination', sa.String(length=20), nullable=True),
    sa.Column('distance', sa.String(length=20), nullable=True),
    sa.Column('goFirstBusTime', sa.String(length=4), nullable=True),
    sa.Column('backFirstBusTime', sa.String(length=4), nullable=True),
    sa.Column('goLastBusTime', sa.String(length=4), nullable=True),
    sa.Column('backLastBusTime', sa.String(length=4), nullable=True),
    sa.Column('holidayGoFirstBusTime', sa.String(length=4), nullable=True),
    sa.Column('holidayBackFirstBusTime', sa.String(length=4), nullable=True),
    sa.Column('holidayGoLastBusTime', sa.String(length=4), nullable=True),
    sa.Column('holidayBackLastBusTime', sa.String(length=4), nullable=True),
    sa.Column('segmentBuffer', sa.String(length=200), nullable=True),
    sa.Column('ticketPriceDescription', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stops',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('routeId', sa.Integer(), nullable=True),
    sa.Column('routeName', sa.String(length=200), nullable=True),
    sa.Column('seqNo', sa.Integer(), nullable=True),
    sa.Column('longitude', sa.String(length=50), nullable=True),
    sa.Column('latitude', sa.String(length=50), nullable=True),
    sa.Column('goBack', sa.String(length=2), nullable=True),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.Column('stopLocationId', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
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
    op.drop_table('stops')
    op.drop_table('routes')
    ### end Alembic commands ###
