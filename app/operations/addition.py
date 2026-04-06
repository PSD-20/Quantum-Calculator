"""import pennylane as qml
from pennylane import numpy as np

def addition(a:float, b: float):
    
    # Define the Hamiltonian
    h = np.array([[a, 0],
                  [0, b]])
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

    add_ans = round(float(2 * expectation_value), 2)

    return add_ans"""

from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from qiskit.transpiler import generate_preset_pass_manager
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np

from qiskit_ibm_runtime.fake_provider import FakeAuckland, FakeManilaV2

from qiskit_ibm_runtime import EstimatorV2 as Estimator
from qiskit.quantum_info import Operator, SparsePauliOp


def addition(a:float, b: float):

    """#Real Hardware
    from qiskit_ibm_runtime import QiskitRuntimeService

    service = QiskitRuntimeService()

    backend = service.least_busy(operational=True, simulator=False)"""

    #Fake Backend
    backend = FakeManilaV2()

    estimator = Estimator(backend)

    qc = QuantumCircuit(2)

    qc.h(0)
    qc.x(1)
    qc.cx(0, 1)

    pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
    isa_psi = pm.run(qc)

    h = np.array([[a, 0],
                [0, 2]])
    H = np.array([[b, 0],
                [0, 2]])

    #ops = Operator(h)
    h_s = SparsePauliOp.from_operator(Operator(np.kron(h, H)))

    isa_observables2 = h_s.apply_layout(isa_psi.layout)
    job2 = estimator.run([(isa_psi, isa_observables2)], precision=0.001)

    job_result2 = job2.result()[0] # It will block until the job finishes.
    expv2 = job_result2.data.evs
    
    return expv2

"""s = addition(3, 4)
print(np.round(s, 3))"""
#print(s)