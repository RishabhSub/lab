class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        """
        Constructor to create initial state of a Television object
        """
        self.__status = False
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME

    def power(self) -> None:
        """
        Method to modify television's status
        :return: Does not return anything, but this is a setter function to set the value of private variable status.
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    # Getter functon
    def get_channel(self) -> int:
        """
        Method to access a television's channel
        :return: Television's current channel
        """
        return self.__channel

    def get_volume(self) -> int:
        """
        Method to access a television's volume
        :return: Television's current volume
        """
        return self.__volume

    # Setter function
    def channel_up(self) -> None:
        """
        Method to modify a television's channel
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    # Setter function
    def channel_down(self) -> None:
        """
        Method to modify a television's channel
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    # Setter function
    def volume_up(self) -> None:
        """
        Method to modify a television's volume
        """
        if self.__status:
            if self.__volume == Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
            else:
                self.__volume += 1

    # Setter function
    def volume_down(self) -> None:
        """
        Method to modify a television's volume
        """
        if self.__status:
            if self.__volume == Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to return a television's current settings
        :return: A television's current status, channel, and volume
        """
        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
