"""
Unit tests for the Spacecraft state machine.
Run with: pytest test_spacecraft.py -v
"""

from spacecraft import Spacecraft, Mode


def test_starts_in_safe_mode():
    """Spacecraft should boot up conservatively."""
    sc = Spacecraft()
    assert sc.mode == Mode.SAFE


def test_low_battery_triggers_safe_mode():
    """Below 20% battery, spacecraft must fall back to SAFE regardless of sun state."""
    sc = Spacecraft()
    sc.battery_pct = 10
    sc.in_eclipse = False
    sc.update_mode()
    assert sc.mode == Mode.SAFE


def test_mid_battery_triggers_sun_pointing():
    """Between 20-60% battery, spacecraft should prioritize recharging."""
    sc = Spacecraft()
    sc.battery_pct = 45
    sc.in_eclipse = False
    sc.update_mode()
    assert sc.mode == Mode.SUN_POINTING


def test_eclipse_forces_sun_pointing_even_with_high_battery():
    """Even with good battery, being in eclipse should prevent NOMINAL mode."""
    sc = Spacecraft()
    sc.battery_pct = 90
    sc.in_eclipse = True
    sc.update_mode()
    assert sc.mode == Mode.SUN_POINTING


def test_high_battery_and_sunlight_triggers_nominal():
    """Healthy battery + sunlight should allow full nominal operations."""
    sc = Spacecraft()
    sc.battery_pct = 80
    sc.in_eclipse = False
    sc.update_mode()
    assert sc.mode == Mode.NOMINAL


def test_battery_drains_during_eclipse():
    """Battery percentage should decrease when in eclipse."""
    sc = Spacecraft()
    sc.battery_pct = 50
    sc.in_eclipse = True
    sc.update_power(dt=1.0)
    assert sc.battery_pct < 50


def test_battery_charges_in_sunlight():
    """Battery percentage should increase when in sunlight."""
    sc = Spacecraft()
    sc.battery_pct = 50
    sc.in_eclipse = False
    sc.update_power(dt=1.0)
    assert sc.battery_pct > 50


def test_battery_never_exceeds_100():
    """Battery should be clamped at 100%, not overflow."""
    sc = Spacecraft()
    sc.battery_pct = 99.9
    sc.in_eclipse = False
    sc.update_power(dt=10.0)
    assert sc.battery_pct <= 100.0


def test_battery_never_drops_below_zero():
    """Battery should be clamped at 0%, not go negative."""
    sc = Spacecraft()
    sc.battery_pct = 0.5
    sc.in_eclipse = True
    sc.update_power(dt=10.0)
    assert sc.battery_pct >= 0.0