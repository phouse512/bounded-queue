#Queue

Coded by Philip House [@phouse512](http://www.github.com/phouse512)


###Details
- Implementation Language - Python 2.7.5
- Used only built in libraries


###How to run the program
To run the program, be sure Python is installed, but you need not install additional
libraries. Run the following command:

	python QueueTest.py

###Output
The results of the unit tests will be displayed, which thoroughly test both
the enqueue and dequeue functions of the Queue class.
	
	
###Solution - A Queue class built on an array

I built a Queue class uses an array of size classified by the constructor.

The class contains two variables, front and back which hold the indexes of the
front and back elements of the queue. By incrementing these two indexes and 
modifying the contents of the array, it is possible for us to create a Queue of
size n that only uses an array of size n due to "wrapping around" the front and back index values.

	
###Algorithm Complexity###

By using two pointers that hold the front and back positions in the queue, my solution takes O(1) time.

	Enqueue O(1)
	Dequeue O(1)