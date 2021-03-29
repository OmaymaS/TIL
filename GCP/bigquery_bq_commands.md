
- Create a dataset

```
bq mk dataset_name
```

- Create a table with schema

```
bq mk --time_partitioning_field timestamp \
  --table dataset_name.new_table_name\
  column1:STRING,column2:INT64,column3:TIMESTAMP
```