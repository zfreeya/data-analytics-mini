from __future__ import annotations
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


def plot_gmv_daily(daily: pd.DataFrame, out_path: str | None = None) -> None:
    plt.figure(figsize=(8, 4))
    plt.plot(daily["date"], daily["gmv"], marker="o")
    plt.title("GMV 日级趋势")
    plt.xlabel("日期")
    plt.ylabel("GMV (¥)")
    plt.grid(True)
    if out_path:
        Path(out_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(out_path, bbox_inches="tight", dpi=150)
    plt.close()


def plot_funnel_rate(funnel_df: pd.DataFrame, out_path: str | None = None) -> None:
    plt.figure(figsize=(6, 4))
    plt.plot(funnel_df.index, funnel_df["rate"].values, marker="o")
    plt.title("用户行为漏斗转化率")
    plt.ylabel("转化率")
    plt.grid(True)
    if out_path:
        Path(out_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(out_path, bbox_inches="tight", dpi=150)
    plt.close()
