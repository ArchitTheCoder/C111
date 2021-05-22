import csv
from os import stat
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("int2.csv")
data = df["Math_score"].tolist()
  
# pop_mean = statistics.mean(data)
# pop_stdev = statistics.stdev(data)

# print("Mean is {} and stdev is {}".format(pop_mean, pop_stdev))

def rand_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(1, len(data)-1)
        val = data[random_index]
        dataset.append(val)
    sample_mean = statistics.mean(dataset)
    return sample_mean

sample_mean_list = []

for i in range(0, 1000):
    setofmeans = rand_mean(100)
    sample_mean_list.append(setofmeans)

mean = statistics.mean(sample_mean_list)
# print("Mean of sample is {}".format(mean))
std = statistics.stdev(sample_mean_list)

# fig = ff.create_distplot([sample_mean_list], ["Math_score"], show_hist=False)
# fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.20], mode = "lines", name="MEAN"))
# fig.show()      

first_stdev_start, first_stdev_end = mean - std, mean + std

second_stdev_start, second_stdev_end = mean - (2*std), mean + (2*std)

third_stdev_start, third_stdev_end = mean - (3*std), mean + (3*std)

mean_of_sample2 = statistics.mean(data)
# print(mean_of_sample2)

fig = ff.create_distplot([sample_mean_list], ["Math_score"], show_hist=False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.60], mode = "lines", name="MEAN"))
fig.add_trace(go.Scatter(x = [mean_of_sample2, mean_of_sample2], y = [0, 0.60], mode = "lines", name="Mean of Sample 2"))
fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.60], mode = "lines", name="First Stdev End"))
fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.60], mode = "lines", name="Second Stdev End"))

# fig.show() 

z_score = (mean_of_sample2-mean)/std
print(z_score)

