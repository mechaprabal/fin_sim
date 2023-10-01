from flask import Flask, render_template, request
from financial_mc import fin_mc

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


font = {"family": "Palatino Linotype", "weight": "bold", "size": 16}

mpl.rc("font", **font)
plt.style.use("ggplot")

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    """
    Homepage
    """
    if request.method == "POST":
        form_res = request.form

        sales_data, avg_profit, all_profit_list = fin_mc(
            profit_low=int(form_res.get("profit_l")),
            profit_high=int(form_res.get("profit_h")),
            n_leads_low=int(form_res.get("leads_l")),
            n_leads_high=int(form_res.get("leads_h")),
            r_low=float(form_res.get("conv_l")),
            r_high=float(form_res.get("conv_h")),
            lc_low=float(form_res.get("lc_l")),
            lc_high=float(form_res.get("lc_h")),
            f_overhead=int(form_res.get("overhead")),
            n_iter=int(form_res.get("nsim")),
        )

        sim_fig = simulation_chart(data=all_profit_list)

        user_text = f"Average Profits for all periods is: {avg_profit}"
        return render_template(
            "home.html", 
            avg_profit=avg_profit, 
            user_text=user_text,
        )
    else:
        user_text = "Submit the form to generate results"
        return render_template("home.html", user_text=user_text)

@app.route("/about/")
def about():
    '''
    About Page
    '''
    return render_template("about.html")

def simulation_chart(data):
    """
    Function to plot charts of simulation
    """
    fig, ax = plt.subplots(figsize=(11,6))

    ax.plot(
        range(len(data)),
        data, ".b-"
    )

    ax.set_title("Overall Profits")
    ax.set_xlabel("Periods")
    ax.set_ylabel("Profit")

    # ax.set_xticks(np.arange(len(data)))

    ax.set_xlim(xmin=0)
    # ax.set_ylim(ymin=0)

   
    fig.savefig("./static/profit_sim.png", bbox_inches="tight", dpi=300)

    return fig


if __name__ == "__main__":
    app.run(debug=True)
