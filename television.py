class Television:
    MIN_VOLUME = 0
    MIN_CHANNEL = 0
    MAX_VOLUME = 2
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__status = False
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        '''
        Method that turns the TV on/off
        '''
        if not self.__status:
            self.__status = True
        elif self.__status:
            self.__status = False

    def mute(self) -> None:
        '''
        Method that mutes the TV
        '''
        if self.__status:
            if not self.__muted:
                self.__muted = True
            elif self.__muted:
                self.__muted = False

    def channel_up(self):
        '''
        Method to increase the tv channel
        '''
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        '''
        Method to decrease the tv channel
        '''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            else:
                self.__volume = Television.MIN_VOLUME

    def volume_down(self):
        '''
        Method that turns the volume
        '''
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            else:
                self.__volume = Television.MAX_VOLUME

    def __str__(self) -> str:
        '''
        Method to show the tv status.
        :return: tv status.
        '''
        if self.__muted:
            volume = Television.MIN_VOLUME
        else:
            volume = self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}"

    
