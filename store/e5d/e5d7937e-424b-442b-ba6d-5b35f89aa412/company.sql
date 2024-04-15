ATTACH TABLE _ UUID '26eab1c0-1c04-47f5-ad9f-7ae8d7d473dd'
(
    `company_id` UUID,
    `name` String,
    `website` Nullable(String),
    `linkedin_url` Nullable(String),
    `inferred_employee_count` Nullable(Decimal(10, 0)),
    `industry` String,
    `city` String,
    `state` String,
    `zip_code` Nullable(String),
    `street_address` Nullable(String),
    `founded` Nullable(Decimal(10, 0)),
    `is_referral_source` Bool
)
ENGINE = MergeTree
PRIMARY KEY company_id
ORDER BY (company_id, is_referral_source)
SETTINGS index_granularity = 8192
