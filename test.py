import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QLineEdit

class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Layouts
        mainLayout = QVBoxLayout()
        bottomLayout = QHBoxLayout()

        # Widgets
        self.chatHistory = QTextEdit()
        self.chatHistory.setReadOnly(True)
        self.messageInput = QLineEdit()
        self.sendButton = QPushButton("Send")

        # Setup layouts
        bottomLayout.addWidget(self.messageInput)
        bottomLayout.addWidget(self.sendButton)

        mainLayout.addWidget(self.chatHistory)
        mainLayout.addLayout(bottomLayout)

        self.setLayout(mainLayout)

        # Signals
        self.sendButton.clicked.connect(self.add_message)
        self.messageInput.returnPressed.connect(self.add_message)  # Handling Enter presses

        # Window settings
        self.setWindowTitle("PyQt Chat")
        self.resize(400, 300)

    def add_message(self):
        message = self.messageInput.text()
        if message:  # if the message is not empty
            formatted_message = f"Вы >> {message}"
            self.chatHistory.append(formatted_message)
            self.messageInput.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    app.exec_()
