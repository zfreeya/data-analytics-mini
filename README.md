# ecommerce-analytics-pandas

Pandas 驱动的电商日志分析流水线：**清洗 → 指标 → 漏斗 → 趋势 → 导出**。

## 一、环境准备
- Python 3.9+
- 任选其一安装方式：
  - `pip install -r requirements.txt`
  - 或使用 `pyproject.toml`：`pip install .`（或 `pipx run` 等）

## 二、快速开始
1. 将你的原始日志 CSV 放在 `data/input/events.csv`（或修改 `config.yaml`）。
2. 运行：
   ```bash
   python -m ecommerce_analytics.cli --config config.yaml
   # 或
   python scripts/run_pipeline.py
   ```

3. 输出位置：`data/output/`（含清洗后数据、指标、漏斗、质量报告与图表）。

## 三、数据要求（最小集合）

必需列：

* `user_id`, `event`, `ts`

可选列（用于增强分析）：

* `event_id`, `session_id`, `product_id`, `price`, `qty`, `device`, `city`, `channel`

## 四、指标口径

* `dau`：当天产生任意事件的独立用户数
* `orders`：`event=purchase` 的条数（事件级）
* `payments`：`event=pay` 的条数
* `gmv`：`Σ(price*qty)`
* 漏斗：`view → cart → purchase → pay` 基于**用户层**是否出现过该事件

## 五、自定义

* 在 `config.yaml` 中修改 `timezone`、`qty_upper_limit`、`iqr_k` 等
* 在 `cleaning.py` 中新增业务规则（例如价格带校验、时序前置校验）
* 在 `metrics.py`/`funnel.py` 中增加渠道/品类/活动维度

## 六、注意事项

* 时间统一为 UTC 存储，展示转为本地时区 `ts_local`
* 去重优先使用 `event_id`；否则使用业务键（`user_id+event+product_id+ts`）
* 异常值先**标记**再分层分析，避免一刀切删除

## 七、数据库

项目附带 `data/schema.sql`，用于快速在关系型数据库中创建 `events` 表及常用索引。

## 八、许可证

MIT
