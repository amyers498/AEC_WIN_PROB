import csv
import random

# Generate random data and save as CSV
states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
          'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
          'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
          'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico',
          'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
          'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
          'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']  # All states

industries = ['Aviation', 'Transportation', 'Federal', 'Healthcare', 'Defense', 'Energy', 'Corporate']

num_data_points = 1000

data = []
for _ in range(num_data_points):
    state = random.choice(states)
    industry = random.choice(industries)
    fee = random.uniform(100000, 10000000)  # Adjust the range of fee values as needed
    square_footage = random.uniform(10000, 500000)  # Adjust the range of square footage values as needed
    data.append([state, industry, fee, square_footage])

filename = 'data.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['State', 'Industry', 'Fee', 'Square Footage'])  # Write header
    writer.writerows(data)  # Write data rows

import streamlit as st
from transformers import pipeline