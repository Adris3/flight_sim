from spacecraft import Spacecraft, Mode

def test_starts_in_safe_mode():
    # Spacecraft should boot in safe mode
    sc = Spacecraft()
    assert sc.mode == Mode.SAFE