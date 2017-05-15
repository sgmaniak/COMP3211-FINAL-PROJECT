# COMP3211-FINAL-PROJECT


Intro---------------
	This project is dedicated to examining different methods of solving the classic 
Pacman Atari game through the OpenAI environment.



Problem--------------
	OpenAI provides an environment for simulating a simple Atari video game while
allowing you to provide the policies for the agent, essentially allowing you
to implement your own strategy for solving the game. For each game, there are two
variations on different types of input: either using memory RAM as input, or using
screenshots of the game as input. In order to make the problem more interesting and
add elements of AI dealing with computer vision, we have chosen the latter form of input.




Solution--------------

Random:
One way of trying to solve the problem was by randomly controlling the pacman agent. This
is a somewhat poor approach to an actual solution, but it gives a good baseline for comparing
our other solution.


Constraint Satisfaction (AC3 Algorithm):
	Our real attempt to solve the problem involved framing the game as a constraint satisfaction problem.
For this type of problem, we have to deal with a set of variables, a set of domains, and a set of 
constraints. We then try to find evalutaions of the variables within those domains that satisfy our 
constraints.
	One specific way of solving the constraint satisfaction problem is by checking for arc consistency.
One variable is arc consistent with another if each of its admissible values is consistent with some admissible 
value of the second variable. Formally, a variable x is arc-consistent with another variable y if, for every 
value a in the domain of x there exists a value b in the domain of y such that (a, b)  satisfies the binary 
constraint between x and y.
	So, how does arc consistency apply to the problem of pacman? Our agent, pacman, has the choice of going
north, east, south or west. Say we are in the middle of a game, and we are trying to figure out the best direction
for our next step. We start off by considering all possibilities. However, perhaps there is a wall directly below
us, so we eliminate south as an option.
	To check for arc consistency, we utilize the AC3 algorithm, developed by Alan Mackworth in 1977. This
algorithm takes as input a set of variables, a set of domains for each variable, and both a set of unary
constraints (e.g. x must be a prime number) and a separate set of binary constraints (e.g. x must be 3 
less than y).
	Once this algorithm terminates, we have values of the variables that satisfy our current problem. 

Process---------------
	To run these next two algorithms, there are some dependencies that need to be installed. First, there is the gym library from OpenAI Gym. There is an installation guide	on 'github.com/openai/gym'. This is needed for both the random algorithm and the AC3 algorithm. 
	For the AC3 algorithm, we had to download some dependencies for the program. The program for the python file, we found on 'https://gist.github.com/fortunto2/14f9c6deffb14b50e13ad082b8514be0'. Before downloading the AC3 file, we used the installation guide found below 'A3C-Gym.py. After installing the requirements, we also had to download the pre-trained model for Ms Pacman, 'MsPacman-v0.tfmodel', on 'https://goo.gl/9yIol2'. We moved both 'MsPacman-v0.tfmodel' and 'A3C-Gym.py' to the directory in tensorpack that should have been downloaded, in  'tensorpack/examples/A3C-Gym'. 
	We then tested out two different algorithms. The first algorithm is a simple random agent, which performs a random action every timestep. To run this algorithm, we used the command 'python ms_pacman_random.py | tee ms_pacman_random.txt' to output the results for each episode into an accessable text file. 
	For the AC3 algorithm, we used the program 'A3C-Gym.py' using the command 'sudo python A3C-Gym.py --load MsPacman-v0.tfmodel --env MsPacman-v0 --episode 100 --output ms_pacman_tensorpack.txt'. The program should output a few video models of the program running, as well as a text file with each of the scores during each of the 100 episodes. We used a pre-trained model because training the model takes a lot of resources, and there were some pretrained models available. 





Results----------------
	The randomly controlled agent had an average reward of 203.67 with a standard deviation of 61.06. The agent running the AC3 algorithm had an average reward of 6027 with a standard deviation of 1569. 





Conclusion--------------
	In conclusion, the AC3 algorithm is a powerful way to tackle the pacman problem.
