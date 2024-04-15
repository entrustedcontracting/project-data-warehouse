ATTACH TABLE _ UUID 'd7b270d0-700e-4101-8a6e-b3bbd51d9e75'
(
    `company_id` String,
    `name` String,
    `website` Nullable(String),
    `linkedin_url` Nullable(String),
    `inferred_employee_count` Nullable(Int64),
    `industry` String,
    `city` String,
    `state` String,
    `zip_code` Nullable(String),
    `street_address` Nullable(String),
    `founded` Nullable(Int64),
    `is_referral_source` Bool
)
ENGINE = MergeTree
PRIMARY KEY company_id
ORDER BY company_id
SETTINGS index_granularity = 8192
