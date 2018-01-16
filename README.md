# PythonTasks

In Random Number Generator Algo, LCG linear congruential generator (LCG) is used which is defined by recurrence relation.
The initial condition (or seed values which are very important in generating random numbers) are 0 and 10 here. 

Seeds are generating in getSeeds() method.

The generator is defined as:
next_seed = (current_seed * multiplier +increment) % mod_value , where % indicates the modulus of mod_value.
It is defined in generate method.



getSeeds method returns the actual multiplier and seed values which are validated by the validate input method in recurrence relation.


The 73 % biased value is checked in while loop which only takes the values between 5 to 9 and therefore 27% will be for numbers less than 5.

