from __future__ import annotations
import argparse
import yaml
from pathlib import Path
from typing import Any, Dict

from .io_utils import read_csv, ensure_dirs, to_parquet, to_csv, dump_json
from .cleaning import clean_events
from .metrics import build_daily_metrics, build_channel_daily
from .funnel import user_level_funnel
from .visualize import plot_gmv_daily, plot_funnel_rate


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="E-commerce analytics pipeline")
    ap.add_argument("--config", default="config.yaml", help="Path to config.yaml")
    return ap.parse_args()


def load_config(path: str | Path) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main() -> None:
    args = parse_args()
    cfg = load_config(args.config)

    input_csv = cfg["paths"]["input_csv"]
    out_dir = cfg["paths"]["output_dir"]
    fig_dir = cfg["paths"]["figure_dir"]
    tz = cfg["params"].get("timezone", "Asia/Shanghai")
    iqr_k = float(cfg["params"].get("iqr_k", 1.5))
    qty_upper = int(cfg["params"].get("qty_upper_limit", 100))

    ensure_dirs(out_dir, fig_dir)

    df_raw = read_csv(input_csv)

    res = clean_events(df_raw, tz=tz, qty_upper=qty_upper, iqr_k=iqr_k)
    df = res["data"]
    report = res["report"]

    daily = build_daily_metrics(df)
    channel_daily = build_channel_daily(df)

    funnel_df = user_level_funnel(df)

    to_parquet(df, Path(out_dir) / "clean_events.parquet")
    to_csv(df, Path(out_dir) / "clean_events.csv")
    to_csv(daily, Path(out_dir) / "daily_metrics.csv")
    to_csv(channel_daily, Path(out_dir) / "channel_daily_metrics.csv")
    to_csv(funnel_df, Path(out_dir) / "funnel_rate.csv")
    dump_json(report, Path(out_dir) / "quality.json")

    plot_gmv_daily(daily, Path(fig_dir) / "gmv_daily.png")
    plot_funnel_rate(funnel_df, Path(fig_dir) / "funnel_rate.png")

    print("Pipeline finished. Outputs saved to:", Path(out_dir).resolve())


if __name__ == "__main__":
    main()
