if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    from controller.maincontroller import MainController
    
    app = QApplication(sys.argv)
    main = MainController()
    main.show()
    sys.exit(app.exec_())