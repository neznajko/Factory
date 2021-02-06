## ls -al

*Yeah* **Ok** [this](https://ioinformatics.org/files/ioi1996problem2.pdf)
looks like a *Discrete Simulation* with ***Priority Queue***, and so on,
but I've decided to try something simpler, by the way recently have
learned that the *Chrome* JavaScript **V8** engine uses a similar
technique, I mean with the *queue* and stuff.

[*Ok*] we have two production lines the input of the second is output
of the first one, and the machines on both lines have different
production times. We are given couple of jobs and the question is
what is the minimum time required for both lines called A and B to
finish their jobs.

If one machine has infinite production time, in the program called
*delay*, than regardless of the fact that it's available from time *0*,
we don't want to give it a job, so the question is how we choose
which machine to take the next job?

[***Ok***] zo in addition to machine's *delay* we assign a second
number (*time*), which will represent the time that machine will be
available to take new job, initially this number is set to zero, and
incremented each time a job is dispatched to it by the delay. So
basically we pick next machine vhich has minimum (*time + delay*).
That number will represent the time vhen the job will be finished.
Jobs are basically list of these numbers, and that time of the last
job will represent the minimum time.

[Stay On These Roads](https://youtu.be/nWey1DBAchM)
