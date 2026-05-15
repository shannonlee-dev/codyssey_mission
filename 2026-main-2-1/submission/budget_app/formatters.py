from __future__ import annotations

from .models import Transaction


def money(value: int) -> str:
    return f"{value}원"


def format_transaction(tx: Transaction) -> str:
    tags = ",".join(tx.tags)
    return (
        f"{tx.id:<9} | {tx.date:<10} | {tx.type:<7} | {tx.category:<14} | "
        f"{tx.amount:>10} | {tx.memo} | {tags}"
    ).rstrip()


def print_transactions(rows: list[Transaction]) -> None:
    if not rows:
        print("데이터 없음")
        return
    print("ID        | DATE       | TYPE    | CATEGORY       | AMOUNT     | MEMO | TAGS")
    print("-" * 82)
    for tx in rows:
        print(format_transaction(tx))
