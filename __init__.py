from mycroft import MycroftSkill, intent_file_handler


class WakeWordSensitivity(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('sensitivity.word.wake.intent')
    def handle_sensitivity_word_wake(self, message):
        self.speak_dialog('sensitivity.word.wake')


def create_skill():
    return WakeWordSensitivity()

