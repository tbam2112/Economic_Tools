########################################################
# Input your imperical data into the variables;        #
# quantity/price_demanded, and quantity/price_supplied #
#                                                      #
#                     #Below#                          #
########################################################

"""
Create an input asking if user would like to predict points along the curves.
        1. ask user to input their data points in for quantity demanded seperated by commas a,b,c,d,e. Then the same for price demanded.
        2. ask the user if they want to input supply data y/n.
        3. repeat step 1 but for supply.
"""  

###Input META data here###
    # on both tables 
    #   x = quantity
    #   y = price
    #   (x,y) table points

quantity_demanded = [82, 423] # Test with (82, 423)
price_demanded = [1100,875]   # Test with (1100, 875)

quantity_supplied = [0, 845]  # Test with (0, 1450)
price_supplied = [0, 647]     # Test with (0, 542)

cost = 336                    # Test with (336)


predicted_demand_quantity = []
predicted_demand_price = []

predicted_supply_quantity = []
predicted_supply_price = []




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