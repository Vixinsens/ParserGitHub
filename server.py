from flask import Flask, request, render_template
import threading
import APIGitHub

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        
        self.app = Flask(__name__, template_folder='.')
        #self.app.add_url_rule('/shutdown', view_func=self.shutdown)
        self.app.add_url_rule('/', 'index', view_func = self.home)

 
    def home(self):
          return render_template('index.html')

  

    

    def run_server(self):
        self.server = threading.Thread(target=self.app.run, kwargs={'host': self.host, 'port': self.port})
        self.server.start()
        return self.server

if __name__ == "__main__":
    server_host = "0.0.0.0"
    server_port = "5000"

    server = Server(
        host=server_host,
        port=server_port
        )
    server.run_server()