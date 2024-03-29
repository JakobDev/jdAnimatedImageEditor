from PyQt6.QtCore import QCoreApplication


def get_language_names() -> dict[str, str]:
    return {
        "en": QCoreApplication.translate("Language", "English"),
        "de": QCoreApplication.translate("Language", "German"),
        "nl": QCoreApplication.translate("Language", "Dutch"),
        "sv": QCoreApplication.translate("Language", "Swedish"),
        "it": QCoreApplication.translate("Language", "Italian"),
        "tr": QCoreApplication.translate("Language", "Turkish"),
    }
