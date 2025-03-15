# Create sample dataset of 10 rows from the existing dataset.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
print(df.sample(10))


"""Output:
        Transaction_ID  Customer_ID              Name                 Email  \
162315         2236914        14175    Katelyn Butler   Theresa20@gmail.com   
140569         6068670        68125    Patrick Garcia   Jillian26@gmail.com   
127211         8108001        24928   Jennifer Moreno     Mark100@gmail.com   
226035         3188547        46424  Christine Taylor   Charles69@gmail.com   
213102         2554065        85106     Tracy Simmons    Robert59@gmail.com   
289250         5114821        13524     Daniel Jarvis  Courtney73@gmail.com   
37029          4485742        89656        Tammy Webb    Robert42@gmail.com   
77427          1933234        70057     Karen Johnson  Jonathan25@gmail.com   
82577          7917637        43020   Margaret Murray     Kevin64@gmail.com   
137100         6440290        70411  Timothy Williams     Keith77@gmail.com   

             Phone                              Address           City  \
162315  9700804463         5444 Michael Street Apt. 093        Phoenix   
140569  8842620200                     45987 James Keys  San Francisco   
127211  4720081158          8207 Richard Manor Apt. 082    San Antonio   
226035  6914381426  45101 Christopher Islands Suite 724         Berlin   
213102  1781810977         80173 Foster Coves Suite 027      Toowoomba   
289250  6637917504         85203 Lindsey Glen Suite 778          Perth   
37029   3930295227         1216 Rodney Lights Suite 465       Hamilton   
77427   2159288748           332 Knight Summit Apt. 113        Chicago   
82577   8184946125             032 Caleb Coves Apt. 780        Chicago   
137100  2797918202                      9669 Ann Street       Winnipeg   

                  State  Zipcode    Country  Age  Gender  Income  \
162315      Connecticut     6240        USA   21    Male  Medium   
140569            Maine     7553        USA   26    Male    High   
127211     Pennsylvania    18289        USA   26    Male    High   
226035           Berlin    92144    Germany   19    Male     Low   
213102  New South Wales    79616  Australia   35  Female     Low   
289250  New South Wales    65121  Australia   20  Female     Low   
37029           Ontario    75197     Canada   22    Male     Low   
77427       Connecticut    56412        USA   34  Female  Medium   
82577       Connecticut    91251        USA   34    Male  Medium   
137100          Ontario    53096     Canada   26    Male    High   

       Customer_Segment        Date  Year     Month      Time  \
162315              New  02-09-2024  2024  February  03:59:08   
140569          Regular  12-10-2023  2023   January  06:01:00   
127211              New  10/26/2023  2023   October  11:02:21   
226035          Premium  03-06-2023  2023     March  12:31:30   
213102              New   3/28/2023  2023    August  13:07:58   
289250              New  04-12-2023  2023     April  06:14:25   
37029           Regular  12-12-2023  2023  December  19:24:45   
77427               New   2/27/2024  2024  February  08:34:29   
82577               New  04-05-2023  2023     April  16:32:58   
137100          Regular  02-02-2024  2024   January  08:20:36   

        Total_Purchases      Amount  Total_Amount Product_Category  \
162315                5   97.597070    487.985351         Clothing   
140569                6  280.835508   1685.013049         Clothing   
127211                9  417.570259   3758.132335       Home Decor   
226035                5  279.113305   1395.566524         Clothing   
213102                2  432.748314    865.496628            Books   
289250                1  359.842668    359.842668         Clothing   
37029                 1  196.250422    196.250422       Home Decor   
77427                 6  184.034951   1104.209707            Books   
82577                 9  150.860936   1357.748428          Grocery   
137100                5   26.387592    131.937958      Electronics   

            Product_Brand Product_Type   Feedback Shipping_Method  \
162315               Zara        Shirt    Average        Same-Day   
140569             Adidas       Jacket        Bad        Same-Day   
127211  Bed Bath & Beyond      Bedding       Good        Standard   
226035             Adidas      T-shirt  Excellent         Express   
213102       Random House      Fiction  Excellent        Standard   
289250             Adidas      T-shirt  Excellent         Express   
37029   Bed Bath & Beyond      Bedding        Bad         Express   
77427        Random House   Literature       Good         Express   
82577               Pepsi        Water       Good        Same-Day   
137100          Whirepool       Fridge       Good        Same-Day   

       Payment_Method Order_Status  Ratings            products  
162315         PayPal      Shipped        2        Henley shirt  
140569         PayPal    Delivered        1      Varsity jacket  
127211         PayPal    Delivered        3           Comforter  
226035           Cash   Processing        4          Henley tee  
213102           Cash      Pending        4              Horror  
289250    Credit Card    Delivered        5      Scoop neck tee  
37029      Debit Card    Delivered        1           Bed skirt  
77427     Credit Card      Pending        4         Anthologies  
82577     Credit Card   Processing        3      Artesian water  
137100           Cash    Delivered        4  Black refrigerator
"""