import pandas as pd
import numpy as np

def get_6_random_var_df():
    df = pd.DataFrame()
    df["x"] = np.random.uniform(-10, 10, 100)
    df["y"] = np.random.uniform(-10, 10, 100)
    df["z"] = np.random.uniform(-10, 10, 100)
    df["a"] = np.random.uniform(-180, 180, 100)
    df["b"] = np.random.uniform(-180, 180, 100)
    df["g"] = np.random.uniform(-180, 180, 100)
    df.to_csv("data/6_random_vars.csv", index=False)

