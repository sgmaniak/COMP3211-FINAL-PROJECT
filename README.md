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





Results----------------
	



Conclusion--------------
	In conclusion, the AC3 algorithm is a powerful way to tackle the pacman problem.
