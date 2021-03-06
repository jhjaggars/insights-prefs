"""empty message

Revision ID: 3ea7f0050080
Revises: 
Create Date: 2019-04-08 14:27:49.496500

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3ea7f0050080'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('preferences',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('account', sa.String(length=10), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('modified_on', sa.DateTime(), nullable=True),
    sa.Column('prefs', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('preferences')
    # ### end Alembic commands ###
