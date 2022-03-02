## Example
```
import pandas as pd
df = pd.DataFrame({'id': [0, 1, 2], 'class': ['2 3', '1 3', '3 5']})
df['class'] = df['class'].apply(lambda x: x.split(' '))
df_long = df.explode('class')
df_one_hot_encoded = pd.concat([df, pd.get_dummies(df_long['class'],prefix='class', prefix_sep='_')], axis=1)
df_one_hot_encoded_compact = df_one_hot_encoded.groupby('id').max().reset_index()
```

## Details

Given this data

```
import pandas as pd
df = pd.DataFrame({'id': [0, 1, 2], 'class': ['2 3', '1 3', '3 5']})
```

1- split values

```
df['class'] = df['class'].apply(lambda x: x.split(' '))

df
   id   class
0   0  [2, 3]
1   1  [1, 3]
2   2  [3, 5]
```

2- explode --> each record in a row

```
df_long = df.explode('class')

df_long
   id class
0   0     2
0   0     3
1   1     1
1   1     3
2   2     3
2   2     5
```

3- get one hot encoded values

```
df_one_hot_encoded = pd.concat([df, pd.get_dummies(df_long['class'],prefix='class', prefix_sep='_')], axis=1)

df_one_hot_encoded
   id   class  class_1  class_2  class_3  class_5
0   0  [2, 3]        0        1        0        0
0   0  [2, 3]        0        0        1        0
1   1  [1, 3]        1        0        0        0
1   1  [1, 3]        0        0        1        0
2   2  [3, 5]        0        0        1        0
2   2  [3, 5]        0        0        0        1
```

4- groupby `id` and get the max value per column (same result of logical OR for binary values) --> one row per id

```
df_one_hot_encoded.groupby('id').max().reset_index()

   id   class  class_1  class_2  class_3  class_5
0   0  [2, 3]        0        1        1        0
1   1  [1, 3]        1        0        1        0
2   2  [3, 5]        0        0        1        1
```
