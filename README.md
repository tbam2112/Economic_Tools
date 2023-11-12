# Economic_Tools
A place for my tools to help analyze data using economic principles

---------------------------------------------------------------------

# Supply-Demand
imports pandas, matplotlib
Project application that recommends the optimal price to sell a product from sales data. (#sold | price).

1). Ingest user sales data points for a (quantity sold | price sold for) relationship (x,y), and cost to produce the project.

2). Uses a function to create the demand curve line based on ingested data, and returns the information into a dictionary.

3). Then proceeds to predict (x,y) points along the demand curve, and creates a new dictionary "supply_demand_dict".

4). A Data Frame is created from supply_demand_dict, and then checks each row to determine the optimal price, where demand is greatest to create the most profit.
        &Tab(price-cost) * Demand = Profit

5). Important information is then printed to the terminal, and a supply & demand model is then created for visualization.
