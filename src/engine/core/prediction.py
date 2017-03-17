__author__ = 'manishankargoswami'
"""
This class holds all prediction related data and it supports associated operations

"""


class Prediction(object):
    def __init__(self, prediction, probability):
        self.__prediction = prediction
        self.__probability = probability

    def get_prediction(self):
        return self.__prediction

    def get_probability_distribution(self):
        return self.__probability
