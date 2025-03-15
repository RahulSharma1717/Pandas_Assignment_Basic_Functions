# Display 5 rows from the bottom.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
print(df.tail())


"""Output:
        Transaction_ID  Customer_ID            Name                     Email  \
293906         4246475        12104    Meagan Ellis      Courtney60@gmail.com   
293907         1197603        69772     Mathew Beck      Jennifer71@gmail.com   
293908         7743242        28449      Daniel Lee  Christopher100@gmail.com   
293909         9301950        45477  Patrick Wilson       Rebecca65@gmail.com   
293910         2882826        53626  Dustin Merritt       William14@gmail.com   

             Phone                       Address        City            State  \
293906  7466353743        389 Todd Path Apt. 159  Townsville  New South Wales   
293907  5754304957             52809 Mark Forges     Hanover           Berlin   
293908  9382530370  407 Aaron Crossing Suite 495    Brighton          England   
293909  9373222023               3204 Baird Port     Halifax          Ontario   
293910  9518926645           143 Amanda Crescent      Tucson    West Virginia   

        Zipcode    Country  Age  Gender  Income Customer_Segment        Date  \
293906     4567  Australia   31    Male  Medium          Regular   1/20/2024   
293907    16852    Germany   35  Female     Low              New  12/28/2023   
293908    88038         UK   41    Male     Low          Premium   2/27/2024   
293909    67608     Canada   41    Male  Medium              New  09-03-2023   
293910    25242        USA   28  Female     Low          Premium  01-08-2024   

        Year      Month      Time  Total_Purchases      Amount  Total_Amount  \
293906  2024    January  23:40:29                5  194.792597    973.962984   
293907  2023   December  02:55:45                1  285.137301    285.137301   
293908  2024   February  02:43:49                3   60.701761    182.105285   
293909  2023  September  11:20:31                1  120.834784    120.834784   
293910  2024    January  11:44:36                7  340.319059   2382.233417   

       Product_Category  Product_Brand Product_Type   Feedback  \
293906            Books  Penguin Books      Fiction        Bad   
293907      Electronics          Apple       Laptop  Excellent   
293908         Clothing         Adidas       Jacket    Average   
293909       Home Decor           IKEA    Furniture       Good   
293910       Home Decor     Home Depot  Decorations    Average   

       Shipping_Method Payment_Method Order_Status  Ratings  \
293906        Same-Day           Cash   Processing        1   
293907        Same-Day           Cash   Processing        5   
293908         Express           Cash      Shipped        2   
293909        Standard           Cash      Shipped        4   
293910        Same-Day           Cash      Shipped        2   

                  products  
293906  Historical fiction  
293907             LG Gram  
293908               Parka  
293909            TV stand  
293910              Clocks  
"""