"""Adds timestamps to the SearchFilter model

Revision ID: 9ad021045e45
Revises: 930eb80028d2
Create Date: 2023-05-17 11:30:33.542458

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "9ad021045e45"
down_revision = "930eb80028d2"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("search_filter", sa.Column("enabled", sa.Boolean(), nullable=True))
    op.add_column("search_filter", sa.Column("updated_at", sa.DateTime(), nullable=True))
    op.add_column("search_filter", sa.Column("created_at", sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("search_filter", "created_at")
    op.drop_column("search_filter", "updated_at")
    op.drop_column("search_filter", "enabled")
    # ### end Alembic commands ###
