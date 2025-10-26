-- Schema for events table used in ecommerce analytics pipeline
CREATE TABLE IF NOT EXISTS events (
    event_id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    session_id TEXT,
    event TEXT NOT NULL,
    ts TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    product_id TEXT,
    price NUMERIC,
    qty NUMERIC,
    device TEXT,
    city TEXT,
    channel TEXT
);

CREATE INDEX IF NOT EXISTS idx_events_user_ts ON events (user_id, ts);
CREATE INDEX IF NOT EXISTS idx_events_event_ts ON events (event, ts);
