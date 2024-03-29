"""Added new model (insight), changed users slightly and groups as well

Revision ID: 2d365729906d
Revises: 5df5b08a496b
Create Date: 2024-03-20 11:33:02.356164

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d365729906d'
down_revision = '5df5b08a496b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('insights',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], name=op.f('fk_insights_group_id_groups')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_insights'))
    )
    with op.batch_alter_table('groups', schema=None) as batch_op:
        batch_op.add_column(sa.Column('_access_token', sa.String(), nullable=True))

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('group_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('group_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('groups', schema=None) as batch_op:
        batch_op.drop_column('_access_token')

    op.drop_table('insights')
    # ### end Alembic commands ###
