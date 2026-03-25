import sys
import pytest
# setting path
sys.path.append('./src/')

import antenna_pnf as pnf

def test_separation_distance():
    frequency = 10E9
    coeff = 10

    print()
    assert round(pnf.separation_distance(frequency, coeff),3) == pytest.approx(0.3)
    print(f"- separation distance at {frequency/1E6}MHz is {pnf.separation_distance(frequency,coeff):.3f}m with coefficient={coeff}")


def test_min_separation_distance():
    frequency = 3E9

    print()
    assert round(pnf.min_separation_distance(frequency),3) == pytest.approx(0.5)
    print(f"- Minimum separation distance at {frequency/1E6}MHz is {pnf.min_separation_distance(frequency):.3f}m")
    assert round(pnf.min_separation_distance(frequency, True),3) == pytest.approx(0.3)
    print(f"- Minimum separation distance at {frequency/1E6}MHz is {pnf.min_separation_distance(frequency, True):.3f}m (3 lambda crtieria)")


def test_angle_of_view():
    a = 0.15
    d = 0.05
    L = 1.00

    result = 83.290

    print()
    assert round(pnf.angle_of_view(a,d,L),3) == pytest.approx(result)
    print(f"- Angle of view (d={a}m, d={d}m, L={L}m) is {pnf.angle_of_view(a,d,L):.3f}°")

def test_sampling_spacing():
    freq = 5E9

    result = 0.030

    print()
    assert round(pnf.sampling_spacing(freq),3) == pytest.approx(result)
    print(f"- Sampling spacing (frequency={freq/1e6}MHz) is {pnf.sampling_spacing(freq):.3f}m")

def test_scan_length():
    a = 0.15
    d = 0.05
    theta = 83.290

    result = 1.000

    print()
    assert round(pnf.scan_length(a,d,theta),3) == pytest.approx(result)
    print(f"- Scan length (d={a}m, d={d}m, theta={theta}°) is {pnf.scan_length(a,d,theta):.3f}m")


