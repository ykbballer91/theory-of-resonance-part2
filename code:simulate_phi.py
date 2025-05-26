import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp
import json

# --- Load parameters ---
with open("parameters.json", "r") as f:
    params = json.load(f)

omega_0 = params["omega_0"]
r = params["r"]
alpha = params["alpha"]
N = params["num_terms"]
eta_strength = params["eta_strength"]
use_eta = True  # Toggle η(t) effect

# --- Time domain ---
t = np.linspace(0, 20, 2000)
phi = np.zeros_like(t)

# --- Build Φ(t) ---
for n in range(1, N + 1):
    omega_n = omega_0 * r**n
    A_n = 1 / n**alpha
    phase = np.random.uniform(0, 2 * np.pi)
    phi += A_n * np.sin(omega_n * t + phase)

# --- Add η(t) modulation ---
if use_eta:
    eta = eta_strength * chirp(t, f0=0.1, f1=2.0, t1=t[-1], method='linear')
    phi += eta
else:
    eta = np.zeros_like(t)

# --- Plot result ---
plt.figure(figsize=(10, 4))
plt.plot(t, phi, label="Φ(t)", color='navy')
if use_eta:
    plt.plot(t, eta, label="η(t)", color='gray', linestyle='--', alpha=0.5)
plt.title("Simulated Phase Structure Φ(t)")
plt.xlabel("t")
plt.ylabel("Φ(t)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("phi_simulation_output.png", dpi=300)
plt.show()
