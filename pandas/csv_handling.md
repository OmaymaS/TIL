
Read and combine multiple CSVs
```
import pandas as pd
import glob

## read all CSVs in a sub-directory
all_filenames = [filename for filename in glob.glob(f'{COMPLETIONS_CONVERTED_DIR}/*/*.csv')]

## combine CSV
combined_csv = pd.concat([pd.read_csv(f, sep = ",") for f in all_filenames])
```