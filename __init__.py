from mycroft import MycroftSkill, intent_file_handler, intent_handler
import vlc
import time

player=vlc.MediaPlayer("skills/theme-song-skill/snoopy_vs_red_baron.mp3")

class ThemeSong(MycroftSkill):
    #This plays the song about Snoopy
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('song.theme.intent')
    def handle_song_theme(self, message):
        '''Snoopy answers and plays song'''
        self.speak_dialog('song.theme')
        time.sleep(5)
        player.play()

    def stop(self):
        '''This stops the song'''
        player.stop()
        pass

    @intent_handler('pause.intent')
    def handle_pause(self):
        '''This pauses and resumes song '''
        player.pause() 

def create_skill():
    return ThemeSong() t
