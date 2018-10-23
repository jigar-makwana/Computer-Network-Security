Implementation of an HTTP client and server running a pared down version of HTTP/1.0. This project is coded in python.


PROGRAM DESIGN: 
• The HTTP client and server are implemented using python programming language. 
• The python version used is 3.7.0 
• The python’s socket and request modules are used to build the server.



HTTP Server: 
• Server is initialized in the beginning. 
• A method for server to launch on a specified port is defined. 
• The number of concurrent requests the server can support is set to 3 in the get_request method. 
• The server is set around an infinite loop and needs to be interrupted with a terminal signal before it stops. 
• The type of HTTP request method is identified using the socket request. Then, it will parse the input and serve the request accordingly. 
• If server receives a GET request, then it sends out HTTP version:1.0, status code: 200, response phrase: OK to the client. It displays the content of that file. 
• If server receives a PUT request, it saves the file as test.txt and on successful creation of this file, server responds to the client with “200 OK File Created” message.


HTTP Client: 
• The client can invoke either the local server or any of the intranet servers for either sending files to those servers or receiving files from them. 
• The client can send/receive files to/from local server, but for the real web servers, files can only be received/ retrieved from them. 
• The client cannot upload a file on the real web servers. 
• The requests sent here are http requests and have a specific format. For any other request than the valid http request, the server does not respond.


To run the HTTP server and Client:

Step1: Run the server 
		• Server: server.py 9999 

Step2: Execute the client using GET method to retrieve file Step3: Execute the client using PUT method to upload file

		• Client: Test cases client.py 127.0.0.1 8080 GET index.html 
			  	     client.py www.cnn.com 80 GET index.html


HTTP Request methods: 

The HTTP request methods implemented in this program are as following. 

• GET: GET request indicates that the client wants to retrieve a file from the server specified. 
• PUT: PUT request indicates that the client wants to upload a file to the server specified.