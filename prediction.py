import pickle
import numpy as np
model = pickle.load(open('models/model_logistic.pkl','rb'))
pca = pickle.load(open('pickle_files/pca.pkl','rb'))

def pred(inputs):
    inputs = pca.transform(inputs.reshape(1,-1))
    # prediction
    return model.predict(inputs)