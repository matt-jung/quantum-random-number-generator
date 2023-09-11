# Quantum Random Number Generator
<p align="center">
    Generates a random binary string using Qiskit:
</p>

<p align="center">
  <img width="212" alt="Screenshot 2023-09-12 at 06 16 01" src="https://github.com/matt-jung/quantum-random-number-generator/assets/133035195/46e0d378-93c4-4916-bc05-195a1edee14d">
</p>

## How does it work?
### Hadamard Gates
In Quantum Computing, a Hadamard gate can be used to put a single qubit into an equal superposition of $| 0 \rangle$ and $| 1 \rangle$ states:

<p align='center'>
    $H | 0 \rangle = \frac{1}{\sqrt{2}} (| 0 \rangle + | 1 \rangle)$
</p>

Upon measurement, there is then a 50% chance for the output '1' and 50% for '0'.


If we apply a 'layer' of Hadamard gates to $n$ qubits, the system will be put into an equal superposition of all possible states. For example when $n=2$:
<p align='center'>
    $H| 0 \rangle \otimes H| 0 \rangle  = \frac{1}{2}(| 00 \rangle + | 01 \rangle + | 10 \rangle + |11 \rangle)$
</p>

During measurement the output will therefore be chosen uniformly at random with a probability of $\frac{1}{2^n}$; in this case, the output will be '00', '01, '10', or '11', each with a 25% chance.

### Building the Circuit
When the user inputs a given length $n$, the program simulates a quantum circuit with $n$ qubits and puts them into a superposition of all possible states using a layer of Hadamard gates. Each qubit is then measured, giving a random binary string of length $n$ as the output.
<p align="center">
    <img width="466" alt="Screenshot 2023-09-12 at 07 11 11" src="https://github.com/matt-jung/quantum-random-number-generator/assets/133035195/2aa85a08-d1b3-4a2e-bf04-dd48f35be13b">
</p>
<p align="center">
    Example Quantum Circuit for $n=7$ qubits
</p>
