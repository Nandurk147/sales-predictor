import numpy as np
from sklearn.linear_model import LinearRegression

# Sample input data
# You can replace this with your own dataset
# X represents the input features, and y represents the corresponding sales
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Input features
y = np.array([10, 20, 30])  # Sales

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Predict sales for new input features
new_features = np.array([[2, 3, 4], [5, 6, 7]])  # New input features
predicted_sales = model.predict(new_features)

# Print the predicted sales
for i in range(len(predicted
