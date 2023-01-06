### Program 4
# Write a program to demonstrate the working of the decision tree based ID3 algorithm. Use an  appropriate data set for building the decision tree and apply this knowledge to classify a new  sample

### Algorithm
1) Observing the dataset
2) Importing the necessary Python libraries
3) Reading the dataset
4) Calculate the entropy of the dataset
```math
H(x) = -p_{+}log_{2}p_{+}-p_{-}log_{2}p_{-}
```
5) Calculating the information gain
- We use the partial deviate of each variable relative to all other variables to measure the information gain of each attribute
```math
G(x, A) = H(x) - \sum_{V \epsilon values(A)} \frac{|S_{v}|}{S} H(S_{v})
```
6) Finding the most informative feature
7) Adding the mode to the thee
8) Repeat Step 4-8.

### Program

```python
import pandas as pd
from pprint import pprint
from sklearn.feature_selection import mutual_info_classif
from collections import Counter


def id3(df, target_attribute, attribute_names, default_class=None):
    cnt = Counter(x for x in df[target_attribute])
    if len(cnt) == 1:
        return next(iter(cnt))

    elif df.empty or (not attribute_names):
        return default_class

    else:
        gainz = mutual_info_classif(df[attribute_names], df[target_attribute], discrete_features=True)
        index_of_max = gainz.tolist().index(max(gainz))
        best_attr = attribute_names[index_of_max]
        tree = {best_attr: {}}
        remaining_attribute_names = [i for i in attribute_names if i != best_attr]

        for attr_val, data_subset in df.groupby(best_attr):
            subtree = id3(data_subset, target_attribute, remaining_attribute_names, default_class)
            tree[best_attr][attr_val] = subtree

        return tree

df = pd.read_csv("tennisdata.csv")

attribute_names = df.columns.tolist()
print("List of attribut name")

attribute_names.remove("PlayTennis")

for colname in df.select_dtypes("object"):
    df[colname], _ = df[colname].factorize()

print(df)

tree = id3(df, "PlayTennis", attribute_names)
print("The tree structure")
pprint(tree)
```

### Result
```
List of attribut name
    Outlook  Temperature  Humidity  Windy  PlayTennis
0         0            0         0      0           0
1         0            0         0      1           0
2         1            0         0      0           1
3         2            1         0      0           1
4         2            2         1      0           1
5         2            2         1      1           0
6         1            2         1      1           1
7         0            1         0      0           0
8         0            2         1      0           1
9         2            1         1      0           1
10        0            1         1      1           1
11        1            1         0      1           1
12        1            0         1      0           1
13        2            1         0      1           0
The tree structure
{'Outlook': {0: {'Humidity': {0: 0, 1: 1}}, 1: 1, 2: {'Windy': {0: 1, 1: 0}}}}
```
