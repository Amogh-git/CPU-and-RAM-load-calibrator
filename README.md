# CPU-and-RAM-load-calibrator
The program is targeted to stress CPU and RAM. 
There are 3 options 1. stressing RAM 2. Stressing CPU 3.Stress both
------------------------------------------------------------------------
Stressing RAM:
Here we are taking input in % from command line arguments. We have calculated current RAM utilization and substracted from input.
If our input < current utilization then we send responce as already utilized!
commands:
stress RAM upto 60% for 10 seconds.
python test2.py 1 60 10

---------------------------------------------------------------------------
Stressing CPU:
Input in % will be accepted from command line arguments. Input determines how much more CPU to be utilized
Here we have used multiprocessing library and created 1 process for each core.
In target function we are runnung the process for input/100 seconds for e.g if you enter 60 as input each process will run for 0.6 sec
and will sleep for (0.9-0.6) i.e 0.2 sec. Here 0.9 is used to improve utilization. So in other words your process will run for given percent
of 1 second and this will continue for time you want to stress CPU.

command:
utilizing 60% of CPU for 10 seconds
python test2.py 2 60 10 

----------------------------------------------------------------------------
Stressing both CPU and memory:
Here we will accept 4th argument determining memory to be loaded in percent. 
Then we are creating 1 process for each core as discussed earlier. Here the only addition is that each process when executes it loads
the RAM with factor of no of cores. For e.g if you want memory to stress 80% and current RAM be 40% then you need to eat more 40% of RAM.
For that purpose if you have 8 cores then each process will load 40/8 % memory giving total of 40%.

command:
Stress CPU for 40% and memory for 70% for 10sec
python test2.py 3 40 10 70
