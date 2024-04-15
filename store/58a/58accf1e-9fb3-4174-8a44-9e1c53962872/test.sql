ATTACH TABLE _ UUID 'ab5bddf6-2c40-42f2-a6bc-43caf1f441f1'
(
    `id` Int32,
    `name` String,
    `age` UInt8
)
ENGINE = MergeTree
ORDER BY id
SETTINGS index_granularity = 8192
