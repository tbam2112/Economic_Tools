import matplotlib.pyplot as plt



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

