"""Changed contraints on users

Revision ID: 711cc6fffe0f
Revises: 24dec93a25c5
Create Date: 2024-03-22 12:42:14.244450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '711cc6fffe0f'
down_revision = '24dec93a25c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('phone',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.drop_constraint('uq_users_first_name', type_='unique')
        batch_op.drop_constraint('uq_users_last_name', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_unique_constraint('uq_users_last_name', ['last_name'])
        batch_op.create_unique_constraint('uq_users_first_name', ['first_name'])
        batch_op.alter_column('phone',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###
