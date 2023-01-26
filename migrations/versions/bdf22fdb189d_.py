"""empty message

Revision ID: bdf22fdb189d
Revises: 3015d0a17bfd
Create Date: 2023-01-26 21:11:01.275475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bdf22fdb189d'
down_revision = '3015d0a17bfd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favoritos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('personajes_id', sa.Integer(), nullable=True),
    sa.Column('vehiculos_id', sa.Integer(), nullable=True),
    sa.Column('planetas_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['personajes_id'], ['personajes.id'], ),
    sa.ForeignKeyConstraint(['planetas_id'], ['planetas.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['vehiculos_id'], ['vehiculos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favoritos')
    # ### end Alembic commands ###