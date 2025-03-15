# Display the top 12 rows of the dataset.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
print(df.head(12))


"""Output:
    Transaction_ID  Customer_ID                 Name                Email  \
0          8691788        37249  Michelle Harrington    Ebony39@gmail.com   
1          2174773        69749          Kelsey Hill     Mark36@gmail.com   
2          6679610        30192         Scott Jensen    Shane85@gmail.com   
3          7232460        62101        Joseph Miller     Mary34@gmail.com   
4          4983775        27901        Debra Coleman  Charles30@gmail.com   
5          6095326        41289         Ryan Johnson    Haley12@gmail.com   
6          5434096        97285           Erin Lewis   Arthur76@gmail.com   
7          2344675        26603        Angela Fields    Tanya94@gmail.com   
8          4155845        80175          Diane Clark   Martin39@gmail.com   
9          4926148        31878            Lori Bell  Jessica33@gmail.com   
10         8493213        19136       Jonathan Eaton     Mark38@gmail.com   
11         1609659        66883      Brianna Oconnor    David47@gmail.com   

         Phone                       Address        City            State  \
0   1414786801             3959 Amanda Burgs    Dortmund           Berlin   
1   6852899987            82072 Dawn Centers  Nottingham          England   
2   8362160449             4133 Young Canyon     Geelong  New South Wales   
3   2776751724   8148 Thomas Creek Suite 100    Edmonton          Ontario   
4   9098267635     5813 Lori Ports Suite 269     Bristol          England   
5   3292677006    532 Ashley Crest Suite 014    Brisbane  New South Wales   
6   1578355423   600 Brian Prairie Suite 497   Kitchener          Ontario   
7   3668096144               237 Young Curve      Munich           Berlin   
8   6219779557  8823 Mariah Heights Apt. 263  Wollongong  New South Wales   
9   6004895059            6225 William Lodge     Cologne           Berlin   
10  2996714102               9772 Sosa Coves  Portsmouth          England   
11  9398168800  95471 Jerry Hollow Suite 034  Portsmouth          England   

    Zipcode    Country  Age  Gender  Income Customer_Segment        Date  \
0     77985    Germany   21    Male     Low          Regular   9/18/2023   
1     99071         UK   19  Female     Low          Premium  12/31/2023   
2     75929  Australia   48    Male     Low          Regular   4/26/2023   
3     88420     Canada   56    Male    High          Premium  05-08-2023   
4     48704         UK   22    Male     Low          Premium  01-10-2024   
5     74430  Australia   58  Female  Medium          Premium   9/21/2023   
6     47545     Canada   29  Female     Low              New   6/26/2023   
7     86862    Germany   29    Male  Medium          Premium   3/24/2023   
8     39820  Australia   46    Male  Medium              New  01-06-2024   
9     64317    Germany   25    Male  Medium              New  10-04-2023   
10    59280         UK   64  Female     Low          Regular   7/20/2023   
11    91253         UK   31  Female  Medium          Regular   6/21/2023   

    Year      Month      Time  Total_Purchases      Amount  Total_Amount  \
0   2023  September  22:03:55                3  108.028757    324.086270   
1   2023   December  08:42:04                2  403.353907    806.707815   
2   2023      April  04:06:29                3  354.477600   1063.432799   
3   2023        May  14:55:17                7  352.407717   2466.854021   
4   2024    January  16:54:07                2  124.276524    248.553049   
5   2023  September  23:24:27                4  296.291806   1185.167224   
6   2023       June  13:35:51                2  315.057648    630.115295   
7   2023      March  10:12:56                1   46.588070     46.588070   
8   2024    January  14:38:26                8  328.839302   2630.714413   
9   2023    October  22:27:40               10  397.611229   3976.112295   
10  2023       July  23:06:51                4   90.981870    363.927479   
11  2023       June  13:09:58                1  364.830567    364.830567   

   Product_Category  Product_Brand Product_Type   Feedback Shipping_Method  \
0          Clothing           Nike       Shorts  Excellent        Same-Day   
1       Electronics        Samsung       Tablet  Excellent        Standard   
2             Books  Penguin Books   Children's    Average        Same-Day   
3        Home Decor     Home Depot        Tools  Excellent        Standard   
4           Grocery         Nestle    Chocolate        Bad        Standard   
5       Electronics          Apple       Tablet       Good         Express   
6       Electronics        Samsung   Television        Bad        Standard   
7          Clothing           Zara        Shirt        Bad        Same-Day   
8           Grocery         Nestle    Chocolate        Bad        Same-Day   
9        Home Decor     Home Depot  Decorations  Excellent        Standard   
10       Home Decor     Home Depot        Tools    Average        Standard   
11            Books   Random House  Non-Fiction    Average        Standard   

   Payment_Method Order_Status  Ratings           products  
0      Debit Card      Shipped        5     Cycling shorts  
1     Credit Card   Processing        4         Lenovo Tab  
2     Credit Card   Processing        2   Sports equipment  
3          PayPal   Processing        4      Utility knife  
4            Cash      Shipped        1  Chocolate cookies  
5          PayPal      Pending        4         Lenovo Tab  
6            Cash   Processing        1            QLED TV  
7            Cash   Processing        1        Dress shirt  
8            Cash    Delivered        1     Dark chocolate  
9            Cash    Delivered        4            Candles  
10    Credit Card      Shipped        2    Screwdriver set  
11    Credit Card      Pending        2            Science
"""