from PyQt5 import QtNetwork
from PyQt5.QtCore import QCoreApplication, QUrl
import sys
import threading

class Example:

    def __init__(self):

        self.doRequest()

    def doRequest(self):

        url = 'http://webcode.me'
        req = QtNetwork.QNetworkRequest(QUrl(url))
        t = threading.current_thread()
        print(f'do request at {t.ident}, {t.name}')
        self.nam = QtNetwork.QNetworkAccessManager()
        self.nam.finished.connect(self.handleResponse)
        self.nam.get(req)

    def handleResponse(self, reply):
        t = threading.current_thread()
        print(f'handle response at {t.ident}, {t.name}')
        er = reply.error()

        if er == QtNetwork.QNetworkReply.NoError:

            bytes_string = reply.readAll()
            print(str(bytes_string, 'utf-8'))

        else:
            print("Error occured: ", er)
            print(reply.errorString())

        QCoreApplication.quit()


def main():
    app = QCoreApplication([])
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
