import pandas as pd
from pathlib import Path

datapath = Path("Labs") / "wk7" / "cmsc140-f22-lab7" / "city_temperature.csv"
df = pd.read_csv(datapath, sep=",")

hot = df.loc[df.groupby(["Region"])["AvgTemperature"].idxmax()]
outfile = Path("Labs") / "wk7" / "city_maxtemp.csv"

hot.to_csv(outfile, index=False)