import plotly.express as px

df = px.data.iris()
print(df)
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
fig.show()