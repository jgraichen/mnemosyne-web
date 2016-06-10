CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

DROP INDEX IF EXISTS traces_start_time_index;

DROP TABLE IF EXISTS spans;
DROP TABLE IF EXISTS traces;
DROP TABLE IF EXISTS applications;

CREATE TABLE applications(
uuid uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
name text,
original_name text
);

CREATE TABLE traces(
uuid uuid PRIMARY KEY,
transaction_uuid uuid,
origin_uuid uuid,
application_uuid uuid,
name text,
start_time timestamp(6),
end_time timestamp(6),
meta jsonb,
FOREIGN KEY (application_uuid) REFERENCES applications(uuid)
);

CREATE TABLE spans(
trace_uuid uuid,
uuid uuid,
name text,
start_time timestamp(6),
end_time timestamp(6),
meta jsonb,
FOREIGN KEY (trace_uuid) REFERENCES traces(uuid)
);

CREATE INDEX traces_start_time_index ON traces(start_time);
