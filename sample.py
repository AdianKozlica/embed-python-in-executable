from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication([])
    main_widget = QWidget()
    main_widget.setFixedSize(250, 250)
    main_widget.show()
    exit(app.exec_())