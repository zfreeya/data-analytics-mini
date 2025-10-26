from __future__ import annotations
import pandas as pd
from typing import Dict, Any

EVENT_LEVELS = ["view", "cart", "purchase", "pay", "refund"]
CHANNEL_MAP = {
    "sem": "sem", "adwords": "sem", "google_ads": "sem",
    "organic": "organic", "seo": "organic",
    "push": "push", "notification": "push"
}


def clean_events(raw: pd.DataFrame, *, tz: str = "Asia/Shanghai", qty_upper: int = 100, iqr_k: float = 1.5) -> Dict[str, Any]:
    df = raw.copy()

    # --- 缺失与基本过滤 ---
    need_price_qty = df["event"].isin(["purchase", "cart", "pay"])
    df = df.loc[~(need_price_qty & (df["price"].isna() | df["qty"].isna()))].copy()

    # 标记 view 的 product 缺失，不删除
    df["product_missing"] = df["event"].eq("view") & df["product_id"].isna()

    # --- 去重（event_id 优先；否则业务键） ---
    if "event_id" in df.columns:
        df = df.drop_duplicates(subset=["event_id"], keep="first")
    df = df.sort_values("ts").drop_duplicates(subset=["user_id", "event", "product_id", "ts"], keep="first")

    # --- 类型与时间 ---
    for col in ["price", "qty"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    must_positive = df["event"].isin(["purchase", "pay"]) & ((df["price"] <= 0) | (df["qty"] <= 0))
    df = df.loc[~must_positive].copy()

    df["ts"] = pd.to_datetime(df["ts"], errors="coerce", utc=True)
    df = df.loc[df["ts"].notna()].copy()
    df["ts_local"] = df["ts"].dt.tz_convert(tz)
    df["date"] = df["ts_local"].dt.date

    for c in ["device", "channel", "city", "user_id", "session_id", "product_id"]:
        if c in df.columns:
            df[c] = df[c].astype("string").str.strip().str.lower()
    df["channel"] = df["channel"].map(lambda x: CHANNEL_MAP.get(x, x))

    df["event"] = pd.Categorical(df["event"], categories=EVENT_LEVELS)

    if {"price", "qty"}.issubset(df.columns):
        df["revenue"] = df["price"] * df["qty"]

        q1, q3 = df["price"].quantile(0.25), df["price"].quantile(0.75)
        iqr = q3 - q1
        lo, hi = q1 - iqr_k * iqr, q3 + iqr_k * iqr
        df["price_outlier"] = (df["price"] < lo) | (df["price"] > hi)

        df["qty_too_large"] = df["qty"] > qty_upper

    checks = {
        "ts_not_null": df["ts"].notna().all(),
        "known_event_values": df["event"].isin(EVENT_LEVELS).all(),
        "positive_on_purchase_pay": (~(df["event"].isin(["purchase", "pay"]) & ((df["price"] <= 0) | (df["qty"] <= 0)))).all(),
    }

    report = {
        "row_count": int(len(df)),
        "n_missing": {k: int(v) for k, v in df.isna().sum().to_dict().items()},
        "checks": checks,
        "outlier_ratio": {
            "price": float(df.get("price_outlier", pd.Series()).mean()) if "price_outlier" in df else 0.0,
            "qty_too_large": float(df.get("qty_too_large", pd.Series()).mean()) if "qty_too_large" in df else 0.0,
        },
    }

    return {"data": df, "report": report}
