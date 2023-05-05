from .ui_compiled.AboutDialog import Ui_AboutDialog
from PyQt6.QtWidgets import QDialog
from typing import TYPE_CHECKING
import webbrowser


if TYPE_CHECKING:
    from .Environment import Environment


class AboutDialog(QDialog, Ui_AboutDialog):
    def __init__(self, env: "Environment"):
        super().__init__()

        self.setupUi(self)

        self.icon_label.setPixmap(env.icon.pixmap(64, 64))
        self.version_label.setText(self.version_label.text().replace("{{version}}", env.version))

        self.view_source_button.clicked.connect(lambda: webbrowser.open("https://codeberg.org/JakobDev/jdAnimatedImageEditor"))
        self.close_button.clicked.connect(self.close)
