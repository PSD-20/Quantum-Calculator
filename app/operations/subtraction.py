import pennylane as qml
from pennylane import numpy as np


def get_precision(x):
    s = str(x)
    if '.' in s:
        return len(s.split('.')[1])
    return 0

def subtraction(a:float, b: float):
    
    dev = qml.device("default.qubit", wires=2)

    # Define matrices
    h = np.array([[a, 0],
                  [0, 2]])

    H = np.array([[-b, 0],
                  [0, 2]])

    # Tensor product
    H_total = np.kron(h, H)

    # Hermitian observable
    observable = qml.Hermitian(H_total, wires=[0, 1])

    @qml.qnode(dev)
    def circuit():

        # Same circuit as Qiskit
        qml.Hadamard(wires=0)
        qml.PauliX(wires=1)
        qml.CNOT(wires=[0, 1])
   
        return qml.expval(observable)
    
    expectation_value = circuit()

    return(round(float(expectation_value), max(get_precision(a), get_precision(b))))


"""s = subtraction(0, -5.5)
print(s)"""