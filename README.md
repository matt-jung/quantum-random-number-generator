# quantum-random-number-generator
Program that generates a random binary string of a given length using H gates.

For a given `length`, the program creates a `QuantumCircuit` object with qubit number equal to `length`.
Hadamard gates are then applied to all qubits in the circuit, creating an equal superposition of all possible states.
The circuit is then measured, and the result of the measurement is returned as the random binary string.
