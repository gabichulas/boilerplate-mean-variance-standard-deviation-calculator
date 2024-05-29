import numpy as np

def calculate(list):
        if len(list)==9:
            arr = np.array([list[:3],list[3:6],list[6:9]])
            calculations = {
                'mean' : [np.mean(arr,axis=0).tolist(),np.mean(arr,axis=1).tolist(),np.mean(arr).tolist()],
                'variance': [np.var(arr,axis=0).tolist(),np.var(arr,axis=1).tolist(),np.var(arr).tolist()],
                'standard deviation': [np.std(arr,axis=0).tolist(),np.std(arr,axis=1).tolist(),np.std(arr).tolist()],
                'max': [np.amax(arr,axis=0).tolist(),np.amax(arr,axis=1).tolist(),np.amax(arr).tolist()],
                'min': [np.amin(arr,axis=0).tolist(),np.amin(arr,axis=1).tolist(),np.amin(arr).tolist()],
                'sum': [np.sum(arr,axis=0).tolist(),np.sum(arr,axis=1).tolist(),np.sum(arr).tolist()]
            }
            return calculations
        else: raise ValueError("List must contain nine numbers.")
