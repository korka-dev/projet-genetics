"""update GuardQRScan table

Revision ID: 9f542696c525
Revises: ddc44b21ed7a
Create Date: 2025-06-17 20:49:23.390956

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '9f542696c525'
down_revision: Union[str, None] = 'ddc44b21ed7a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('guard_qr_scans', sa.Column('confirmed', sa.Boolean(), nullable=True))
    op.add_column('guard_qr_scans', sa.Column('scanned_at', sa.DateTime(), nullable=False))
    op.add_column('guard_qr_scans', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.add_column('guard_qr_scans', sa.Column('updated_at', sa.DateTime(), nullable=False))
    op.alter_column('guard_qr_scans', 'guard_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.create_index(op.f('ix_guard_qr_scans_id'), 'guard_qr_scans', ['id'], unique=False)
    op.drop_column('guard_qr_scans', 'scan_time')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('guard_qr_scans', sa.Column('scan_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_guard_qr_scans_id'), table_name='guard_qr_scans')
    op.alter_column('guard_qr_scans', 'guard_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.drop_column('guard_qr_scans', 'updated_at')
    op.drop_column('guard_qr_scans', 'created_at')
    op.drop_column('guard_qr_scans', 'scanned_at')
    op.drop_column('guard_qr_scans', 'confirmed')
    # ### end Alembic commands ###
