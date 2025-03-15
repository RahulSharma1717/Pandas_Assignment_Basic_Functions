# Display 8 bottom rows.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
print(df.tail(8))


"""Output:
        Transaction_ID  Customer_ID            Name                     Email  \
293903         8961631        79479     Jason Welch         Jason36@gmail.com   
293904         2844206        18799      Angel Hood        Joseph24@gmail.com   
293905         4833982        94117       Kara Hart         Tammy37@gmail.com   
293906         4246475        12104    Meagan Ellis      Courtney60@gmail.com   
293907         1197603        69772     Mathew Beck      Jennifer71@gmail.com   
293908         7743242        28449      Daniel Lee  Christopher100@gmail.com   
293909         9301950        45477  Patrick Wilson       Rebecca65@gmail.com   
293910         2882826        53626  Dustin Merritt       William14@gmail.com   

             Phone                        Address        City  \
293903  6279294104                764 Garcia Flat    Hamilton   
293904  2825444712    7593 Joseph Trace Suite 382      Cairns   
293905  7108672468  872 Robinson Harbors Apt. 328   Charlotte   
293906  7466353743         389 Todd Path Apt. 159  Townsville   
293907  5754304957              52809 Mark Forges     Hanover   
293908  9382530370   407 Aaron Crossing Suite 495    Brighton   
293909  9373222023                3204 Baird Port     Halifax   
293910  9518926645            143 Amanda Crescent      Tucson   

                  State  Zipcode    Country  Age  Gender  Income  \
293903          Ontario    61218     Canada   63    Male     Low   
293904  New South Wales    39837  Australia   41    Male  Medium   
293905         Missouri    65301        USA   54    Male    High   
293906  New South Wales     4567  Australia   31    Male  Medium   
293907           Berlin    16852    Germany   35  Female     Low   
293908          England    88038         UK   41    Male     Low   
293909          Ontario    67608     Canada   41    Male  Medium   
293910    West Virginia    25242        USA   28  Female     Low   

       Customer_Segment        Date  Year      Month      Time  \
293903              New  09-06-2023  2023  September  17:37:41   
293904          Premium   5/28/2023  2023        May  13:11:33   
293905              New  10/14/2023  2023    October  15:06:09   
293906          Regular   1/20/2024  2024    January  23:40:29   
293907              New  12/28/2023  2023   December  02:55:45   
293908          Premium   2/27/2024  2024   February  02:43:49   
293909              New  09-03-2023  2023  September  11:20:31   
293910          Premium  01-08-2024  2024    January  11:44:36   

        Total_Purchases      Amount  Total_Amount Product_Category  \
293903                6  443.329498   2659.976987       Home Decor   
293904                6  397.452883   2384.717299      Electronics   
293905                5  472.424060   2362.120301         Clothing   
293906                5  194.792597    973.962984            Books   
293907                1  285.137301    285.137301      Electronics   
293908                3   60.701761    182.105285         Clothing   
293909                1  120.834784    120.834784       Home Decor   
293910                7  340.319059   2382.233417       Home Decor   

        Product_Brand Product_Type   Feedback Shipping_Method Payment_Method  \
293903     Home Depot        Tools  Excellent         Express           Cash   
293904          Apple       Tablet    Average        Same-Day           Cash   
293905           Nike       Shorts  Excellent        Standard           Cash   
293906  Penguin Books      Fiction        Bad        Same-Day           Cash   
293907          Apple       Laptop  Excellent        Same-Day           Cash   
293908         Adidas       Jacket    Average         Express           Cash   
293909           IKEA    Furniture       Good        Standard           Cash   
293910     Home Depot  Decorations    Average        Same-Day           Cash   

       Order_Status  Ratings            products  
293903      Pending        5               Level  
293904      Pending        2  Amazon Fire Tablet  
293905    Delivered        4        Chino shorts  
293906   Processing        1  Historical fiction  
293907   Processing        5             LG Gram  
293908      Shipped        2               Parka  
293909      Shipped        4            TV stand  
293910      Shipped        2              Clocks 
"""