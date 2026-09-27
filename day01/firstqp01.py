from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Step 1: Initialize a circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Step 2: Apply a Hadamard gate to create superposition
qc.h(0)

# Step 3: Measure the qubit into the classical bit
qc.measure(0, 0)

# Step 4: Simulate running the circuit 1000 times
simulator = AerSimulator()
result = simulator.run(qc, shots=1000).result()
print(result.get_counts())
# Expected output: roughly ~50% '0' and ~50% '1'
