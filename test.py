from spacecraft import Spacecraft, Mode


def test_starts_in_safe_mode():
    sc = Spacecraft()
    assert sc.mode == Mode.SAFE


def test_low_battery_triggers_safe_mode():
    sc = Spacecraft()
    sc.battery_lvl = 10
    sc.in_eclipse = False
    sc.update_mode()
    assert sc.mode == Mode.SAFE


def test_mid_battery_triggers_sun_pointing():
    sc = Spacecraft()
    sc.battery_lvl = 45
    sc.in_eclipse = False
    sc.update_mode()
    assert sc.mode == Mode.SUN_POINTING


def test_eclipse_forces_sun_pointing_even_with_high_battery():
    sc = Spacecraft()
    sc.battery_lvl = 90
    sc.in_eclipse = True
    sc.update_mode()
    assert sc.mode == Mode.SUN_POINTING


def test_high_battery_and_sunlight_triggers_nominal():
    sc = Spacecraft()
    sc.battery_lvl = 80
    sc.in_eclipse = False
    sc.update_mode()
    assert sc.mode == Mode.NOMINAL


def test_battery_drains_during_eclipse():
    sc = Spacecraft()
    sc.battery_lvl = 50
    sc.in_eclipse = True
    sc.update_power(dt=1.0)
    assert sc.battery_lvl < 50


def test_battery_charges_in_sunlight():
    sc = Spacecraft()
    sc.battery_lvl = 50
    sc.in_eclipse = False
    sc.update_power(dt=1.0)
    assert sc.battery_lvl > 50


def test_battery_never_exceeds_100():
    sc = Spacecraft()
    sc.battery_lvl = 99.9
    sc.in_eclipse = False
    sc.update_power(dt=10.0)
    assert sc.battery_lvl <= 100.0


def test_battery_never_drops_below_zero():
    sc = Spacecraft()
    sc.battery_lvl = 0.5
    sc.in_eclipse = True
    sc.update_power(dt=10.0)
    assert sc.battery_lvl >= 0.0