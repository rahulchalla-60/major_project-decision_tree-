import pandas as pd
import numpy as np
import random
from sklearn.tree import DecisionTreeRegressor
from config import Config

class Commodity:
    def __init__(self, csv_name):
        self.name = csv_name
        dataset = pd.read_csv(csv_name)
        self.X = dataset.iloc[:, :-1].values
        self.Y = dataset.iloc[:, 3].values

        depth = random.randrange(7, 18)
        self.regressor = DecisionTreeRegressor(max_depth=depth)
        self.regressor.fit(self.X, self.Y)

    def getPredictedValue(self, value):
        if value[1] >= 2019:
            fsa = np.array(value).reshape(1, 3)
            return self.regressor.predict(fsa)[0]
        else:
            c = self.X[:, 0:2]
            x = [i.tolist() for i in c]
            fsa = [value[0], value[1]]
            ind = 0
            for i in range(len(x)):
                if x[i] == fsa:
                    ind = i
                    break
            return self.Y[ind]

    def getCropName(self):
        return self.name.split('.')[0]

    def __str__(self):
        return self.getCropName().split('/')[1]

# Initialize commodity_list here
commodity_list = [Commodity(path) for path in Config.COMMODITY_DICT.values()]
