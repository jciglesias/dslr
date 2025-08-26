import numpy as np

def sigmoid(z: np.ndarray) -> np.ndarray:
    """Sigmoid activation function"""
    # Clip z to prevent overflow
    z = np.clip(z, -500, 500)
    return 1 / (1 + np.exp(-z))

def cost(X: np.ndarray, y: np.ndarray, theta: np.ndarray) -> float:
    """
    Compute logistic regression cost function
    J(θ) = -(1/m) * Σ[y*log(h(x)) + (1-y)*log(1-h(x))]
    """
    m = len(y)
    
    # Compute hypothesis using sigmoid
    z = X.dot(theta)
    h = sigmoid(z)
    
    # Prevent log(0) by adding small epsilon
    epsilon = 1e-15
    h = np.clip(h, epsilon, 1 - epsilon)
    
    # Compute cost using cross-entropy
    cost = -(1/m) * np.sum(y * np.log(h) + (1 - y) * np.log(1 - h))
    
    return cost