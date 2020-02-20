from qiskit import *
from qiskit.tools.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor

IBMQ.save_account('f37b2ea60f6f6c08b97b2473aa2e6b3b3e2ce6ddd47bc5b6aa6faf74cdf947f9e28a56238d3417b455c3b74a664ab7978cd32aef8a6b21fb63e6665280536f38')

# Create 2 quantum qubits for actual actions
qr = QuantumRegister(2)
# Create classical registers of 2 bits to take measurements from qubits
cr = ClassicalRegister(2)

# Create circuit from registers
circ = QuantumCircuit(qr, cr)

# Create entanglement between two qubits
circ.h(qr[0])  # apply Hadamard gate to first qubit
circ.cx(qr[0], qr[1])  # apply controlled x gate to first qubit with second as target

# Measure qubits and store into classical bits
circ.measure(qr, cr)

# Simulate circuit locally
# sim = Aer.get_backend('qasm_simulator')
# results = execute(circ, sim).result()
# plot_histogram(results.get_counts(circ))

# Run circuit on IBM machine
IBMQ.load_account()
prov = IBMQ.get_provider('ibm-q')
qcomp = prov.get_backend('ibmq_16_melbourne')
job = execute(circ, backend=qcomp)
job_monitor(job)
results = job.result()
plot_histogram(results.get_counts(circ))

# circ.draw(output='mpl')
