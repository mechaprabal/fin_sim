# ######### Profits (Y) = Income - Expenses ##########

# ############## Assumption: Income is solely from Sales

# Income = Sales * Profits per sale (P)
# Sales = sale leads per month (L) * Conversion rate in percentage (R)
# Expenses = Fixed Overhead (F) + Cost of Leads
# Cost of leads = Number of leads per month (L) * Cost of single lead (C)
# Y = (L*R*P) - (F+(L*C))

# #########System Variation
# # Profit (P) - 47 - 53
# # Leads (L) - 1200 - 1800
# # Conversion (R) - 1% - 5%
# # Lead Cost - 0.2 - 0.8


import numpy as np

def gen_random_uniform(low, high):
    '''
    Generate a uniform random number
    '''
    return np.random.uniform(low=low, high=high)

def fin_mc(
    profit_low=47,
    profit_high=53,
    n_leads_low=1200,
    n_leads_high=1800,
    r_low=0.01,
    r_high=0.05,
    lc_low=0.2,
    lc_high=0.8,
    f_overhead=800,
    n_iter=10000,
):
    """
    Function to evaluate financial profits
    using Monte Carlo Simulations
    """
    sales_data = []

    for i in range(n_iter):
        profit = gen_random_uniform(low=profit_low, high=profit_high)
        leads = gen_random_uniform(low=n_leads_low, high=n_leads_high)
        conversion = gen_random_uniform(low=r_low, high=r_high)
        lead_cost = gen_random_uniform(low=lc_low, high=lc_high)

        overall_profit = (leads*conversion*profit) - (f_overhead + (leads*lead_cost))

        sales_data.append({
            "sim":i+1,
            "profit": profit,
            "leads": leads,
            "conversion": conversion,
            "lead_cost": lead_cost,
            "overall_profit": overall_profit,
        })

        print(f"Overall Profit for period {i+1}: {overall_profit}")
    
    all_profits = [sale["overall_profit"] for sale in sales_data]

    print(all_profits)

    print(f"Average profit for {n_iter} periods is: {np.mean(all_profits)}")

    return


if __name__ == "__main__":
    fin_mc()
