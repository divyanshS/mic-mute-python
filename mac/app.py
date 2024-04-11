import logging

import rumps

from mic_service import MicService

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

ON_ICON = "icons/on.png"
OFF_ICON = "icons/off.png"


class StatusBarApp(rumps.App):
    def __init__(self):
        super(StatusBarApp, self).__init__(name="Mic Manager")
        self.icon = ON_ICON

    @rumps.clicked("Mute")
    def mute(self, _):
        logger.info("Muting the mic")
        MicService.mute_mic()
        self.icon = OFF_ICON
        logger.info("Mic muted")

    @rumps.clicked("Unmute")
    def unmute(self, _):
        logger.info("Unmuting the mic")
        MicService.unmute_mic()
        self.icon = ON_ICON
        logger.info("Mic unmuted")

    def applicationSupportsSecureRestorableState(self):
        return "YES"


if __name__ == "__main__":
    app = StatusBarApp()
    app.run()
