import pennylane as qml
from pennylane import numpy as np

"""
def get_precision(x):
    s = str(x)
    if '.' in s:
        return len(s.split('.')[1])
    return 0"""

def smart_round(x, sig=10):
    return float(f"{x:.{sig}g}")

def division(a:float, b: float):

    if(a and b):
        dev = qml.device("default.qubit", wires=2)

        # Define matrices
        h = np.array([[a, 0],
                    [0, 1]])

        H = np.array([[1/b, 0],
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

    elif(a == 0 and b):
        expectation_value = 0

    else:
        expectation_value = np.inf
    #return(round(float(expectation_value), max(get_precision(a), get_precision(b))))
    return(smart_round(float(expectation_value)))
    
    """if (a and b):
        A = np.log(np.abs(a))
        B = np.log(np.abs(b))
        # Define the Hamiltonian
        h = np.array([[A, 0],
                    [0, -B]])
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

        div_ans = np.sign(a) * np.sign(b) * round(np.exp(float(2 * expectation_value)), 2)
    
    elif(a == 0 and b):
        div_ans = 0

    else:
        div_ans = np.inf

    return div_ans"""

"""d = division(10, 2)
print(d)"""