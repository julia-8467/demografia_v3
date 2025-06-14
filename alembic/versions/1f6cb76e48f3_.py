"""empty message

Revision ID: 1f6cb76e48f3
Revises: ea19043695b3
Create Date: 2025-06-04 19:48:51.782074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f6cb76e48f3'
down_revision = 'ea19043695b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('zgony_woj',
    sa.Column('liczba_ludnosci', sa.Integer(), nullable=True),
    sa.Column('kobiety', sa.Integer(), nullable=True),
    sa.Column('mezczyzni', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('wojewodztwa', sa.String(), nullable=True),
    sa.Column('rok', sa.Integer(), nullable=True),
    sa.Column('liczba_ogolem', sa.Integer(), nullable=True),
    sa.Column('p0_4', sa.Integer(), nullable=True),
    sa.Column('p5_9', sa.Integer(), nullable=True),
    sa.Column('p10_14', sa.Integer(), nullable=True),
    sa.Column('p15_19', sa.Integer(), nullable=True),
    sa.Column('p20_24', sa.Integer(), nullable=True),
    sa.Column('p25_29', sa.Integer(), nullable=True),
    sa.Column('p30_34', sa.Integer(), nullable=True),
    sa.Column('p35_39', sa.Integer(), nullable=True),
    sa.Column('p40_44', sa.Integer(), nullable=True),
    sa.Column('p45_49', sa.Integer(), nullable=True),
    sa.Column('p50_54', sa.Integer(), nullable=True),
    sa.Column('p55_59', sa.Integer(), nullable=True),
    sa.Column('p60_64', sa.Integer(), nullable=True),
    sa.Column('p65_69', sa.Integer(), nullable=True),
    sa.Column('p70_74', sa.Integer(), nullable=True),
    sa.Column('p75_79', sa.Integer(), nullable=True),
    sa.Column('p80_84', sa.Integer(), nullable=True),
    sa.Column('p85', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_zgony_woj_id'), 'zgony_woj', ['id'], unique=False)
    op.drop_index('ix_ludnosc_woj_id', table_name='ludnosc_woj')
    op.drop_table('ludnosc_woj')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ludnosc_woj',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('wojewodztwa', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('rok', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('liczba_ludnosci', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('kobiety', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('mezczyzni', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='ludnosc_woj_pkey')
    )
    op.create_index('ix_ludnosc_woj_id', 'ludnosc_woj', ['id'], unique=False)
    op.drop_index(op.f('ix_zgony_woj_id'), table_name='zgony_woj')
    op.drop_table('zgony_woj')
    # ### end Alembic commands ###
