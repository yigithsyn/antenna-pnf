# antenna-pnf

A Python utility module for planar near-field (PNF) antenna measurement calculations. It provides helper methods to determine key measurement parameters such as separation distance, sampling spacing, scan length, and angle of view, based on IEEE standards.

---

## Requirements

- Python 3.8+
- No third-party dependencies (uses the standard library `math` module only)

---

## Installation

```shell
pip install antenna-pnf
```

---

## Usage

```python
import antenna_pnf as pnf
```

---

## API Reference

All methods are static and accessible directly on the `antenna-pnf` class without instantiation.

---

### `seperation_distance(frequency, coeff)`

Computes an arbitrary separation distance as a multiple of the wavelength.

| Parameter   | Type    | Unit | Description                       |
| ----------- | ------- | ---- | --------------------------------- |
| `frequency` | `float` | Hz   | Frequency of interest             |
| `coeff`     | `float` | —    | Wavelength multiplier coefficient |

**Returns:** `float` — separation distance in meters [m]

**Formula:**

$$R_{nf} = k \times \lambda = k \times c_0 / f$$

```python
d = pnf.seperation_distance(10e9, 10)  # 10 wavelengths at 10 GHz
```

---

### `min_seperation_distance(frequency, three_lambda=False)`

Returns the minimum recommended separation distance between the antenna under test (AUT) and the probe, per IEEE 1720-2012 Section 5.3.1.4.

| Parameter      | Type    | Unit | Description                                |
| -------------- | ------- | ---- | ------------------------------------------ |
| `frequency`    | `float` | Hz   | Frequency of interest                      |
| `three_lambda` | `bool`  | —    | Use 3λ criterion instead of the default 5λ |

**Returns:** `float` — minimum separation distance in meters [m]

**Formula:**

$$R_{nf} = 5 \times \lambda = 5 \times c_0 / f$$

> **Note:** The standard recommends choosing between 3λ and 5λ. The default (5λ) is used to ensure sufficient decoupling between the AUT and the probe. Set `three_lambda=True` to use the relaxed 3λ criterion.

```python
d_min = pnf.min_seperation_distance(10e9)           # 5λ (default)
d_min = pnf.min_seperation_distance(10e9, three_lambda=True)  # 3λ
```

---

### `angle_of_view(a, d, L)`

Computes the reliable far-field angle-of-view achievable from a planar near-field scan, per IEEE 149-2021 Eq. 99 and IEEE 1720-2012 Eq. 27.

| Parameter | Type    | Unit | Description                               |
| --------- | ------- | ---- | ----------------------------------------- |
| `a`       | `float` | m    | Antenna cross-section length              |
| `d`       | `float` | m    | Separation distance between AUT and probe |
| `L`       | `float` | m    | Scan region length                        |

**Returns:** `float` — angle of view in degrees [deg]

**Raises:** `ValueError` — if `L <= a` (scan length must exceed antenna size)

**Formula:**

$$\theta = \arctan\left(\frac{L - a}{2d}\right)$$

> **Note:** The scan region is assumed to be centered on the AUT.

```python
theta = pnf.angle_of_view(a=0.3, d=0.15, L=1.2)
```

---

### `sampling_spacing(frequency)`

Returns the maximum allowable sampling interval (grid spacing) for a near-field scan, per IEEE 149-2021 and IEEE 1720-2012 Eq. 25.

| Parameter   | Type    | Unit | Description           |
| ----------- | ------- | ---- | --------------------- |
| `frequency` | `float` | Hz   | Frequency of interest |

**Returns:** `float` — maximum sampling spacing in meters [m]

**Formula:**

$$\Delta = \lambda / 2 = 0.5 \times c_0 / f$$

```python
delta = pnf.sampling_spacing(10e9)
```

---

### `scan_length(a, d, theta)`

Computes the required scan length to achieve a desired angle-of-view, per IEEE 149-2021 Eq. 99 and IEEE 1720-2012 Eq. 27.

| Parameter | Type    | Unit | Description                               |
| --------- | ------- | ---- | ----------------------------------------- |
| `a`       | `float` | m    | Antenna cross-section length              |
| `d`       | `float` | m    | Separation distance between AUT and probe |
| `theta`   | `float` | deg  | Desired pattern view angle (one side)     |

**Returns:** `float` — required scan length in the same unit as inputs [m]

**Formula:**

$$L = 2d \cdot \tan\theta + a$$

> **Note:** The scan region is assumed to be centered on the AUT.

```python
L = pnf.scan_length(a=0.3, d=0.15, theta=45.0)
```

---

## Usage Example

```python
from antenna-pnf import antenna-pnf

frequency = 10e9  # 10 GHz

# Minimum separation distance (5 wavelengths)
d = pnf.min_seperation_distance(frequency)
print(f"Min separation distance : {d*100:.2f} cm")

# Maximum sampling spacing
delta = pnf.sampling_spacing(frequency)
print(f"Max sampling spacing    : {delta*1000:.2f} mm")

# Required scan length for ±45° angle-of-view with a 30 cm antenna
antenna_size = 0.30  # m
L = pnf.scan_length(a=antenna_size, d=d, theta=45.0)
print(f"Required scan length    : {L:.4f} m")

# Achieved angle-of-view
theta = pnf.angle_of_view(a=antenna_size, d=d, L=L)
print(f"Angle of view           : {theta:.2f} deg")
```

---

## Standards References

| Standard       | Title                                                    |
| -------------- | -------------------------------------------------------- |
| IEEE 149-2021  | Recommended Practice for Antenna Measurements            |
| IEEE 1720-2012 | Recommended Practice for Near-Field Antenna Measurements |

---

## Constants

| Symbol | Value           | Description              |
| ------ | --------------- | ------------------------ |
| `C0`   | 299 792 458 m/s | Speed of light in vacuum |