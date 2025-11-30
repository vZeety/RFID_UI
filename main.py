import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader


def main():
    app = QApplication(sys.argv)

    loader = QUiLoader()
    # This assumes rfid_ui.ui is in the SAME folder as this script
    window = loader.load("rfid_ui.ui", None)

    if window is None:
        raise RuntimeError("Failed to load rfid_ui.ui – check the path and file name.")

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
