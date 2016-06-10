CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

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