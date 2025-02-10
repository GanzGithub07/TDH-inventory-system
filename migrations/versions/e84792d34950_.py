"""empty message

Revision ID: e84792d34950
Revises: 846e3810e1ff
Create Date: 2025-02-09 14:08:19.234031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e84792d34950'
down_revision = '846e3810e1ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('purchase_price', sa.Float(), nullable=True),
    sa.Column('selling_price', sa.Float(), nullable=True),
    sa.Column('purchase_date', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('batch_no', sa.String(), nullable=True),
    sa.Column('supplier', sa.String(), nullable=True),
    sa.Column('total_price', sa.Float(), nullable=True),
    sa.Column('expiration_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('item_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item')
    # ### end Alembic commands ###
