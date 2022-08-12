class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        """
        Initializes private variables status, channel, and volume of the Television class. Each variable is set to its
        default value; False, 0, 0 respectively.
        :return: Does not return anything
        """
        self.__status = False
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME

    def power(self) -> None:
        """
        :return: Does not return anything, but this is a setter function to set the value of private variable status.
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    # Getter functon
    def get_channel(self) -> int:
        """

        :return: Returns the current value of the private variable channel.
        """
        return self.__channel

    def get_volume(self) -> int:
        """

        :return: Returns the current value of the private variable volume.
        """
        return self.__volume

    # Setter function
    def channel_up(self) -> str:
        """

        :return: A setter function for private variable channel. If status is set to True, and if channel is set
        to television's channel's max value, sets private variable channel to 0. Otherwise, if channel is less than
        television's channel's max value, increments the value of channel by 1. Otherwise, if status is False,
        returns "Television is not turned on".
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
        else:
            return 'Television is not turned on.'

    # Setter function
    def channel_down(self) -> str:
        """

        :return: A setter function for private variable channel. If status is set to True, and if channel is set
        to television's channel's min value, sets private variable channel to 3. Otherwise, if channel is greater than
        television's channel's min value, decrements the value of channel by 1. Otherwise, if status is False,
        returns "Television is not turned on".
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
        else:
            return 'Television is not turned on.'

    # Setter function
    def volume_up(self) -> str:
        """

        :return: Setter function for private variable volume. If television status is False, returns
        "Television is not turned on." If status is True, increments volume by 1. If volume
        is television's max volume, does not increment volume.
        """
        if self.__status:

            if self.__volume == Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
            else:
                self.__volume += 1
        else:
            return 'Television is not turned on.'

    # Setter function
    def volume_down(self) -> None:
        """
        :return: Setter function for private variable volume. If television status is False, returns
        "Television is not turned on." If status is True, decrements volume by 1. If volume
        is television's min volume, does not decrement volume.
        """
        if self.__status:
            if self.__volume == Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        :return: A string which states the status of the Television instance, the
        current channel, and the current volume.
        """
        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
