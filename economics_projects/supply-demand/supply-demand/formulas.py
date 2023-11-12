


"""
    This function finds the linear equation (y = mx + b) for the demand curve,
    With this information it assumes the supply curve being the negative reciprical of the demand curve,
    The end goal will be to utilize the demand curve to find the optimal price for maximum profit given demand. 
    
    Definitions follow algebra rules:
    m = slope
    b = y-intercept
    r = negative reciprical of m  
"""
def demand_linear_equation_for_supply_demand(x,y):
    
    m = (y[1]-y[0])/(x[1]-x[0])
    b = y[0] - (m*x[0])
    r = (1/m)*(-1)

    return {
        "Demand Intercept": round(b,4),
        "Demand Slope": round(m,4),
        "Supply Slope": round(r,4),
        "Supply Intercept": 0
    }





"""
    Returns a list of predicted (x,y) values, given the slope and y-intercept.
"""    
def predict_values(line_dictionary):
    
    predicted_quantity = []
    predicted_price = []
    slope = line_dictionary["Demand Slope"]
    y_intercept = line_dictionary["Demand Intercept"]

    x = range(round(y_intercept))
    for y in x:

        x_value = round((y - y_intercept) / slope)
        
        if x_value >= 0:
                
            predicted_price.append(y)
            predicted_quantity.append(x_value)

    return predicted_quantity, predicted_price





"""   
    Create a dictionary for a supply/demand dataframe
    paramater names: 
    (x, y) = (quantity, price)
    (d, s) = (demand, supply)
    
    dx,sx = variables for quantity data  
    dx_n,sx_n = desired key name for values 
    
    example -   data_dict(newquantity_demanded, "quantity_d", newprice_demanded, "price_d", new_quantity_supplied, "quantity_s", new_price_supplied, "price_s"
"""

def data_dict(dx, dx_n, dy, dy_n, sx ,sx_n, sy, sy_n):
    
    return {
        dy_n: dy,
        dx_n: dx,
        sy_n: sy,
        sx_n: sx
    }



