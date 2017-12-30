"""
SDSS Redshift - Decision Tree Regressor
---------------------------------------
Author: Jansen Penido <jansen.penido@gmail.com>
"""

import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import KFold
from matplotlib import pyplot as plt


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


# Validate predictions using KFold cross validations
def cross_validate_predictions(model, features, targets, k):
    kf = KFold(n_splits=k, shuffle=True)

    # declare an array for predicted redshifts from each iteration
    all_predictions = np.zeros_like(targets)

    for train_indices, test_indices in kf.split(features):
        # split the data into training and testing
        train_features, test_features = features[train_indices], features[test_indices]
        train_targets, test_targets = targets[train_indices], targets[test_indices]

        # fit the model for the current set
        model.fit(train_features, train_targets)

        # predict using the model
        predictions = model.predict(test_features)

        # put the predicted values in the all_predictions array defined above
        all_predictions[test_indices] = predictions

    # return the predictions
    return all_predictions


if __name__ == "__main__":
    data = np.load('data/sdss_galaxy_colors.npy')
    features, targets = get_features_targets(data)

    # initialize model
    dtr = DecisionTreeRegressor()

    # call cross validation function
    predictions = cross_validate_predictions(dtr, features, targets, 10)

    # calculate and print the model's accuracy using median difference
    diffs = median_diff(predictions, targets)
    print('Median difference: {:.3f}'.format(diffs))

    # plot the model's results
    plt.scatter(targets, predictions, s=0.4)
    plt.xlim((0, targets.max()))
    plt.ylim((0, predictions.max()))
    plt.xlabel('Measured Redshift')
    plt.ylabel('Predicted Redshift')
    plt.show()
