import user_input as input
import formulas




    #create Linear equations for supply/demand
line_data_supply_demand = formulas.demand_linear_equation_for_supply_demand(input.quantity_demanded, input.price_demanded)
#supplyLine = demand_linear_equation_for_supply_demand(quantity_supplied, price_supplied)

print(f"Supply and Demand Lines: {line_data_supply_demand}")



    #predict values with the given lines
predicted_demand_quantity, predicted_demand_price = formulas.predict_values(line_data_supply_demand)
#predicted_supply_quantity, predicted_supply_price = predict_values(line_data_supply_demand)





    #new supply and demand data points predicted with actual represented by linear equation         
    #Sorting may be required, I think it's doubtful but will leave in commented just in case.

newquantity_demanded = list(input.quantity_demanded) + predicted_demand_quantity
#newquantity_demanded.sort()

newprice_demanded = list(input.price_demanded) + predicted_demand_price
#newprice_demanded.sort(reverse=True)


new_quantity_supplied = list(input.quantity_supplied) + input.predicted_supply_quantity
#new_quantity_supplied.sort()

new_price_supplied = list(input.price_supplied) + input.predicted_supply_price
#new_price_supplied.sort()





    #create dictionaries of supply and demand lists
supply_demand_dict = formulas.data_dict(newquantity_demanded, "quantity_d", newprice_demanded, "price_d", new_quantity_supplied, "quantity_s", new_price_supplied, "price_s")
#supply_dict = data_dict(new_quantity_supplied, "quantity_s", new_price_supplied, "price_s")
"""
Will show every data point alot the supply&demand demand curve: 
print(supply_demand_dict)
"""



