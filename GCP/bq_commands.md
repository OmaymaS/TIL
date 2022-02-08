### Create dataset 

Specify the following parameters:
```
DATASET_LOCATION='EU'
PROJECT_ID='gcp_project_name'
DATASET_ID='test_dataset'
```

Use `bq mk`:
```
bq --location=$DATASET_LOCATION --project_id=$PROJECT_ID mk --dataset $DATASET_ID
```

### Create a bq table from csv on gcs

specify schema:
```
SCHEMA='Elevation:INTEGER,Aspect:INTEGER,Slope:INTEGER,Horizontal_Distance_To_Hydrology:INTEGER,Vertical_Distance_To_Hydrology:INTEGER,Horizontal_Distance_To_Roadways:INTEGER,Hillshade_9am:INTEGER,Hillshade_Noon:INTEGER,Hillshade_3pm:INTEGER,Horizontal_Distance_To_Fire_Points:INTEGER,Wilderness_Area:STRING,Soil_Type:STRING,Cover_Type:INTEGER'
```
Specify table name and source csv
```
TABLE_ID='covertype'
DATA_SOURCE='gs://workshop-datasets/covertype/small/dataset.csv'
```

use `bq load`:
```
bq --project_id=$PROJECT_ID --dataset_id=$DATASET_ID load \
--source_format=CSV \
--skip_leading_rows=1 \ ## skip header in this case, default is 0
--replace \
$TABLE_ID \
$DATA_SOURCE \
$SCHEMA
```

### Create big query table from a query result

```
!bq query \
-n 0 \
--destination_table DATASET_NAME.NEW_TABLE_NAME \
--replace \
--use_legacy_sql=false \
'SELECT * \
FROM `DATASET_NAME.EXISTING_TABLE_NAME` AS cover \
LIMIT 10' 
```
###  Export data from bq 

```
!bq extract \
--destination_format CSV \
covertype_dataset.training \
gs://my_bucket/exported.csv 
```