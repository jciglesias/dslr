#!/usr/bin/env python3

import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from model.logistic_regression import OneVsAllClassifier

def test_nan_handling():
    """Test how the model handles NaN values with real predictions"""
    print("=== Testing Improved NaN Handling ===")
    
    # Create data similar to your Hogwarts data
    np.random.seed(42)
    X = np.array([
        [85, 90, np.nan],   # Student didn't take Ancient Runes
        [np.nan, 88, 92],   # Student didn't take Herbology  
        [78, np.nan, 85],   # Student didn't take Astronomy
        [90, 85, 88],       # Student took all classes
        [45, 50, np.nan],   # Poor student, didn't take Ancient Runes
        [np.nan, 45, 48],   # Poor student, didn't take Herbology
        [82, np.nan, 86],   # Good student, didn't take Astronomy
        [88, 92, 90],       # Excellent student, took all classes
    ])
    
    y = np.array(['Gryffindor', 'Gryffindor', 'Ravenclaw', 'Ravenclaw', 
                  'Hufflepuff', 'Hufflepuff', 'Slytherin', 'Slytherin'])
    
    print(f"Training data with NaN:")
    print(f"X:\n{X}")
    print(f"y: {y}")
    print(f"NaN count: {np.isnan(X).sum()}")
    
    # Train model
    model = OneVsAllClassifier(learning_rate=0.01, max_iterations=500)
    model.fit(X, y)
    
    # Test with prediction data that also has NaN
    X_test = np.array([
        [87, np.nan, 89],   # Good student, didn't take Astronomy
        [np.nan, 91, 88],   # Good student, didn't take Herbology
        [46, 49, np.nan],   # Poor student, didn't take Ancient Runes
    ])
    
    print(f"\nTest data with NaN:")
    print(f"X_test:\n{X_test}")
    
    # Make predictions
    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)
    
    print(f"\nPredictions: {predictions}")
    print(f"Probabilities:")
    for house, probs in probabilities.items():
        print(f"  {house}: {probs}")
    
    # Check if we got valid (non-NaN) probabilities
    all_valid = True
    for house, probs in probabilities.items():
        if np.isnan(probs).any():
            print(f"❌ {house} has NaN probabilities!")
            all_valid = False
        else:
            print(f"✅ {house} has valid probabilities (range: {probs.min():.3f} to {probs.max():.3f})")
    
    return all_valid

if __name__ == "__main__":
    success = test_nan_handling()
    if success:
        print("\n🎉 NaN handling is working correctly!")
        print("Students who didn't take certain classes are handled with average scores.")
    else:
        print("\n💥 NaN handling still has issues!")
