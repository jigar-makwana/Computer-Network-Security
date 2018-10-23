import socket
import signal
import sys
import argparse


class runserver:                #building socket
  def __init__(self, port):
    self.host = ''
    self.port = port
    self.root_dir = '.'

  def get_headers(self, code):          #generate header

    header = ''                 #empty
    if code == 200:
      header = 'HTTP/1.0 200 OK\n'
    elif code == 404:
      header = 'HTTP/1.0 404 Not Found\n'

    header += 'Server: Python-Server\n'
    header += 'Connection: close\n\n'
    #print header
    return header

  def run(self):                        #infinite loop for requests

    """
    This function is used to start and understand the server
    responses to trigger http methods
    Current concurrency is set to 3
    """

    try:
      self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      #print("HTTP Server launched on host - {} port = {}".format(self.host,
                                                                 self.port))
      self.socket.bind((self.host, self.port))
    except Exception as e:
      #print("ERROR - {}".format(e))

    self.get_request()

  def get_request(self):
    # Infinite Loop for deciding get/put requests
    while True:
      self.socket.listen(3)

      connection, address = self.socket.accept()
      receieved_data = connection.recv(1024)
      info = bytes.decode(receieved_data)
      method = info.split(' ')[0]
      if (method == 'GET'):
        self.do_get(info, connection)
      if (method == "PUT"):
        print(method)
        print(info)
        self.do_put(info, connection)

  def do_get(self, info, connection):
    """
    it is called when GET is requested.
    it parse the file name from the message recieved from the connection
    and get that file.


    default file is set to index.html
    and will always return a result.

    Closes connection once the request is served.
    
    :param info: the information recieved from the request
    :param connection: the current connection
    :return: void
    """
    file_name = info.split(' ')
    file_name = file_name[1]
    print(file_name)
    file_name = file_name.split('?')[0]
    file_path = self.root_dir + file_name
    try:
      file_reader = open(file_path, 'rb')
      response_content = file_reader.read()
      file_reader.close()
      response_headers = self.get_headers(200)
      output_response = response_headers.encode()
      output_response += response_content
      print(output_response)
      connection.send(output_response)
      connection.close()
    except Exception as e:
      response_headers = self.get_headers(404)
      output_response = response_headers.encode()
      output_response += output_response
      print(output_response)
      connection.send(output_response)
      connection.close()

  def do_put(self, info, connection):
    """
    it is called when PUT is requested.
    it parse the file name from the message recieved from the connection
    and we create that file and put text in it.

    And closes connection once the request is served.

    :param info: the information recieved from the request
    :param connection: the current connection
    :return: void
    """
    try:
      text = info.split("\n\r")
      file_name = info.split(' ')
      file_name = file_name[1]
      file_name = file_name.split('?')[0]
      file_path = self.root_dir + file_name
      f = open(file_path, "w+")
      data = text[-1]
      f.write(data)
      f.close()
      response_headers = self.get_headers(404)
      output_response = response_headers.encode()
      output_response += output_response
      connection.send(output_response)
      connection.close()

    except Exception as e:
      response_headers = self.get_headers(404)
      output_response = response_headers.encode()
      output_response += output_response
      print(output_response)
      connection.send(output_response)
      connection.close()


def shutdown(current_server):
  """
  to end the socket
  """
  current_server.socket.shutdown()
  sys.exit()


if __name__ == '__main__':
    '''

    '''
  parser = argparse.ArgumentParser()
  parser.add_argument('--port', action='store',
                      default=8080, type=int,
                      nargs='?',
                      help='Specify alternate port [default: 8080]')
  args = parser.parse_args()

  myserver = runserver(args.port)
  myserver.run()
  signal.signal(signal.SIGINT, shutdown(myserver))
