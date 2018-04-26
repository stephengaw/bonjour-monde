"""
Example Classes
"""


class Instrument(object):

    def __init__(self, name, sound):
        """
        Create a Instrument instance
        
        :param name: str, the name of the instrument 
        :param sound: str, sound the instrument makes
        """
        self.name = name
        self.sound = sound

    def play(self):
        """
        Play the instrument, making the sound.
        
        :return: str, the instrument sound 
        """

        return self.sound

__all__ = sorted(['Instrument'])
