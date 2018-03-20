
# from keras.models import SPD_classfication
from abc import abstractmethod
import numpy as np
import pandas as pd
import queue
class singlePointDataModel(object):


    @abstractmethod
    def __init__(self):
        pass

    # calculate the right rate and error after classfication
    @abstractmethod
    def evaluate(self,preY,reaY):
        pass

    @abstractmethod
    def fit(self):
        pass

    @abstractmethod
    def predict(self):
        pass



class SPD_classfication(singlePointDataModel):

    def __init__(self):
        self.__isProgress = None
        self.__totalProgress = None
        self.__currentProgress = None
        pass

    def choeseFunction(self):
        pass

    def progressBar(self):

        if self.__isProgress == None:
            raise ("there are not initial ProcessBar")
        if self.__totalProgress == None:
            raise ("task do not start")
        if self.__isProgress:
            return int(100*float(self.__currentProgress)/self.__totalProgress)
        else:
            return -1

    def evaluate(self,preY,reaY):
        rightNumber = 0
        errorNumber = 0

        for i in range(len(preY)):
            if reaY[i]==preY[i]:
                rightNumber = rightNumber+1
            else:
                errorNumber = errorNumber+1

        if rightNumber+errorNumber!=len(preY):
            raise("there are errors in count right and wrong ")

        rightRatio = float(rightNumber)/len(preY)
        errorRatio = float(errorNumber)/len(preY)

        return rightRatio,errorRatio