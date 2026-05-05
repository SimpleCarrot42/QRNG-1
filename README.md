# Simple QRNG

This is a simple Quantum Random Number Generator (QRNG) built to run on real IBM Quantum hardware. 

The main feature here is a **clever 8-qubit architecture** I designed to cancel out hardware imperfections. In real quantum computers, qubits aren't perfect—they often have a slight "bias" toward 0 or 1 during initialization. My circuit fixes this by flipping half of the qubits before they enter superposition, balancing out the final result.

This program was made to accompany my research paper where I explain the basics of quantum computing and why QRNG matters for things like cyber security.

## How to use it

1. **Install Libraries:** Quantum libraries change fast, so make sure you have the latest `qiskit` and `qiskit-ibm-runtime` installed.
2. **Setup:** Run `setup.py` first. You’ll need to paste in your **44-character API key** from the IBM Quantum platform to get access to the real machines.
3. **Run:** 
   - Use `simulator.py` if you want to test the code for free on your own computer.
   - Use `main.py` when you're ready to run it on **real quantum hardware**.

##  Performance
The script usually uses between **1000ms and 2000ms** of IBM runtime. 

Generating just one number is honestly pretty inefficient because of the overhead and queue times. However, the real power comes when you generate a lot of numbers at once—the runtime doesn't really increase much, making it way more practical for bulk generation.

##  Circuit Architecture
Below is the circuit layout that compensates for the slight initialization errors in the hardware.

<img width="692" height="625" alt="QRNG Architecture" src="https://github.com/user-attachments/assets/f9eb51ce-9c7e-4e0f-ad6d-58a006d1b4c2" />

##  License
This project is open-source under the **Apache License 2.0**.
