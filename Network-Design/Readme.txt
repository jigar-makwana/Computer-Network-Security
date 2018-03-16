Team Member 1: Derek Teixeira							
Team Member 2: Jigar Makwana

Files Submitted: receiver.py	Client side for the socket program
		 sender.py	Server side for the socket program
		 error.py	it generates random error and timeout
		 common.py	for checksum	


Execution of program on windows 7:

			Option one with error

		1. Make sure that all the files are on the desktop
		2. Open up 3 cmd in the same direcory as your files are or just change the direcory using "cd.."
		3. On the first cmd in error folder by "shift+right click" Run the error.py
			This is done by typing in: python2 error.py 1600 1601 1602 1603     
			into the first cmd
			Wait for cmd to say "Listning..."
		
		4. Once error is started start the receiver the receiver.py into the second cmd.
			This is done by typing in: python2 receiver.py 127.0.0.1 1602 127.0.0.1 1601
			
		5. Now start the sender in to third cmd.
			This is done by typing in: python2 sender.py 127.0.0.1 1600 127.0.0.1 1603 file.txt


			Option two without error

		1. Make sure that all the files are on the desktop
		2. Open up 2 cmd in the same direcory as your files are or just change the direcory using "cd.."
		3. On the first cmd in receiver folder by "shift+right click" Run the receiver.py
			This is done by typing in: python2 receiver.py 127.0.0.1 1600 127.0.0.1 1601     
			into the first cmd
			Wait for cmd to say "Listning..."
		
		4. Once receiver is started start the receiver the sender.py into the second cmd.
			This is done by typing in: python2 sender.py 127.0.0.1 1601 127.0.0.1 1600 file.txt


			Option three with error but with adjustment

		25% of packets will be dropped. 
		Another 25% of packets will be corrupted by randomly changing one byte. 
		You can change the percentage by editing ""error.py"".



The error(may be a router/switch/link) will contact the sender and receiver, see the data on the receiver screen. And also write a new_file.txt file.

*Use python2 and not python3 in cmd


Make sure an edition of Python 2 is installed on the windows machine.

