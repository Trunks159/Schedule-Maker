"""empty message

Revision ID: b69c67922d7b
Revises: 
Create Date: 2019-10-31 11:44:17.546439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b69c67922d7b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('worker',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=60), nullable=True),
    sa.Column('last_name', sa.String(length=60), nullable=True),
    sa.Column('position', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_worker_first_name'), 'worker', ['first_name'], unique=False)
    op.create_index(op.f('ix_worker_last_name'), 'worker', ['last_name'], unique=False)
    op.create_index(op.f('ix_worker_position'), 'worker', ['position'], unique=False)
    op.create_table('availability',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('monday', sa.String(length=60), nullable=True),
    sa.Column('tuesday', sa.String(length=60), nullable=True),
    sa.Column('wednesday', sa.String(length=60), nullable=True),
    sa.Column('thursday', sa.String(length=60), nullable=True),
    sa.Column('friday', sa.String(length=60), nullable=True),
    sa.Column('saturday', sa.String(length=60), nullable=True),
    sa.Column('sunday', sa.String(length=60), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['worker.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_availability_friday'), 'availability', ['friday'], unique=False)
    op.create_index(op.f('ix_availability_monday'), 'availability', ['monday'], unique=False)
    op.create_index(op.f('ix_availability_saturday'), 'availability', ['saturday'], unique=False)
    op.create_index(op.f('ix_availability_sunday'), 'availability', ['sunday'], unique=False)
    op.create_index(op.f('ix_availability_thursday'), 'availability', ['thursday'], unique=False)
    op.create_index(op.f('ix_availability_tuesday'), 'availability', ['tuesday'], unique=False)
    op.create_index(op.f('ix_availability_wednesday'), 'availability', ['wednesday'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_availability_wednesday'), table_name='availability')
    op.drop_index(op.f('ix_availability_tuesday'), table_name='availability')
    op.drop_index(op.f('ix_availability_thursday'), table_name='availability')
    op.drop_index(op.f('ix_availability_sunday'), table_name='availability')
    op.drop_index(op.f('ix_availability_saturday'), table_name='availability')
    op.drop_index(op.f('ix_availability_monday'), table_name='availability')
    op.drop_index(op.f('ix_availability_friday'), table_name='availability')
    op.drop_table('availability')
    op.drop_index(op.f('ix_worker_position'), table_name='worker')
    op.drop_index(op.f('ix_worker_last_name'), table_name='worker')
    op.drop_index(op.f('ix_worker_first_name'), table_name='worker')
    op.drop_table('worker')
    # ### end Alembic commands ###