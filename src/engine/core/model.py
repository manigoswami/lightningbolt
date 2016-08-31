__author__ = 'manishankargoswami'
"""
This class represents a model, it does all the heavy wight-lifting
in terms of loading model, parsing the incoming request dimensions,
running prediction and generating the validation window

"""

from sklearn.externals import joblib
import numpy as np

from src.engine.utils import toolbox


class Model(object):
    def __init__(self, path):

        self.__model = joblib.load(path)

    def get(self):
        return self.__model

    def __getfeatures(self, featureproperties, dimensions):
        iterations = 0
        result = 0
        features = []
        for feature, properties in featureproperties.items():
            for items in properties:

                if items == 'donothing':
                    continue
                if iterations == 0:
                    result = getattr(toolbox, items)(dimensions[feature])
                else:
                    result = getattr(toolbox, items)(result)
                iterations += 1

            features.append(result)
            result = 0
            iterations = 0

        return np.array(features)

    def predict(self, featureproperties, windowproperties, dimensions):
        x = self.__getfeatures(featureproperties, dimensions)
        testX = x.astype(np.float)

        p = self.__model.predict_proba(testX)

        weightarray = np.array(p).reshape(-1, ).tolist()
        return self.__getbestpossiblerange(weightarray, windowproperties)

    def __getbestpossiblerange(self, weight, configurations):

        defaultrange = configurations['defaultrange']
        initialcutoff = configurations['initialcutoff']
        range1cutoff = configurations['range1cutoff']
        range2cutoff = configurations['range2cutoff']
        minwindowsize = configurations['minwindowsize']
        maxwindowsize = configurations['maxwindowsize']
        finaldefaultwindowsize = configurations['finaldefaultwindowsize']

        keyweight = {}
        keydiff = {}
        max = 0
        maxindex = 0
        for i in range(len(weight)):
            if max < weight[i]:
                max = weight[i]
                maxindex = i

        if maxindex == len(weight) - 1 or maxindex == len(weight) - 2:
            return defaultrange

        cutoff = 1.03
        suggestedrang = ""
        basenonfdays = minwindowsize
        switchcount = maxwindowsize - minwindowsize
        cutoff100to90count = 0
        cutoff90to75count = 0
        cutofflessthan75count = 0

        while True:
            initialcutoff -= minwindowsize / 100.0
            if cutoff100to90count <= switchcount and initialcutoff < range1cutoff:
                minwindowsize += 1
                initialcutoff = 1.00
                cutoff100to90count += 1
            if cutoff90to75count <= switchcount and initialcutoff < range2cutoff:
                minwindowsize += 1
                initialcutoff = range1cutoff
                cutoff90to75count += 1
            if cutofflessthan75count < 1 and minwindowsize > maxwindowsize:
                initialcutoff = range1cutoff
                minwindowsize = basenonfdays
                cutofflessthan75count += 1
            elif minwindowsize > maxwindowsize:
                initialcutoff = range2cutoff
                minwindowsize = finaldefaultwindowsize
            suggestedrang = self.__suggestedrange(weight, initialcutoff, minwindowsize, keyweight, keydiff)
            if len(suggestedrang) != 0:
                break

        return suggestedrang

    def __suggestedrange(self, weight, cutoff, minwindowsize, keyweight, keydiff):

        if cutoff <= 0 or minwindowsize <= 0:
            return {'min': 3, 'max': 5}

        for startIndex in range(len(weight) - minwindowsize + 1):
            endindex = startIndex + minwindowsize - 1
            su = self.sum(weight, startIndex, endindex)
            if su >= cutoff:

                key = self.__getkey(startIndex, endindex)
                keyweight[key] = su
                diff = endindex - startIndex + 1
                if diff <= minwindowsize:
                    if diff not in keydiff:
                        arrayList = []
                        keydiff[diff] = arrayList
                    keydiff.get(diff).insert(0, key)

        if bool(keydiff):
            max = 0.0
            maxKey = ""
            for key in keydiff.keys():
                for index in keydiff[key]:
                    val = keyweight[index]
                    if val >= max:
                        maxkey = index
                        max = val
            return self.__serializetodict(maxkey)
        return ""

    def __getkey(self, startindex, endindex):
        return str(startindex) + "," + str(endindex)

    def sum(self, weight, startindex, endindex):
        su = 0
        for index in range(startindex, endindex + 1):
            su += weight[index]
        return su

    def __serializetodict(self, value):
        serizd = value.split(",")
        return {'min': int(serizd[0]), 'max': int(serizd[1])}
