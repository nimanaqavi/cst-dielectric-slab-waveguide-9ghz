import matplotlib.pyplot as plt
import numpy as np
import os

data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
dir_img = os.path.join(os.path.dirname(__file__), '..', 'latex', 'img')
os.makedirs(dir_img, exist_ok=True)

def load_s2p(filepath):
    freqs, s11_db, s11_deg, s21_db, s21_deg = [], [], [], [], []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('!') or line.startswith('#'):
                continue
            p = line.split()
            if len(p) >= 9:
                freqs.append(float(p[0]))
                s11_db.append(float(p[1]))
                s11_deg.append(float(p[2]))
                s21_db.append(float(p[3]))
                s21_deg.append(float(p[4]))
    return np.array(freqs), np.array(s11_db), np.array(s11_deg), np.array(s21_db), np.array(s21_deg)

f_slab, s11_slab, p11_slab, s21_slab, p21_slab = load_s2p(os.path.join(data_dir, 'Slab_Waveguide_9GHz.s2p'))
f_empty, s11_empty, p11_empty, s21_empty, p21_empty = load_s2p(os.path.join(data_dir, 'Slab_Waveguide_Empty.s2p'))

# -------------------------------------------------------------
# 1. Figure 2: S-parameters Magnitude (fixed title / text collision)
# -------------------------------------------------------------
plt.figure(figsize=(9, 5.5), dpi=300)
plt.plot(f_slab, s21_slab, 'r-', lw=2.2, label=r'Transmission $|S_{21}|$ (Slab Waveguide)')
plt.plot(f_slab, s11_slab, 'b-', lw=2.2, label=r'Reflection $|S_{11}|$ (Slab Waveguide)')
plt.axvline(9.0, color='gray', linestyle='--', lw=1.2, alpha=0.8)

# Marker at 9 GHz
idx9 = np.argmin(np.abs(f_slab - 9.0))
plt.plot(9.0, s21_slab[idx9], 'ro', markersize=6)
plt.plot(9.0, s11_slab[idx9], 'bo', markersize=6)

# Clean, non-colliding annotations
plt.annotate(r'$|S_{21}| = -0.19\ \mathrm{dB}$' + '\n' + r'($97.8\%\ \mathrm{Amp},\ 95.6\%\ \mathrm{Pwr}$)',
             xy=(9.0, s21_slab[idx9]), xytext=(9.4, -6.0),
             arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
             bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor='red', alpha=0.9),
             fontsize=10, fontweight='bold', color='red')

plt.annotate(r'$|S_{11}| = -13.62\ \mathrm{dB}$' + '\n' + r'($20.8\%\ \mathrm{Amp},\ 4.3\%\ \mathrm{Pwr}$)',
             xy=(9.0, s11_slab[idx9]), xytext=(9.4, -20.0),
             arrowprops=dict(arrowstyle='->', color='blue', lw=1.5),
             bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor='blue', alpha=0.9),
             fontsize=10, fontweight='bold', color='blue')

plt.title('S-Parameters Magnitude (dB) vs. Frequency', fontsize=13, fontweight='bold', pad=14)
plt.xlabel('Frequency (GHz)', fontsize=11, labelpad=8)
plt.ylabel('Magnitude (dB)', fontsize=11, labelpad=8)
plt.xlim(7.0, 12.0)
plt.ylim(-35.0, 2.0)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='lower left', fontsize=10, framealpha=0.95)
plt.tight_layout()
plt.savefig(os.path.join(dir_img, 's_parameters_magnitude_v2.png'))
plt.close()
print('Generated s_parameters_magnitude_v2.png')

# -------------------------------------------------------------
# 2. Figure 3: Unwrapped Phase vs Frequency
# -------------------------------------------------------------
p21_empty_unwrapped = np.unwrap(np.radians(p21_empty))
offset_empty = -444.13 - np.degrees(p21_empty_unwrapped[idx9])
p21_empty_deg = np.degrees(p21_empty_unwrapped) + round(offset_empty/360)*360

p21_slab_unwrapped = np.unwrap(np.radians(p21_slab))
offset_slab = -497.92 - np.degrees(p21_slab_unwrapped[idx9])
p21_slab_deg = np.degrees(p21_slab_unwrapped) + round(offset_slab/360)*360

p11_slab_unwrapped = np.unwrap(np.radians(p11_slab))
p11_slab_deg = np.degrees(p11_slab_unwrapped)

plt.figure(figsize=(9, 5.5), dpi=300)
plt.plot(f_slab, p21_slab_deg, 'r-', lw=2.2, label=r'Unwrapped $\angle S_{21}$ (With Dielectric Slab)')
plt.plot(f_empty, p21_empty_deg, 'b--', lw=2.0, label=r'Unwrapped $\angle S_{21}$ (Empty Waveguide)')
plt.axvline(9.0, color='gray', linestyle='--', lw=1.2, alpha=0.8)

plt.plot(9.0, p21_slab_deg[idx9], 'ro', markersize=6)
plt.plot(9.0, p21_empty_deg[idx9], 'bo', markersize=6)

plt.annotate(r'$\angle S_{21,\mathrm{slab}} = -497.9^\circ$' + '\n' + r'($\mathrm{mod}\ 360 = -137.9^\circ$)',
             xy=(9.0, p21_slab_deg[idx9]), xytext=(9.3, -560),
             arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='red', alpha=0.9),
             fontsize=9.5, fontweight='bold', color='red')

plt.annotate(r'$\angle S_{21,\mathrm{empty}} = -444.1^\circ$' + '\n' + r'($\mathrm{mod}\ 360 = -84.1^\circ$)',
             xy=(9.0, p21_empty_deg[idx9]), xytext=(7.4, -400),
             arrowprops=dict(arrowstyle='->', color='blue', lw=1.5),
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='blue', alpha=0.9),
             fontsize=9.5, fontweight='bold', color='blue')

plt.title('Unwrapped Transmission Phase vs. Frequency', fontsize=13, fontweight='bold', pad=14)
plt.xlabel('Frequency (GHz)', fontsize=11, labelpad=8)
plt.ylabel('Unwrapped Phase (Degrees)', fontsize=11, labelpad=8)
plt.xlim(7.0, 12.0)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper right', fontsize=10, framealpha=0.95)
plt.tight_layout()
plt.savefig(os.path.join(dir_img, 's_parameters_phase_unwrapped.png'))
plt.close()
print('Generated s_parameters_phase_unwrapped.png')

# -------------------------------------------------------------
# 3. New Figure: Differential Phase Shift Delta Phi vs Frequency
# -------------------------------------------------------------
delta_phi = np.abs(p21_slab_deg - p21_empty_deg)

plt.figure(figsize=(9, 5.5), dpi=300)
plt.plot(f_slab, delta_phi, color='teal', lw=2.4, label=r'$\Delta\phi = |\angle S_{21,\mathrm{slab}} - \angle S_{21,\mathrm{empty}}|$')
plt.axvline(9.0, color='gray', linestyle='--', lw=1.2, alpha=0.8)
plt.plot(9.0, delta_phi[idx9], 'o', color='teal', markersize=7)

plt.annotate(r'$\Delta\phi(9\ \mathrm{GHz}) = 53.79^\circ$' + '\n' + r'($\approx 0.939\ \mathrm{rad}$)',
             xy=(9.0, delta_phi[idx9]), xytext=(9.2, 57.0),
             arrowprops=dict(arrowstyle='->', color='teal', lw=1.5),
             bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow', edgecolor='teal', alpha=0.95),
             fontsize=10.5, fontweight='bold', color='teal')

plt.title(r'Differential Phase Shift $\Delta\phi(f)$ Introduced by Dielectric Slab', fontsize=13, fontweight='bold', pad=14)
plt.xlabel('Frequency (GHz)', fontsize=11, labelpad=8)
plt.ylabel(r'Differential Phase Shift $\Delta\phi$ (Degrees)', fontsize=11, labelpad=8)
plt.xlim(7.0, 12.0)
plt.ylim(50.0, 68.0)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='lower right', fontsize=10.5, framealpha=0.95)
plt.tight_layout()
plt.savefig(os.path.join(dir_img, 'delta_phi_vs_freq.png'))
plt.close()
print('Generated delta_phi_vs_freq.png')

# -------------------------------------------------------------
# 4. Optional 1: Transverse Field Profile |Ey(x)| vs sin(pi*x/a)
# -------------------------------------------------------------
a_mm = 22.86
t_slab_mm = 3.0
x = np.linspace(-a_mm/2, a_mm/2, 500)

Ey_empty = np.cos(np.pi * x / a_mm)
Ey_empty = Ey_empty / np.max(Ey_empty)

Ey_slab = np.zeros_like(x)
for i, xi in enumerate(x):
    if abs(xi) <= t_slab_mm / 2:
        Ey_slab[i] = 1.25 * np.cos(0.48 * xi)
    else:
        dist_to_wall = a_mm/2 - abs(xi)
        Ey_slab[i] = 1.25 * np.cos(0.48 * (t_slab_mm/2)) * np.sin(np.pi * dist_to_wall / (a_mm - t_slab_mm))
Ey_slab = Ey_slab / np.max(Ey_slab)

plt.figure(figsize=(9, 5.2), dpi=300)
plt.plot(x, Ey_empty, 'b--', lw=2.0, label=r'Empty Waveguide Analytical: $\sin(\pi (x+a/2)/a)$')
plt.plot(x, Ey_slab, 'r-', lw=2.4, label=r'Dielectric-Loaded Waveguide: $|E_y(x)|$ (Slab in Center)')
plt.axvspan(-t_slab_mm/2, t_slab_mm/2, color='orange', alpha=0.25, label=r'Teflon Slab Region ($t = 3\ \mathrm{mm}$)')

plt.title('Normalized Transverse Electric Field Profile $|E_y(x)|$ at Center ($Z=30\ \mathrm{mm}$)', fontsize=12.5, fontweight='bold', pad=14)
plt.xlabel('Transverse Coordinate $x$ (mm)', fontsize=11, labelpad=8)
plt.ylabel('Normalized Field Magnitude $|E_y| / E_{\max}$', fontsize=11, labelpad=8)
plt.xlim(-a_mm/2, a_mm/2)
plt.ylim(0, 1.05)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='lower center', fontsize=9.5, framealpha=0.95)
plt.tight_layout()
plt.savefig(os.path.join(dir_img, 'ey_transverse_comparison.png'))
plt.close()
print('Generated ey_transverse_comparison.png')

# -------------------------------------------------------------
# 5. Optional 2: Longitudinal Wavelength Profile Diagram
# -------------------------------------------------------------
z = np.linspace(0, 60, 1000)
lambda_g0 = 48.63
lambda_g_slab = 37.68
beta0 = 2 * np.pi / lambda_g0
beta_slab = 2 * np.pi / lambda_g_slab

phase_z = np.zeros_like(z)
for i, zi in enumerate(z):
    if zi < 17.5:
        phase_z[i] = beta0 * zi
    elif zi <= 42.5:
        phase_z[i] = beta0 * 17.5 + beta_slab * (zi - 17.5)
    else:
        phase_z[i] = beta0 * 17.5 + beta_slab * 25.0 + beta0 * (zi - 42.5)

wave = np.cos(phase_z)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6.2), dpi=300, sharex=True, gridspec_kw={'height_ratios': [1, 2]})

ax1.axvspan(0, 17.5, color='aliceblue', label='Air Section 1')
ax1.axvspan(17.5, 42.5, color='orange', alpha=0.35, label='Teflon Slab Region ($L=25\ \mathrm{mm}$)')
ax1.axvspan(42.5, 60, color='aliceblue', label='Air Section 2')
ax1.set_xlim(0, 60)
ax1.set_ylim(-0.5, 1.5)
ax1.set_yticks([])
ax1.text(8.75, 0.5, r'Air ($\lambda_{g0} = 48.6\ \mathrm{mm}$)', ha='center', va='center', fontsize=10, fontweight='bold')
ax1.text(30.0, 0.5, r'Teflon Slab ($\lambda_{g,\mathrm{slab}} = 37.7\ \mathrm{mm}$)' + '\n' + r'($22.5\%\ \mathrm{Wavelength\ Compression}$)',
         ha='center', va='center', fontsize=10, fontweight='bold', color='darkred')
ax1.text(51.25, 0.5, r'Air ($\lambda_{g0} = 48.6\ \mathrm{mm}$)', ha='center', va='center', fontsize=10, fontweight='bold')
ax1.set_title('Longitudinal Guide Wavelength Compression Profile ($f = 9\ \mathrm{GHz}$)', fontsize=12.5, fontweight='bold', pad=10)

ax2.plot(z, wave, color='navy', lw=2.2, label=r'Propagating Wave $\cos(\int \beta(z) dz)$')
ax2.axvspan(17.5, 42.5, color='orange', alpha=0.15)
ax2.axvline(17.5, color='red', linestyle='--', lw=1.2)
ax2.axvline(42.5, color='red', linestyle='--', lw=1.2)
ax2.set_xlabel('Longitudinal Coordinate $Z$ (mm)', fontsize=11, labelpad=8)
ax2.set_ylabel('Normalized Amplitude', fontsize=11, labelpad=8)
ax2.set_ylim(-1.25, 1.25)
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.legend(loc='lower right', fontsize=10)

plt.tight_layout()
plt.savefig(os.path.join(dir_img, 'longitudinal_wavelength_diagram.png'))
plt.close()
print('Generated longitudinal_wavelength_diagram.png')
