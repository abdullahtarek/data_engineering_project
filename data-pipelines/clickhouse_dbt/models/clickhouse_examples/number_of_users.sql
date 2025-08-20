
{{ config(materialized='table') }}

select count(distinct id) as number_of_all_users from s3_test_table

