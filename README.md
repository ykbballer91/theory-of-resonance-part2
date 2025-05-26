# Theory of Resonance – Part II

This repository contains supplementary materials for:

**Theory of Resonance – Part II: Phase Dynamics and Variational Structure**  
Author: Yu Kanda (2025)  
Preprint: https://doi.org/10.5281/zenodo.15519091

---

## 📂 Contents

- `/code` — simulation scripts  
- `/data` — output parameters and structures  
- `/figures` — visualizations from Appendix 6.4

---

## 🖼 Figures (Appendix 6.4)

- `fig1_nested_harmonics.png`: Shows layered oscillations in Φ(t)
- `fig2_eta_effect.png`: Demonstrates the effect of η(t) on coherence

---

## 🧮 Parameters

- `parameters.json`: Simulation settings (ω₀, r, α, etc.)

```json
{
  "omega_0": 0.5,
  "r": 2.0,
  "alpha": 1.5,
  "num_terms": 6,
  "eta_strength": 0.3,
  "phi_noise": true
}
