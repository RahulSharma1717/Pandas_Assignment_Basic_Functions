# Check out the information on all the columns of the dataset.

import pandas as pd

df = pd.read_csv('retail_data.csv')
print(df.info())


"""Output:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 293911 entries, 0 to 293910
Data columns (total 30 columns):
 #   Column            Non-Null Count   Dtype  
---  ------            --------------   -----  
 0   Transaction_ID    293911 non-null  int64  
 1   Customer_ID       293911 non-null  int64  
 2   Name              293911 non-null  object 
 3   Email             293911 non-null  object 
 4   Phone             293911 non-null  int64  
 5   Address           293911 non-null  object 
 6   City              293911 non-null  object 
 7   State             293911 non-null  object 
 8   Zipcode           293911 non-null  int64  
 9   Country           293911 non-null  object 
 10  Age               293911 non-null  int64  
 11  Gender            293911 non-null  object 
 12  Income            293911 non-null  object 
 13  Customer_Segment  293911 non-null  object 
 14  Date              293911 non-null  object 
 15  Year              293911 non-null  int64  
 16  Month             293911 non-null  object 
 17  Time              293911 non-null  object 
 18  Total_Purchases   293911 non-null  int64  
 19  Amount            293911 non-null  float64
 20  Total_Amount      293911 non-null  float64
 21  Product_Category  293911 non-null  object 
 22  Product_Brand     293911 non-null  object 
 23  Product_Type      293911 non-null  object 
 24  Feedback          293911 non-null  object 
 25  Shipping_Method   293911 non-null  object 
 26  Payment_Method    293911 non-null  object 
 27  Order_Status      293911 non-null  object 
 28  Ratings           293911 non-null  int64  
 29  products          293911 non-null  object 
dtypes: float64(2), int64(8), object(20)
memory usage: 67.3+ MB
None
"""