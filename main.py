# &copy Marek Janásek 2026, Apache License 2.0
# Kvantový generátor náhodných čísel v rozmezí 0 až 100
# Vytovořeno pro účely absolventské práce ZŠ Kunratice
# Pro spuštění je potřeba validní API klíč společnosti IBM.

#Importace potřebných knihoven, a SDK
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2

#Stanovení proměnných
shotNum = 1
service = QiskitRuntimeService(channel="ibm_quantum_platform")
backend = service.least_busy(simulator=False, operational=True)

#Tvorba kvantového obvodu
qc = QuantumCircuit(8, 8)

# Apply X-gates to qubits 0-3
for i in range(4):
  qc.x(i)

# Apply Hadamard gates to all 8 qubits
for i in range(8):
  qc.h(i)

qc.measure(range(8), range(8))

#Kopilace kvanotého obvodu
qc_transpiled = transpile(qc, backend)

#Spuštění kvantového obvodu
sampler = SamplerV2(backend)
job = sampler.run([qc_transpiled], shots=shotNum)

#Převdení výsledků na decimalní hodnotu 0 až 100
result = job.result()
pub_result = result[0]
bits = pub_result.data.c.get_bitstrings()
rawBin = bits[0]
preRang = int(rawBin, 2)
postRang = round((preRang * 100) / 255)

#Uvedení výsledků
print(" --- Výsledky QRNG ---")
print(f"Náhodné číslo: {postRang}")
print(f"QC Backend: {backend.name}")
print("--- &copy M.Janásek --- ")
