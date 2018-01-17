# PythonTasks

Problem :- 

Write a custom random number generation algo which should be 73% biased to the higher number. Like if I want ‘a random number between 1 to 10’ 100 times then it should give ‘number more than 5’ 73 times and ‘less than 5’ 27 times. You’re not allowed to use any predefined random number generation function nor use of any kind of third party library to generate random number.

Explanation - >

In Random Number Generator Algo, LCG linear congruential generator (LCG) is used which is defined by recurrence relation.
The initial condition (or seed values which are very important in generating random numbers) are 0 and 10 here. 

Seeds are generating in getSeeds() method.

The generator is defined as:
next_seed = (current_seed * multiplier +increment) % mod_value , where % indicates the modulus of mod_value.
It is defined in generate method.



getSeeds method returns the actual multiplier and seed values which are validated by the validate input method in recurrence relation.


The 73 % biased value is checked in while loop which only takes the values between 5 to 9 and therefore 27% will be for numbers less than 5.

Its implementation code is written in RandomNumberGenerator.py

