import pandas as pd
import data_storage as data
import user_input as input
import models


""" 
    Utilizing the information pulled from formulas.py, data_storage.py, models.py, and user_input.py.
    Main.py creates a DataFrame with the stored data to display a model for optimal (profit | Demand).
    Through the variables max_profit_... and prints the results to the terminal as well as desplays a model.

"""

# I needed to assign each key/value for supply and demand from "supply_demand_dict" to the 4 variables below due to,
# each key having different lengths for creating a Data Frame.

quantity_d_key = data.supply_demand_dict["quantity_d"]
price_d_key = data.supply_demand_dict["price_d"]

quantity_s_key = data.supply_demand_dict["quantity_s"]
price_s_key = data.supply_demand_dict["price_s"]

   
    
demand_DF = pd.DataFrame({
    'price_d': price_d_key,
    'Quantity Demanded': quantity_d_key, 
    })
demand_DF['Total Profit'] = demand_DF['Quantity Demanded'] * (demand_DF.price_d - input.cost)

supply_DF = pd.DataFrame({
    'price_s': price_s_key,
    'Quantity Supplied': quantity_s_key,
    })
supply_DF['Total Profit'] = supply_DF['Quantity Supplied'] * (supply_DF.price_s - input.cost)


  
    
max_profit_data_points = demand_DF.loc[demand_DF['Total Profit'].idxmax()]
max_profit_dict = max_profit_data_points.to_dict()



    
print(f"The best price to sell is:\n{max_profit_data_points}")

finalProduct = models.create_sd_graph(demand_DF, 'Quantity Demanded', 'price_d', supply_DF, 'Quantity Supplied', 'price_s', max_profit_data_points)


