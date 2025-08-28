from model.functions import sigmoid, cost, handle_nan_in_matrix
import numpy as np

class LogisticRegression:
    def __init__(self, learning_rate=0.01, max_iterations=1000, tolerance=1e-6):
        """
        Initialize logistic regression model
        
        Args:
            learning_rate: Step size for gradient descent
            max_iterations: Maximum number of iterations
            tolerance: Convergence threshold
        """
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations
        self.tolerance = tolerance
        self.theta = None
        self.cost_history = []
    
    def fit(self, X, y):
        """
        Train the logistic regression model using gradient descent
        
        Args:
            X: Feature matrix (m x n)
            y: Target vector (m x 1) - should be 0 or 1 for binary classification
        """
        # Handle NaN values in X by replacing with column means
        X_clean = handle_nan_in_matrix(X)
        
        # Add bias term (intercept)
        m, n = X_clean.shape
        X_with_bias = np.column_stack([np.ones(m), X_clean])
        
        # Initialize weights
        self.theta = np.zeros(n + 1)
        
        # Gradient descent
        for i in range(self.max_iterations):
            # Forward propagation
            z = X_with_bias.dot(self.theta)
            h = sigmoid(z)
            
            # Compute cost
            current_cost = cost(X_with_bias, y, self.theta)
            self.cost_history.append(current_cost)
            
            # Compute gradients (partial derivatives)
            # ∂J/∂θ = (1/m) * X^T * (h - y)
            gradients = (1/m) * X_with_bias.T.dot(h - y)
            
            # Update weights
            new_theta = self.theta - self.learning_rate * gradients
            
            # Check for convergence
            if np.linalg.norm(new_theta - self.theta) < self.tolerance:
                print(f"Converged after {i+1} iterations")
                break
                
            self.theta = new_theta
        
        return self
    
    def predict_proba(self, X):
        """
        Predict class probabilities
        
        Args:
            X: Feature matrix
            
        Returns:
            Probabilities for positive class
        """
        if self.theta is None:
            raise ValueError("Model must be trained first")
        
        # Handle NaN values in X by replacing with column means
        X_clean = handle_nan_in_matrix(X)
        
        # Add bias term
        m = X_clean.shape[0]
        X_with_bias = np.column_stack([np.ones(m), X_clean])
        
        # Compute probabilities
        z = X_with_bias.dot(self.theta)
        probabilities = sigmoid(z)
        
        return probabilities
    
    def predict(self, X, threshold=0.5):
        """
        Make binary predictions
        
        Args:
            X: Feature matrix
            threshold: Decision threshold
            
        Returns:
            Binary predictions (0 or 1)
        """
        probabilities = self.predict_proba(X)
        return (probabilities >= threshold).astype(int)
    
    def get_weights(self):
        """Return the trained weights"""
        return self.theta
    
    def set_weights(self, weights):
        """Set weights (for loading pre-trained model)"""
        self.theta = weights

class OneVsAllClassifier:
    """
    Multi-class classifier using One-vs-All strategy
    Required for the 4 Hogwarts houses
    """
    def __init__(self, learning_rate=0.01, max_iterations=1000, tolerance=1e-6):
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations
        self.tolerance = tolerance
        self.classifiers = {}
        self.classes = None
    
    def fit(self, X, y):
        """
        Train one binary classifier for each class
        
        Args:
            X: Feature matrix
            y: Target labels (string labels like 'Gryffindor', 'Hufflepuff', etc.)
        """
        self.classes = np.unique(y)
        
        for class_name in self.classes:
            print(f"Training classifier for {class_name}...")
            
            # Create binary labels (1 for current class, 0 for others)
            binary_y = (y == class_name).astype(int)
            
            # Train binary classifier
            classifier = LogisticRegression(
                learning_rate=self.learning_rate,
                max_iterations=self.max_iterations,
                tolerance=self.tolerance
            )
            classifier.fit(X, binary_y)

            # Save weights
            # os.makedirs("model_weights", exist_ok=True)
            np.save(f"{class_name}_weights.npy", classifier.get_weights())

            self.classifiers[class_name] = classifier
        
        return self
    
    def predict_proba(self, X):
        """
        Predict probabilities for all classes
        
        Returns:
            Dictionary with class probabilities
        """
        if not self.classifiers:
            raise ValueError("Model must be trained first")
        
        probabilities = {}
        for class_name, classifier in self.classifiers.items():
            probabilities[class_name] = classifier.predict_proba(X)
        
        return probabilities
    
    def predict(self, X):
        """
        Predict the most likely class for each sample
        
        Returns:
            Array of predicted class names
        """
        probabilities = self.predict_proba(X)
        
        # Convert to matrix for easier comparison
        prob_matrix = np.column_stack([probabilities[class_name] for class_name in self.classes])
        
        # Get the class with highest probability
        predicted_indices = np.argmax(prob_matrix, axis=1)
        predicted_classes = self.classes[predicted_indices]
        
        # Save predictions to a file
        np.savetxt("predictions.txt", predicted_classes, fmt="%s")
        return predicted_classes
    
    def get_weights(self):
        """Return weights for all classifiers"""
        weights = {}
        for class_name, classifier in self.classifiers.items():
            weights[class_name] = classifier.get_weights()
        return weights
    
    def set_weights(self, weights_dict):
        """Set weights for all classifiers"""
        self.classes = list(weights_dict.keys())
        self.classifiers = {}
        
        for class_name, weights in weights_dict.items():
            classifier = LogisticRegression()
            classifier.set_weights(weights)
            self.classifiers[class_name] = classifier

