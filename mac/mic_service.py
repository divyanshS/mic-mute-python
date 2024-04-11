import logging
import subprocess

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class MicService:
    @staticmethod
    def _set_mic_volume(volume_level):
        """Set the microphone volume. 0 to mute, 100 to unmute."""
        try:
            script = f'set volume input volume {volume_level}'
            subprocess.run(['osascript', '-e', script])
            logger.info(f"mic-volume set to {volume_level}.")
        except Exception as e:
            logger.info(f"Error: {e}")

    @classmethod
    def mute_mic(cls):
        logger.info("Muting the mic, setting mic-volume to 0")
        cls._set_mic_volume(0)

    @classmethod
    def unmute_mic(cls):
        logger.info("Unmuting the mic, setting mic-volume to 100")
        cls._set_mic_volume(100)
