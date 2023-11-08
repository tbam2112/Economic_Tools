import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
#import random

    # on both tables 
    #   x = quantity
    #   y = price
    #   (x,y) table points

####################################################
# Input your imperical data into the variables;    #
# quantity/price_demanded, and quantity/price_supplied #
#                                                  #
#                     #Below#                      #
####################################################


###Input META data here###
quantity_demanded = [82, 423] #Test with (82, 423)
price_demanded = [1100,875] #Test with (1100, 875)

quantity_supplied = [0, 845]    #Test with (0, 1450)
price_supplied = [0, 647]       #Test with (0, 542)

cost = 336  #Test with 336

"""Create an input asking if user would like to predict points along the curves.
        1. ask user to input their data points in for quantity demanded seperated by commas a,b,c,d,e. Then the same for price demanded.
        2. ask the user if they want to input supply data y/n.
        3. repeat step 1 but for supply.
       
        
"""

predicted_demand_quantity = []
predicted_demand_price = []

predicted_supply_quantity = []
predicted_supply_price = []


    #Linear equation for supply and demand lines,
    #Key:Value = {y-intercept: b, slope: m}
line_data_supply_demand = {}

optimal_price_for_demand = []


"""
Irrelevent at the moment may implement later.

#Demand by location/Type
amsterdam_demand_rec = 6830
rio_demand_rec = 4978

total_rec_demand = amsterdam_demand_rec + rio_demand_rec
#print(total_rec_demand)

amsterdam_demand_speed = 4415
rio_demand_speed = 2304

total_speed_demand = amsterdam_demand_speed + rio_demand_rec
#print(total_speed_demand)
"""




"""
    This function finds the linear equation (y = mx + b) for the demand curve,
    With this information it assumes the supply curve being the negative reciprical of the demand curve,
    The end goal will be to utilize the demand curve to find the optimal price for maximum profit given demand.   
"""
def demand_linear_equation_for_supply_demand(x,y):
    #find slope (m)
    m = (y[1]-y[0])/(x[1]-x[0])

    #find y-intercept (b)
    b = y[0] - (m*x[0])

    #find negative reciprical of demand line
    r = (1/m)*(-1)

    #create line dictionary Keys: y-intercept, slope
    return {
        "Demand Intercept": round(b,4),
        "Demand Slope": round(m,4),
        "Supply Slope": round(r,4),
        "Supply Intercept": 0
    }




    #Predict (x,y) values given the slope and y-intercept.
    #
def predict_values(line_dictionary):
    
    #Predict x values for a range of random y values.

    #:param slope: demandLine/supplyLine "slope": value.
    #:param y_intercept: demandLine/supplyLine "intercept": value.
    #:param num_values: The number of x values to predict.
    #:return: A list of predicted x values for random y values.
    
    predicted_quantity = []
    predicted_price = []
    slope = line_dictionary["Demand Slope"]
    y_intercept = line_dictionary["Demand Intercept"]

    x = range(round(y_intercept))
    for n in x:
            #Predict the x value for the given y value, 
            #and return to list predicted_quantity.
        x_value = round((n - y_intercept) / slope)
        
        if x_value >= 0:
                #append (x,y)
            predicted_price.append(n)
            predicted_quantity.append(x_value)

            #Return Predicted (x,y) values lists
    return predicted_quantity, predicted_price




    #Create a dictionary for a supply/demand dataframe
    #new_quantity_supplied, "quantity_s", new_price_supplied, "price_s"
def data_dict(dx, dx_n, dy, dy_n, sx ,sx_n, sy, sy_n):
    
    return {
        dy_n: dy,
        dx_n: dx,
        sy_n: sy,
        sx_n: sx
    }




    #Creates the supply & demand graph
def create_sd_graph(demand_df,demand_df_col_1, demand_df_col_2, supply_df, supply_df_col_1, supply_df_col_2, max_profit):
    demand_df
    supply_df = supply_df
    max_profit = max_profit
    fig, ax = plt.subplots()

    ax.plot(demand_df[demand_df_col_1], demand_df[demand_df_col_2], label = 'Demand')
    ax.plot(supply_df[supply_df_col_1], supply_df[supply_df_col_2], label = 'Supply')

    ax.set_xlabel('Quantity')
    ax.set_ylabel('Price')
    ax.set_title('Supply and Demand Graph')
    ax.legend()

    total_profit = max_profit['Total Profit']

    annotation_text = f"The best price point to sell is:\n\\${max_profit['price_d']} for a profit of \\${total_profit:,.0f}\nat {max_profit['Quantity Demanded']} units."
    x_coord = max_profit['Quantity Demanded']
    y_coord = max_profit['price_d']
    ax.plot(x_coord,y_coord,'ro')

    plt.annotate(annotation_text, (0, 0), xytext=(50,5), textcoords='offset points',
                fontsize=10, color='black')
    #plt.grid()
    plt.show()



###########################################################


    #create Linear equations for supply/demand
line_data_supply_demand = demand_linear_equation_for_supply_demand(quantity_demanded, price_demanded)
#supplyLine = demand_linear_equation_for_supply_demand(quantity_supplied, price_supplied)

print(f"Supply and Demand Lines: {line_data_supply_demand}")




    #predict values with the given lines
predicted_demand_quantity, predicted_demand_price = predict_values(line_data_supply_demand)
#predicted_supply_quantity, predicted_supply_price = predict_values(line_data_supply_demand)



    #new supply and demand data points predicted with actual represented by linear equation         Sorting may be required, I think it's doubtful but will leave in commented just in case.
newquantity_demanded = list(quantity_demanded) + predicted_demand_quantity
#newquantity_demanded.sort()

newprice_demanded = list(price_demanded) + predicted_demand_price
#newprice_demanded.sort(reverse=True)


new_quantity_supplied = list(quantity_supplied) + predicted_supply_quantity
#new_quantity_supplied.sort()

new_price_supplied = list(price_supplied) + predicted_supply_price
#new_price_supplied.sort()


    #create dictionaries of supply and demand lists
supply_demand_dict = data_dict(newquantity_demanded, "quantity_d", newprice_demanded, "price_d", new_quantity_supplied, "quantity_s", new_price_supplied, "price_s")
#supply_dict = data_dict(new_quantity_supplied, "quantity_s", new_price_supplied, "price_s")
"""
Will show every data point alot the supply&demand demand curve: 
print(supply_demand_dict)
"""




"""
I needed to assign each key/value for supply and demand from "supply_demand_dict" to the 4 variables below due to,
each key having different lengths for creating a Data Frame.
"""
quantity_d_key = supply_demand_dict["quantity_d"]
price_d_key = supply_demand_dict["price_d"]

quantity_s_key = supply_demand_dict["quantity_s"]
price_s_key = supply_demand_dict["price_s"]


    #create Data Frames from the new lists above!
demand_DF = pd.DataFrame({
    'price_d': price_d_key,
    'Quantity Demanded': quantity_d_key, 
    })
demand_DF['Total Profit'] = demand_DF['Quantity Demanded'] * (demand_DF.price_d - cost)

supply_DF = pd.DataFrame({
    'price_s': price_s_key,
    'Quantity Supplied': quantity_s_key,
    })
supply_DF['Total Profit'] = supply_DF['Quantity Supplied'] * (supply_DF.price_s - cost)


    #Returns the row in the DataFrame that holds the values to create max profits.
max_profit_data_point = demand_DF.loc[demand_DF['Total Profit'].idxmax()]
max_profit_dict = max_profit_data_point.to_dict()


    #Completed Product!!!!
    #Print the data shown in the model to the terminal
print(f"The best price to sell is:\n{max_profit_data_point}")

    #Supply and Demand visuals
finalProduct = create_sd_graph(demand_DF, 'Quantity Demanded', 'price_d', supply_DF, 'Quantity Supplied', 'price_s', max_profit_data_point)


