# Parallel-Computing-MapReduce
This program takes a list of document names and a list of words:

```
files = ["shakespeare1.txt", "shakespeare2.txt", "shakespeare3.txt", "shakespeare4.txt", "shakespeare5.txt", "shakespeare6.txt", "shakespeare7.txt", "shakespeare8.txt"]

words = ["love", "hate", "death", "night", "sleep", "time", "henry", "hamlet", "you", "my", "blood", "poison", "macbeth", "king", "heart", "honest"]
```

The program then goes on to count all the instances of each word on every document and print the totals, in a parallel manner. The output of this program is shown below:

```
Count totals...

Word    Appearances

love    2102
hate    167
death   915
night   799
sleep   246
time    1058
henry   0
hamlet  0
you     12941
my      11443
blood   712
poison  99
macbeth 0
king    507
heart   1139
honest  294

Testing with more cores...

1 thread execution time: 0.03939032554626465
2 threads execution time: 0.05862569808959961
4 threads execution time: 0.13895964622497559
6 threads execution time: 0.1494741439819336
8 threads execution time: 0.15739154815673828

Displaying runtimes...

Time spent opening files: 0.00013446807861328125
Time spent counting words: 0.797560453414917
```

### What problems you encountered completing the assignment and how you overcame them?
The location of the declaration of the wordcount dictionary affected the behavior of the program.
I spent a considerable amount of time trying to figure out the reason and was only able to fix it by asking the instructor.

### Any problems you weren't able to overcome or any bugs still left in the program?
Not any known bugs

### About how long it took you to complete the assignment?
Around a week

### A short analysis of why the program behaves as it does with an increasing number of threads?
The program produces a very counter intuitive behavior in terms of running times. The initial prediction would be that as the number of threads increases, the running times should decrease. But the observed results show that the running times go up. This was reasoned to be a consequence of the overhead required for managing the locking and unlocking of the critical section.

### Any observations or comments you had while doing the assignment?
Yes, I learned that when programming with pymp, there can be many other behind-the-scenes reasons that might affect the ultimate behavior at runtime.
