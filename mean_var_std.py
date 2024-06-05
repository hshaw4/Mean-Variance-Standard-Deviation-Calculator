import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        nparry = np.array(list).reshape(3,3)

        calculations = {'mean': [np.mean(nparry,axis = 0).tolist(), np.mean(nparry, axis = 1).tolist(), np.mean(nparry).tolist()],
                        'variance': [np.var(nparry,axis = 0).tolist(), np.var(nparry, axis = 1).tolist(), np.var(nparry).tolist()], 
                        'standard deviation': [np.std(nparry,axis = 0).tolist(), np.std(nparry, axis = 1).tolist(), np.std(nparry).tolist()], 
                        'max': [np.max(nparry,axis = 0).tolist(), np.max(nparry, axis = 1).tolist(), np.max(nparry).tolist()], 
                        'min': [np.min(nparry,axis = 0).tolist(), np.min(nparry, axis = 1).tolist(), np.min(nparry).tolist()], 
                        'sum': [np.sum(nparry,axis = 0).tolist(), np.sum(nparry, axis = 1).tolist(), np.sum(nparry).tolist()]}

        return calculations