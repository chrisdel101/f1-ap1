"""empty message

Revision ID: 057fab61695c
Revises: 
Create Date: 2019-11-26 22:25:18.745441

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '057fab61695c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('driver')
    op.drop_table('team')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('driver',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('driver_name', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('country', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('name_slug', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('date_of_birth', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('driver_number', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('place_of_birth', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('flag_img_url', sa.VARCHAR(length=150), autoincrement=False, nullable=True),
    sa.Column('main_image', sa.VARCHAR(length=150), autoincrement=False, nullable=True),
    sa.Column('podiums', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('world_championships', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('highest_grid_position', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('points', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('position', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('team', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('team_name_slug', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('team_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], name='driver_team_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='driver_pkey'),
    sa.UniqueConstraint('name_slug', name='driver_name_slug_key')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('driver_data', postgresql.BYTEA(), autoincrement=False, nullable=True),
    sa.Column('team_data', postgresql.BYTEA(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey')
    )
    op.create_table('team',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('full_team_name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('team_name_slug', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('url_name_slug', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('base', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('team_chief', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('technical_chief', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('power_unit', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('first_team_entry', sa.VARCHAR(length=25), autoincrement=False, nullable=True),
    sa.Column('highest_race_finish', sa.VARCHAR(length=25), autoincrement=False, nullable=True),
    sa.Column('pole_positions', sa.VARCHAR(length=25), autoincrement=False, nullable=True),
    sa.Column('fastest_laps', sa.VARCHAR(length=25), autoincrement=False, nullable=True),
    sa.Column('main_image', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('flag_img_url', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('logo_url', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('podium_finishes', sa.VARCHAR(length=25), autoincrement=False, nullable=True),
    sa.Column('championship_titles', sa.VARCHAR(length=25), autoincrement=False, nullable=True),
    sa.Column('drivers_scraped', postgresql.BYTEA(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='team_pkey'),
    sa.UniqueConstraint('full_team_name', name='team_full_team_name_key'),
    sa.UniqueConstraint('team_name_slug', name='team_team_name_slug_key')
    )
    # ### end Alembic commands ###
