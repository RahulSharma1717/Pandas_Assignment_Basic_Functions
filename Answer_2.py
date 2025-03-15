# Display the top 5 rows of the dataset.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
print(df.head())


"""Output:
   Transaction_ID  Customer_ID                 Name                Email  \
0         8691788        37249  Michelle Harrington    Ebony39@gmail.com   
1         2174773        69749          Kelsey Hill     Mark36@gmail.com   
2         6679610        30192         Scott Jensen    Shane85@gmail.com   
3         7232460        62101        Joseph Miller     Mary34@gmail.com   
4         4983775        27901        Debra Coleman  Charles30@gmail.com   

        Phone                      Address        City            State  \
0  1414786801            3959 Amanda Burgs    Dortmund           Berlin   
1  6852899987           82072 Dawn Centers  Nottingham          England   
2  8362160449            4133 Young Canyon     Geelong  New South Wales   
3  2776751724  8148 Thomas Creek Suite 100    Edmonton          Ontario   
4  9098267635    5813 Lori Ports Suite 269     Bristol          England   

   Zipcode    Country  Age  Gender Income Customer_Segment        Date  Year  \
0    77985    Germany   21    Male    Low          Regular   9/18/2023  2023   
1    99071         UK   19  Female    Low          Premium  12/31/2023  2023   
2    75929  Australia   48    Male    Low          Regular   4/26/2023  2023   
3    88420     Canada   56    Male   High          Premium  05-08-2023  2023   
4    48704         UK   22    Male    Low          Premium  01-10-2024  2024   

       Month      Time  Total_Purchases      Amount  Total_Amount  \
0  September  22:03:55                3  108.028757    324.086270   
1   December  08:42:04                2  403.353907    806.707815   
2      April  04:06:29                3  354.477600   1063.432799   
3        May  14:55:17                7  352.407717   2466.854021   
4    January  16:54:07                2  124.276524    248.553049   

  Product_Category  Product_Brand Product_Type   Feedback Shipping_Method  \
0         Clothing           Nike       Shorts  Excellent        Same-Day   
1      Electronics        Samsung       Tablet  Excellent        Standard   
2            Books  Penguin Books   Children's    Average        Same-Day   
3       Home Decor     Home Depot        Tools  Excellent        Standard   
4          Grocery         Nestle    Chocolate        Bad        Standard   

  Payment_Method Order_Status  Ratings           products  
0     Debit Card      Shipped        5     Cycling shorts  
1    Credit Card   Processing        4         Lenovo Tab  
2    Credit Card   Processing        2   Sports equipment  
3         PayPal   Processing        4      Utility knife  
4           Cash      Shipped        1  Chocolate cookies  
"""