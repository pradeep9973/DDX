#author: Pradeep Kumar
# we are going to implement the Hidden Markov Model in this file for the stock price prediction
# we are going to use the hmmlearn library for the implementation of the Hidden Markov Model
# we are going to use the stock price data of the Apple company for the prediction of the stock prices

# Importing the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from hmmlearn import hmm
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

# Loading the dataset
from src.utils.stock import Stock
stock = Stock("ZOMATO.NS")
data = stock.get_price_history_yf(interval="1d", period="5y")
# so here we have loaded the stock price data of the Apple company for the last 5 years and now we are going to implement a hidden markov model on this data

# I want to add a new column to the data frame that will contain the difference between the closing price of the current day and the closing price of the previous day
data["diff"] = data["Close"].diff()
data.dropna(inplace=True)

# Define the bins for the differences
bins = [-np.inf, -2, -1, 0, 1, 2, np.inf]

# Initialize the transition matrix with zeros
transition_matrix = np.zeros((len(bins) - 1, len(bins) - 1))

# Populate the transition matrix based on the actual differences
for i in range(1, len(data)):
    prev_diff = data["diff"].iloc[i - 1]
    curr_diff = data["diff"].iloc[i]
    print(prev_diff)
    print(curr_diff)
    prev_bin = np.digitize(prev_diff, bins) - 1
    print(prev_bin)
    curr_bin = np.digitize(curr_diff, bins) - 1
    print(curr_bin)
    transition_matrix[prev_bin][curr_bin] += 1

# Normalize the transition matrix to get probabilities
transition_matrix = transition_matrix / transition_matrix.sum(axis=1, keepdims=True)

# Print the transition matrix in a human-readable format with proper labels
print("Transition Matrix:")
bin_labels = ["<-2", "-2 to -1", "-1 to 0", "0 to 1", "1 to 2", ">2"]
print("      ", "  ".join(f"{label:>10}" for label in bin_labels))
for i in range(len(bins) - 1):
    print(f"{bin_labels[i]:>10}:", end=" ")
    for j in range(len(bins) - 1):
        print(f"{transition_matrix[i][j]:.2f}" + "  ", end="      ")
    print()

# print the sum of  the columns as well
print("Sum of the columns:")        
for i in range(len(bins) - 1):
    print(f"{bin_labels[i]:>10}:", end=" ")
    print(f"{transition_matrix[i].sum():.2f}")


# # Scaling the data
# scaler = StandardScaler()
# data["diff"] = scaler.fit_transform(data["diff"].values.reshape(-1, 1))



