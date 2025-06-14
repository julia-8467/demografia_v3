"""empty message

Revision ID: ea19043695b3
Revises: 0410969e59b3
Create Date: 2025-06-04 19:39:08.259751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea19043695b3'
down_revision = '0410969e59b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ludnosc_woj',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('wojewodztwa', sa.String(), nullable=True),
    sa.Column('rok', sa.Integer(), nullable=True),
    sa.Column('liczba_ludnosci', sa.Integer(), nullable=True),
    sa.Column('kobiety', sa.Integer(), nullable=True),
    sa.Column('mezczyzni', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ludnosc_woj_id'), 'ludnosc_woj', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_ludnosc_woj_id'), table_name='ludnosc_woj')
    op.drop_table('ludnosc_woj')
    # ### end Alembic commands ###
