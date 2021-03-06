import shelve

from chef.configuration.Configuration import Configuration
from chef.messagingdaemon import DiscordDaemon


class DiscordConfiguration(Configuration):

    def __init__(self, settings : shelve):
        DiscordDaemon.subscribe_to_channel(settings.get("discord-channel-id"), self)
        super().__init__(settings)

    def send_message(self, message : str):
        DiscordDaemon.send_message(self.settings.get("discord-channel-id"), message)

    @staticmethod
    def get_configuration_type() -> str:
        return "discord"