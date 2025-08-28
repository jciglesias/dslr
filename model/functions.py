import numpy as np

def sigmoid(z: np.ndarray) -> np.ndarray:
    """Sigmoid activation function"""
    # Clip z to prevent overflow
    z = np.clip(z, -500, 500)
    return 1 / (1 + np.exp(-z))

def handle_nan_in_matrix(X: np.ndarray) -> np.ndarray:
    """
    Handle NaN values in feature matrix by replacing with column means
    This represents 'average performance' for students who didn't take a class
    """
    X_clean = X.copy()
    for col in range(X.shape[1] if len(X.shape) > 1 else 1):
        if len(X.shape) > 1:
            col_data = X[:, col]
        else:
            col_data = X
            
        if np.isnan(col_data).any():
            # Replace NaN with mean of non-NaN values in that column
            col_mean = np.nanmean(col_data)
            if np.isnan(col_mean):  # If entire column is NaN
                col_mean = 0
            
            if len(X.shape) > 1:
                X_clean[:, col] = np.where(np.isnan(col_data), col_mean, col_data)
            else:
                X_clean = np.where(np.isnan(col_data), col_mean, col_data)
    
    return X_clean

def cost(X: np.ndarray, y: np.ndarray, theta: np.ndarray) -> float:
    """
    Compute logistic regression cost function
    J(θ) = -(1/m) * Σ[y*log(h(x)) + (1-y)*log(1-h(x))]
    """
    m = len(y)
    
    # Handle NaN values in X
    X_clean = handle_nan_in_matrix(X)
    
    # Compute hypothesis using sigmoid
    z = X_clean.dot(theta)
    h = sigmoid(z)
    
    # Prevent log(0) by adding small epsilon
    epsilon = 1e-15
    h = np.clip(h, epsilon, 1 - epsilon)
    
    # Compute cost using cross-entropy
    cost = -(1/m) * np.sum(y * np.log(h) + (1 - y) * np.log(1 - h))
    
    return cost