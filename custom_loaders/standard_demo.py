import dtale
import pandas as pd

if __name__ == "__main__":
    df = pd.DataFrame([1, 2, 3, 4, 5])
    dtale.show(df, subprocess=False)
