import pennylane as qml
from pennylane import numpy as np

def multiplication(a:float, b: float):

    if (a and b):
        A = np.log(np.abs(a))
        B = np.log(np.abs(b))

        # Define the Hamiltonian
        h = np.array([[A, 0],
                    [0, B]])
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

        mul_ans = np.sign(a) * np.sign(b) * round(np.exp(float(2 * expectation_value)), 2)
    
    else:
        mul_ans = 0

    return mul_ans