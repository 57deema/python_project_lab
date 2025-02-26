import time
import random
from math import sqrt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error

# Define parameter ranges
n_estimators_range = [10, 25, 50, 100, 200, 300, 400]
max_features_range = ['sqrt', 'log2', None]
max_depth_range = [1, 2, 5, 10, 20, None]

# Dummy training and validation datasets (Replace these with actual data)
X_train_filled = [[random.randint(15, 40) for _ in range(3)] for _ in range(100)]
y_train = [random.randint(15, 40) for _ in range(100)]
X_val_filled = [[random.randint(15, 40) for _ in range(3)] for _ in range(30)]
y_val = [random.randint(15, 40) for _ in range(30)]

def run_sequential():
    """Runs the sequential execution of temperature monitoring."""
    print("Running sequential temperature monitoring...")

    start_time = time.time()
    
    # Initialize best model tracking
    best_rmse = float('inf')
    best_mape = float('inf')

    for n_estimators in n_estimators_range:
        for max_features in max_features_range:
            for max_depth in max_depth_range:
                # Train Random Forest model
                rf_model = RandomForestRegressor(
                    n_estimators=n_estimators,
                    max_features=max_features,
                    max_depth=max_depth,
                    random_state=42
                )
                rf_model.fit(X_train_filled, y_train)

                # Predict and evaluate
                y_val_pred = rf_model.predict(X_val_filled)
                rmse = sqrt(mean_squared_error(y_val, y_val_pred))
                mape = mean_absolute_percentage_error(y_val, y_val_pred) * 100

                print(f"Sequential - {n_estimators}, {max_features}, {max_depth}. RMSE: {rmse}, MAPE: {mape}%")

                # Update best model if it improves
                if rmse < best_rmse:
                    best_rmse = rmse
                    best_mape = mape

    end_time = time.time()
    sequential_time = end_time - start_time
    print(f"\nSequential Execution Time: {sequential_time:.2f} sec")
    print(f"Best RMSE: {best_rmse}, Best MAPE: {best_mape}%")