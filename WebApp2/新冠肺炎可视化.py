import pandas as pd
from plotly.offline import plot
import plotly.express as px

dataset = pd.read_csv(r"G:\大三下\python\project\novel-corona-virus-2019-dataset\covid_19_data.csv")

figure = px.bar(dataset, x="Country/Region", y="Confirmed", color="Country/Region",
                hover_name="Country/Region", barmode="group", animation_frame="ObservationDate")
plot(figure)
