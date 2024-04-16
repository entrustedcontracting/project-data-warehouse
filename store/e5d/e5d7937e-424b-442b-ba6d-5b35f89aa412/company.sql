ATTACH TABLE _ UUID 'b70b9081-b17b-4367-a8cb-f180bfb9a2c5'
(
    `company_id` String,
    `name` String,
    `website` String,
    `linkedin_url` String,
    `inferred_employee_count` String,
    `industry` String,
    `city` String,
    `state` String,
    `zip_code` Int64,
    `street_address` String,
    `founded` Int64,
    `is_referral_source` Bool
)
ENGINE = MergeTree
ORDER BY company_id
SETTINGS index_granularity = 8192
