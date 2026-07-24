from spacecraft import Spacecraft, Mode

def test_starts_in_safe_mode():
    # Spacecraft should boot in SAFE mode
    sc = Spacecraft()
    assert sc.mode == Mode.SAFE

def test_mid_batt_sun_pointing():
    # A medium battery should trigger SUN_POINTING mode
    sc = Spacecraft()
    sc.battery_lvl = 45
    sc.in_eclipse = False
    sc.update_mode()
    assert sc.mode == Mode.SUN_POINTING

def 