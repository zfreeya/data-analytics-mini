from __future__ import annotations
import pandas as pd

STAGES = ["view", "cart", "purchase", "pay"]


def user_level_funnel(df: pd.DataFrame, stages=STAGES) -> pd.DataFrame:
    pivot = df.pivot_table(
        index="user_id",
        columns="event",
        values="ts_local",
        aggfunc="min",
    )
    stage_counts = pivot[stages].notna().sum()
    base = stage_counts.iloc[0] if stage_counts.iloc[0] else 1
    rate = (stage_counts / base).round(4)
    return pd.DataFrame({"users": stage_counts, "rate": rate})
