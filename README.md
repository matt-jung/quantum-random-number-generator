# Quantum Random Number Generator
<p align="center">
    Generates a random binary string using Qiskit:
</p>

<p align="center">
  <img width="212" alt="Screenshot 2023-09-12 at 06 16 01" src="https://github.com/matt-jung/quantum-random-number-generator/assets/133035195/46e0d378-93c4-4916-bc05-195a1edee14d">
</p>

## How does it work?
In Quantum Computing, a Hadamard gate can be used to put a single qubit into an equal superposition of $| 0 \rangle$ and $| 1 \rangle$ states:

<p align='center'>
    $H | 0 \rangle = \frac{1}{\sqrt{2}} (| 0 \rangle + | 1 \rangle)$
</p>

Upon measurement, there is then a 50% chance for the output '1' and 50% for '0'.



