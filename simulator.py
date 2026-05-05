
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

qc = QuantumCircuit(8, 8)

for i in range(4):
    qc.x(i)
    qc.h(i)

for i in range(4, 8):
    qc.h(i)

qc.measure(range(8), range(8))

print("Circuit Diagram:")
display(qc.draw('mpl'))


simulator = AerSimulator()
job = simulator.run(qc, shots=1024)
result = job.result()
counts = result.get_counts()


print("\nVýsledek simulátoru:")
display(plot_histogram(counts))
