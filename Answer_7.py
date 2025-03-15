# Check the number of rows and columns in the dataset.

import pandas as pd

df = pd.read_csv('retail_data.csv')
print("The shape of the DataFrame is:", df.shape)


"""Output:
The shape of the DataFrame is: (293911, 30)
"""