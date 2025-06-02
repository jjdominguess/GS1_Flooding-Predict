import openml as opml
import pandas as pd

dataset = opml.datasets.get_dataset(43459)

df, _, _, _ = dataset.get_data()

print(df.head())