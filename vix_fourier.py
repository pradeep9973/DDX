import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Load the VIX data
data = pd.read_csv('VIX_History.csv')

# Extract the 'Close' price data and drop any missing values
close_prices = data['CLOSE'].dropna().values

# Compute the Fourier transform
N = len(close_prices)
fft_values = fft(close_prices)
fft_magnitudes = np.abs(fft_values)

# Compute the frequency bins
sample_spacing = 1  # Assuming daily frequency in data; adjust if needed
freqs = fftfreq(N, sample_spacing)

# Plot the Fourier transform
plt.figure(figsize=(12, 6))
plt.plot(freqs[:N // 2], fft_magnitudes[:N // 2])  # Only plot positive frequencies
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.title('Fourier Transform of VIX Close Prices')
plt.grid()
plt.show()
