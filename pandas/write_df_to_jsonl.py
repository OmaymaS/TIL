import pandas as pd
import json

df = pd.DataFrame({'url': ['https://page.com/p1', 'https://page.com/p2'],
                   'id': ['10010', '93945']})


with open('output.jsonl', 'w') as f:
    for _, row in df.iterrows():
        json.dump(row.to_dict(), f, ensure_ascii=False)
        _ = f.write('\n')