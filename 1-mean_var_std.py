import numpy as np

    
#The values in the returned dictionary should be lists and not Numpy arrays.
def calculate(list):
    try:
        matrix = np.reshape(list,(3,3))
        flattened = matrix.flatten()

        calculations = {
            'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(),flattened.mean()],
            'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), flattened.var()],
            'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), flattened.std()],
            'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), flattened.max()],
            'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), flattened.min()],
            'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), flattened.sum()]
        }
        
    except ValueError:
        print("List must contain nine numbers.")

    return calculations

list1 = calculate([55,11,23,32,41,25,63,67,25])
list2 = calculate([10,20,30,40,50,60,70,80,90]) 


print("Calculations EXAMPLE 1")
print(list1)
print()
print("Calculations EXAMPLE 2")
print(list2)







