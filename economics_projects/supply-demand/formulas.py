


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



