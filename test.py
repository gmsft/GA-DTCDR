import pandas as pd
file = './Data/amazon_clothing/reviews.json'
df = pd.DataFrame()
f = open(file, 'r')
for line in f:
    print(line)
    line_df = pd.read_json(line)
    print(line_df)
    df = df.append(line_df)
    print(df.drop_duplicates())
    break
print(df)
print(df.shape)