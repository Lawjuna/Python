class Television:
    MIN_VOLUME=0
    MAX_VOLUME=2
    MIN_CHANNEL=0
    MAX_CHANNEL= 3

    def __init__(self) -> None:
        """
        Initializes all the variable needed for the methods
        """
        self.__status= False
        self.__muted= False
        self.__volume= Television.MIN_VOLUME
        self.__channel=Television.MIN_CHANNEL
        self.__volume_stored = Television.MIN_VOLUME

    def power(self) -> None:
        """
        Turns the TV on or off
        """
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        """
        turns the volume to zero
        """
        if self.__status:
            if self.__muted == False:
                self.__muted = True
                self.__volume_stored = self.__volume
                self.__volume = Television.MIN_VOLUME
            else:
                self.__muted = False
                self.__volume = self.__volume_stored
    def channel_up(self) -> None:
        """
        Increases the tv channel
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL
    def channel_down(self) -> None:
        """
        Decreases the tv channel
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL
    def volume_up(self) -> None:
        """
        Increases the volume by one
        """
        if self.__status:
            self.__muted = False
            self.__volume=self.__volume_stored
            if self.__volume < Television.MAX_VOLUME:
                self.__volume +=1
        self.__volume_stored=self.__volume
    def volume_down(self) -> None:
        """
        Decreases the volume by one
        """
        if self.__status:
            self.__muted = False
            self.__volume= self.__volume_stored
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -=1
        self.__volume_stored=self.__volume

    def __str__(self) -> str:
        """
        returns the current status, channel, and volume of the tv

        :return: Power = True/False, channel = tv channel, volume = tv volume
        """
        return F'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'