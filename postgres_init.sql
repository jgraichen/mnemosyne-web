CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE traces(
trace_uuid uuid PRIMARY KEY,
transaction_uuid uuid,
origin_uuid uuid,
trace_name text,
start_time timestamp(6),
end_time timestamp(6),
meta jsonb
)

CREATE TABLE spans(
trace_uuid uuid,
span_name text,
start_time timestamp(6),
end_time timestamp(6),
meta jsonb,
FOREIGN KEY (trace_uuid) REFERENCES traces(trace_uuid)
)