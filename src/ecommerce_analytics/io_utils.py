from __future__ import annotations
import json
from pathlib import Path
from typing import Dict, Any
import pandas as pd


def ensure_dirs(*paths: str | Path) -> None:
    for p in paths:
        Path(p).mkdir(parents=True, exist_ok=True)


def read_csv(path: str | Path, dtype: Dict[str, str] | None = None, parse_dates=None) -> pd.DataFrame:
    return pd.read_csv(
        path,
        dtype=dtype or {
            "event_id": "string",
            "user_id": "string",
            "session_id": "string",
            "event": "string",
            "product_id": "string",
            "device": "string",
            "city": "string",
            "channel": "string",
        },
        parse_dates=parse_dates or ["ts"],
        keep_default_na=True,
        na_values=["", "NA", "N/A", "null", "None"],
    )


def to_parquet(df: pd.DataFrame, path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False)


def to_csv(df: pd.DataFrame, path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def dump_json(obj: Dict[str, Any], path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
