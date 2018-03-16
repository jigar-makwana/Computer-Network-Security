
Team Member 1: Derek Teixeira							
Team Member 2: Jigar Makwana
Team Member 3: Pranav Chaughule


Files Submitted: receiver.py	Client side for the socket program
		 sender.py	Server side for the socket program
		 router.py	it generates random error and timeout
		 common.py	for checksum		


Execution of program on windows 7:






		1. Make sure that all the files are on the desktop
		2. Open up 3 cmd in the same direcory as your files are or just change the direcory using "cd.."
		3. On the first cmd in phase 4 folder by "shift+right click" Run the router.py
			This is done by typing in:  router.py 1600 1601 1602 1603   
			into the first cmd
			Wait for cmd to say "Listning..."
			And then it will ask how much error you need answer appropriate
		
		4. Once router is started start the receiver the receiver.py into the second cmd.
			This is done by typing in:  receiver.py 127.0.0.1 1602 127.0.0.1 1601 downloaded.txt
						  :  receiver.py 127.0.0.1 1602 127.0.0.1 1601 downloaded.jpg
						   :  receiver.py 127.0.0.1 1602 127.0.0.1 1601 downloaded.png
			
		5. Now start the sender in to third cmd.
			This is done by typing in:  sender.py 127.0.0.1 1600 127.0.0.1 1603 file.txt
						  :  sender.py 127.0.0.1 1600 127.0.0.1 1603 j.jpg
						   :  sender.py 127.0.0.1 1600 127.0.0.1 1603 j.png






The router(may be a router/switch/link) will connect the sender and the receiver, see the data on the receiver screen. And also write a new_file.txt file.

*Use python2 and not python3 in cmd


Make sure an edition of Python 2 is installed on the windows machine.

