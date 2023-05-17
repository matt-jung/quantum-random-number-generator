from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def random_binary_string(length):
    """
    Generates a random binary string of a given length

    Args:
        length (int): length of random binary string

    Returns:
        binary_string (str): random binary string of given length

    Raises:
        TypeError: If length is not an integer. ValueError: If length < 1.

    Notes:
        -Uses Hadamard gates to put all possible states of a system into equal superposition, then measures the output of the circuit.
    """
    if not isinstance(length,int):
        raise TypeError('Binary string length must be an integer')
    if length<1:
        raise ValueError('Binary string length must be greater than or equal to 1.')

    qc=QuantumCircuit(length)
    qc.h(range(length))
    qc.measure_all()

    sim=AerSimulator()
    counts=sim.run(qc).result().get_counts()

    binary_string=max(counts,key=counts.get)
    return binary_string