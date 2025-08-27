#!/usr/bin/env python3

import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from model.logistic_regression import LogisticRegression, OneVsAllClassifier

def test_binary_logistic_regression():
    """Test binary logistic regression with simple data"""
    print("=== Testing Binary Logistic Regression ===")
    
    # Create simple separable data
    np.random.seed(42)
    X = np.array([
        [1, 2], [2, 3], [3, 4], [4, 5],  # Class 1
        [6, 7], [7, 8], [8, 9], [9, 10]  # Class 0
    ])
    y = np.array([1, 1, 1, 1, 0, 0, 0, 0])
    
    print(f"Training data shape: X={X.shape}, y={y.shape}")
    print(f"X:\n{X}")
    print(f"y: {y}")
    
    # Train model
    model = LogisticRegression(learning_rate=0.1, max_iterations=1000)
    model.fit(X, y)
    
    # Test predictions
    predictions = model.predict(X)
    probabilities = model.predict_proba(X)
    
    print(f"\nPredictions: {predictions}")
    print(f"Probabilities: {probabilities}")
    print(f"Actual:      {y}")
    print(f"Accuracy: {np.mean(predictions == y):.2f}")
    
    return np.mean(predictions == y) > 0.8  # Should be > 80% accurate

def test_multiclass_classification():
    """Test One-vs-All classifier with simple data"""
    print("\n=== Testing One-vs-All Classifier ===")
    
    # Create simple 3-class data
    np.random.seed(42)
    X = np.array([
        [1, 1], [1, 2], [2, 1],  # Class A
        [5, 5], [5, 6], [6, 5],  # Class B  
        [9, 9], [9, 10], [10, 9] # Class C
    ])
    y = np.array(['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'])
    
    print(f"Training data shape: X={X.shape}, y={y.shape}")
    print(f"Classes: {np.unique(y)}")
    
    # Train model
    model = OneVsAllClassifier(learning_rate=0.1, max_iterations=1000)
    model.fit(X, y)
    
    # Test predictions
    predictions = model.predict(X)
    probabilities = model.predict_proba(X)
    
    print(f"\nPredictions: {predictions}")
    print(f"Actual:      {y}")
    print(f"Accuracy: {np.mean(predictions == y):.2f}")
    
    print(f"\nProbabilities for each class:")
    for class_name, probs in probabilities.items():
        print(f"{class_name}: {probs}")
    
    return np.mean(predictions == y) > 0.8

def test_with_nan_values():
    """Test how the model handles NaN values"""
    print("\n=== Testing with NaN Values ===")
    
    # Create data with NaN
    X = np.array([
        [1, 2], [2, np.nan], [3, 4], [np.nan, 5],
        [6, 7], [7, 8], [8, np.nan], [9, 10]
    ])
    y = np.array(['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'])
    
    print(f"Data with NaN:")
    print(f"X:\n{X}")
    print(f"NaN count in X: {np.isnan(X).sum()}")
    
    try:
        model = OneVsAllClassifier(learning_rate=0.1, max_iterations=100)
        model.fit(X, y)
        predictions = model.predict(X)
        print("Model handled NaN values - this might be a problem!")
        return False
    except Exception as e:
        print(f"Model correctly failed with NaN: {e}")
        return True

if __name__ == "__main__":
    print("Testing Logistic Regression Implementation\n")
    
    # Run tests
    test1_passed = test_binary_logistic_regression()
    test2_passed = test_multiclass_classification() 
    test3_passed = test_with_nan_values()
    
    print(f"\n=== Test Results ===")
    print(f"Binary classification: {'PASS' if test1_passed else 'FAIL'}")
    print(f"Multiclass classification: {'PASS' if test2_passed else 'FAIL'}")
    print(f"NaN handling: {'PASS' if test3_passed else 'FAIL'}")
    
    if test1_passed and test2_passed:
        print("\n✅ Logistic regression implementation looks correct!")
    else:
        print("\n❌ Issues found in logistic regression implementation")
