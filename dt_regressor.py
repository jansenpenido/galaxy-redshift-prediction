"""
SDSS Redshift - Decision Tree Regressor
---------------------------------------
Author: Jansen Penido <jansen.penido@gmail.com>
"""

import numpy as np
from sklearn.tree import DecisionTreeRegressor


# Get colour features and corresponding redshift targets
def get_features_targets(data):
    features = np.zeros((data.shape[0], 4))
    features[:, 0] = data['u'] - data['g']
    features[:, 1] = data['g'] - data['r']
    features[:, 2] = data['r'] - data['i']
    features[:, 3] = data['i'] - data['z']

    targets = np.array(data['redshift'])

    return features, targets


# Calculate the median to calculate the model's prediction accuracy
def median_diff(predicted, actual):
    return np.median( abs(predicted - actual) )


# Check the prediction accuracy with median_diff
def validate_model(model, features, targets):
    # split the data into training and testing features and predictions
    split = features.shape[0]//2
    train_features = features[:split]
    test_features = features[split:]

    train_targets = targets[:split]
    test_targets = targets[split:]

    # train the model
    model.fit(train_features, train_targets)

    # get the predicted_redshifts
    predictions = model.predict(test_features)

    # use median_diff function to calculate the accuracy
    return median_diff(test_targets, predictions)


if __name__ == "__main__":
    data = np.load('data/sdss_galaxy_colors.npy')
    features, targets = get_features_targets(data)

    # initialize model
    dtr = DecisionTreeRegressor()

    # validate the model and print the med_diff
    diff = validate_model(dtr, features, targets)
    print('Median difference: {:f}'.format(diff))
