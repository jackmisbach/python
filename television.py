"""
television.py

A simple Television class supporting power, channel up/down (with wrap),
volume up/down (with bounds), and a mute toggle that remembers/restores volume.
"""

class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Initialize a powered‐off TV on channel 0, volume 0, unmuted."""
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
        self.__prev_volume: int = self.__volume

    def power(self) -> None:
        """Toggle the TV power on/off."""
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Toggle mute.
        - When muting, store current volume and set volume to MIN_VOLUME.
        - When unmuting, restore stored volume.
        No effect if TV is off.
        """
        if not self.__status:
            return

        if not self.__muted:
            self.__prev_volume = self.__volume
            self.__volume = Television.MIN_VOLUME
            self.__muted = True
        else:
            self.__volume = self.__prev_volume
            self.__muted = False

    def channel_up(self) -> None:
        """Increment channel (wrap to MIN_CHANNEL after MAX_CHANNEL). Only when on."""
        if not self.__status:
            return
        self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """Decrement channel (wrap to MAX_CHANNEL below MIN_CHANNEL). Only when on."""
        if not self.__status:
            return
        self.__channel = (self.__channel - 1) % (Television.MAX_CHANNEL + 1)

    def volume_up(self) -> None:
        """
        Increase volume by 1 (up to MAX_VOLUME).
        If muted, unmute first (restore previous volume).
        No effect if TV is off.
        """
        if not self.__status:
            return
        if self.__muted:
            self.__muted = False
            self.__volume = self.__prev_volume
        if self.__volume < Television.MAX_VOLUME:
            self.__volume += 1

    def volume_down(self) -> None:
        """
        Decrease volume by 1 (down to MIN_VOLUME).
        If muted, unmute first (restore previous volume).
        No effect if TV is off.
        """
        if not self.__status:
            return
        if self.__muted:
            self.__muted = False
            self.__volume = self.__prev_volume
        if self.__volume > Television.MIN_VOLUME:
            self.__volume -= 1

    def __str__(self) -> str:
        """
        Return the TV’s state in the format:
        Power = [status], Channel = [channel], Volume = [volume]
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
