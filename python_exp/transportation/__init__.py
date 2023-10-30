import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

INPUT_FILEPATH =os.path.join(os.path.dirname(__file__), "traveltracking.csv")
OUTPUT_FILEPATH =os.path.join(os.path.dirname(__file__), "traveltracking.png")
MEANS_LABELS = {
    "bicycle": "Bicycle (Xe đạp)",
    "motorcycle": "Motorcycle (Xe máy)",
    "foot": "Foot (Đi bộ)",
    "bus": "Bus (Xe buýt)",
    "car": "Car (Ô tô)",
    "motorcoach": "Motorcoach (Xe khách)",
    "plane": "Plane (Máy bay)",
}
TITLE = "Kilometers traveled by different means in August 2022 (Km di chuyển bằng các phương tiện trong tháng 8 năm 2022)"

if __name__ == "__main__":
    df = pd.read_csv(INPUT_FILEPATH)
    # parse date column
    df['date'] = pd.to_datetime(df['date'], format="%Y/%m/%d")

    # filter month of interest
    in_month = df.loc[df['date'].dt.month == 9]

    # group by means and sum kilometers and minutes
    by_means = in_month.groupby("means").sum().reset_index()
    # add percentage column
    by_means["percentage"] = by_means["kilometers"] * 100 / by_means["kilometers"].sum()

    # filter out rows with 0 kilometers
    by_means = by_means.loc[by_means["kilometers"] > 0]

    # map means with labels
    by_means = by_means.replace({"means": MEANS_LABELS})

    # bar plot
    # plt.figure(figsize=(7.195, 3.841), dpi=100)
    ax = sns.barplot(data=by_means, x="means", y="kilometers")
    for index, row in by_means.iterrows():
        text = "{0:d} ({1:.2f}%)".format(int(row["kilometers"]), row["percentage"])
        ax.text(row.name, row.kilometers + 5, text, color='black', ha="center")

    ax.set_title(TITLE)
    plt.tight_layout()

    # plt.legend()
    plt.show()
    # plt.savefig(OUTPUT_FILEPATH, dpi=1000)
