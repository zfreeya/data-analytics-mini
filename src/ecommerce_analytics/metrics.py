from __future__ import annotations
import pandas as pd


def build_daily_metrics(df: pd.DataFrame) -> pd.DataFrame:
    daily = (
        df.groupby("date")
          .agg(
              dau=("user_id", pd.Series.nunique),
              orders=("event", lambda x: (x == "purchase").sum()),
              payments=("event", lambda x: (x == "pay").sum()),
              gmv=("revenue", "sum"),
          )
          .reset_index()
    )
    return daily


def build_channel_daily(df: pd.DataFrame) -> pd.DataFrame:
    channel_daily = (
        df.groupby(["date", "channel"])
          .agg(
              users=("user_id", "nunique"),
              orders=("event", lambda x: (x == "purchase").sum()),
              gmv=("revenue", "sum"),
          )
          .reset_index()
    )
    return channel_daily
