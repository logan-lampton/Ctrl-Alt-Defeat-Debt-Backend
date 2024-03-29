"""Removed account model

Revision ID: 5df5b08a496b
Revises: 6d674d97ecc1
Create Date: 2024-03-18 16:23:02.455870

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5df5b08a496b'
down_revision = '6d674d97ecc1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('accounts')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('balance')

    op.create_table('accounts',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('type', sa.VARCHAR(), nullable=False),
    sa.Column('balance', sa.FLOAT(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_accounts_user_id_users'),
    sa.PrimaryKeyConstraint('id', name='pk_accounts')
    )
    # ### end Alembic commands ###
