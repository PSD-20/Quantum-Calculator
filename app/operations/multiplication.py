import pennylane as qml
from pennylane import numpy as np


def get_precision(x):
    s = str(x)
    if '.' in s:
        return len(s.split('.')[1])
    return 0


def multiplication(a:float, b: float):
    
    dev = qml.device("default.qubit", wires=2)

    # Define matrices
    h = np.array([[a, 0],
                  [0, 1]])

    H = np.array([[b, 0],
                  [0, 1]])

    # Tensor product
    H_total = np.kron(h, H)

    # Hermitian observable
    observable = qml.Hermitian(H_total, wires=[0, 1])

    @qml.qnode(dev)
    def circuit():

        # Same circuit as Qiskit
        """qml.Hadamard(wires=0)
        qml.PauliX(wires=1)
        qml.CNOT(wires=[0, 1])"""
   
        return qml.expval(observable)
    
    expectation_value = circuit()

    return(round(float(expectation_value), max(get_precision(a), get_precision(b))))

    """if (a and b):
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

    return mul_ans"""

"""s = multiplication(0, -5.5)
print(s)"""