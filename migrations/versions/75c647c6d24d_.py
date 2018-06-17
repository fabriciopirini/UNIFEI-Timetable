"""empty message

Revision ID: 75c647c6d24d
Revises: 5ee25e63d056
Create Date: 2018-05-02 11:07:39.359234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75c647c6d24d'
down_revision = '5ee25e63d056'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('disciplinas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=150), nullable=True),
    sa.Column('campus', sa.String(length=30), nullable=True),
    sa.Column('curso', sa.String(length=5), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('turmas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idDisciplina', sa.Integer(), nullable=False),
    sa.Column('periodo', sa.String(length=10), nullable=True),
    sa.Column('nivel', sa.String(length=10), nullable=True),
    sa.Column('turma', sa.String(length=10), nullable=True),
    sa.Column('docente', sa.String(length=100), nullable=True),
    sa.Column('situacao', sa.String(length=10), nullable=True),
    sa.Column('horario', sa.String(length=1000), nullable=True),
    sa.Column('local', sa.String(length=30), nullable=True),
    sa.Column('matriculados', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['idDisciplina'], ['disciplinas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('turmas')
    op.drop_table('disciplinas')
    # ### end Alembic commands ###
