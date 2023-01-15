from PyQt5.QtWidgets import QMainWindow

class Window(QMainWindow):
    from PyQt5.QtWebEngineWidgets import QWebEngineView
    from PyQt5.QtCore import QUrl
    from PyQt5.QtWidgets import QApplication

    def __init__(self, *args, **kwargs) -> None:
        qt_app = self.QApplication(
            ["--disable-gpu", "--no-sandbox"]
        )
        qt_app.setApplicationName("Zoro")
        
        super().__init__(*args, **kwargs)

        browser = self.QWebEngineView()
        browser.setUrl(self.QUrl("https://zoro.to/home"))

        self.setCentralWidget(browser)

        self.show()
        qt_app.exec()

if __name__ == "__main__":
    Window()