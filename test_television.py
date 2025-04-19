# test_television.py
import pytest
from television import Television

@pytest.fixture
def tv():
    return Television()

def test_init(tv):
    # TV starts off, channel 0, volume 0
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power_toggle(tv):
    tv.power()
    assert "Power = True" in str(tv)
    tv.power()
    assert "Power = False" in str(tv)

def test_channel_wrapping(tv):
    tv.power()
    # go up past max
    for _ in range(Television.MAX_CHANNEL + 2):
        tv.channel_up()
    # MAX_CHANNEL=3 so (0→1→2→3→0→1)
    assert "Channel = 1" in str(tv)
    # wrap down past min
    for _ in range(3):
        tv.channel_down()
    # 1→0→3→2
    assert "Channel = 2" in str(tv)

def test_volume_bounds(tv):
    tv.power()
    # bump above max
    for _ in range(Television.MAX_VOLUME + 3):
        tv.volume_up()
    assert "Volume = 2" in str(tv)
    # lower below min
    for _ in range(5):
        tv.volume_down()
    assert "Volume = 0" in str(tv)

def test_mute_unmute(tv):
    tv.power()
    # set volume to 2
    tv.volume_up(); tv.volume_up()
    assert "Volume = 2" in str(tv)
    tv.mute()
    # volume -> 0 but remember 2
    assert "Volume = 0" in str(tv)
    # pressing volume_up should restore to 2 then +1 capped at max=2
    tv.volume_up()
    assert "Volume = 2" in str(tv)
    # muting again
    tv.mute()
    assert "Volume = 0" in str(tv)

def test_mute_does_nothing_when_off(tv):
    # TV is off: mute, volume commands, channel commands do nothing
    tv.mute(); tv.volume_up(); tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_str_shows_all(tv):
    tv.power()
    tv.channel_up()
    tv.volume_up()
    out = str(tv)
    assert out.startswith("Power = True, Channel = 1, Volume = 1")

