__author__ = 'chris'

import dbus


class Spotify():

    def __init__(self):
        self.sessionBus = dbus.SessionBus()
        self.proxy = self.sessionBus.get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2')
        self.propertyManager = dbus.Interface(self.proxy, 'org.freedesktop.DBus.Properties')

    def _getMetaData(self):
        return self.propertyManager.Get('org.mpris.MediaPlayer2.Player', 'Metadata')

    def getCurrentSong(self):
        return str(self._getMetaData()['xesam:title'])

    def getCurrentArtist(self):
        return str(self._getMetaData()['xesam:artist'][0])

    def getCurrentSongThumb(self):
        return str(self._getMetaData()['mpris:artUrl'])

    def getVolume(self):
        pass

    def isShuffle(self):
        pass

    def nextSong(self):
        self.proxy.Next()

    def previousSong(self):
        self.proxy.Previous()

    def stop(self):
        self.proxy.Stop()

    def play(self):
        self.proxy.Play()

    def playPause(self):
        self.proxy.PlayPause()

    def quit(self):
        self.proxy.Quit()

    def start(self):
        self.proxy.Raise()

    def openUri(self, uri):
        self.proxy.OpenUri(uri)