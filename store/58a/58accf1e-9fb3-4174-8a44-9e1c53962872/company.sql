ATTACH TABLE _ UUID 'b0435fcd-f67e-4206-8443-f148737ffb36'
(
    `company_id` UUID,
    `name` String,
    `website` Nullable(String),
    `linkedin_url` Nullable(String),
    `size` Nullable(String),
    `industry` String,
    `city` String,
    `state` String,
    `zip_code` Nullable(String),
    `street_address` Nullable(String),
    `business_phone` Nullable(String),
    `claims_phone` Nullable(String),
    `year_founded` Nullable(Float32),
    `type` String,
    `updated_at` DateTime DEFAULT now(),
    `updated_at_date` Date DEFAULT toDate(updated_at)
)
ENGINE = ReplacingMergeTree
PRIMARY KEY company_id
ORDER BY company_id
SETTINGS index_granularity = 8192
