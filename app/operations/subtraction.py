import pennylane as qml
from pennylane import numpy as np

def subtraction(a:float, b: float):
    
    # Define the Hamiltonian
    h = np.array([[a, 0],
                  [0, -b]])
    H = qml.Hermitian(h, wires=0)


    # Initialize the quantum device
    dev = qml.device('default.qubit', wires=3)

    # Define the quantum function
    @qml.qnode(dev)
    def circuit():
        
        qml.Hadamard(0)

        return qml.expval(H)
    

    #Execute the circuit and print the expectation value
    expectation_value = circuit()

    sub_ans = round(float(2 * expectation_value), 2)

    return sub_ans