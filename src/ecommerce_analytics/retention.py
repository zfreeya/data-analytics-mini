from __future__ import annotations
import pandas as pd


def simple_retention(df: pd.DataFrame) -> pd.DataFrame:
    first_day = df.groupby("user_id")["date"].min()
    x = df.merge(first_day.rename("first_date"), on="user_id")
    x["date"] = pd.to_datetime(x["date"])
    x["first_date"] = pd.to_datetime(x["first_date"])

    cohort = (
        x.assign(day_offset=lambda d: (d["date"] - d["first_date"]).dt.days)
         .groupby(["first_date", "day_offset"])["user_id"]
         .nunique()
         .unstack(fill_value=0)
    )
    retention = (cohort.divide(cohort[0], axis=0) * 100).round(1)
    return retention
