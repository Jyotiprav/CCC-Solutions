# CCC-Solutions

## Solution of Canadian Computing Competition 2016 (Junior) in python

### Problem J2: Magic Squares
#### Problem Description
```

Magic Squares are square arrays of numbers that have the interesting property that the numbers in
each column, and in each row, all add up to the same total.
Given a 4 × 4 square of numbers, determine if it is magic square.
Input Specification
The input consists of four lines, each line having 4 space-separated integers.
Output Specification
Output either magic if the input is a magic square, or not magic if the input is not a magic
square.
Sample Input 1
16 3 2 13
5 10 11 8
9 6 7 12
4 15 14 1
Output for Sample Input 1
magic
Explanation for Output for Sample Input 1
Notice that each row adds up to 34, and each column also adds up to 34.
Sample Input 2
5 10 1 3
10 4 2 3
1 2 8 5
3 3 5 0
Output for Sample Input 2
not magic
Explanation for Output for Sample Input 2
Notice that the top row adds up to 19, but the rightmost column adds up to 11.
```
#### Solution: 
Problem J2 Magic Squares.py

<hr>

### Problem J3: Hidden Palindrome
#### Problem Description
```
A palindrome is a word which is the same when read forwards as it is when read backwards. For
example, mom and anna are two palindromes.
A word which has just one letter, such as a, is also a palindrome.
Given a word, what is the longest palindrome that is contained in the word? That is, what is the
longest palindrome that we can obtain, if we are allowed to delete characters from the beginning
and/or the end of the string?
Input Specification
The input will consist of one line, containing a sequence of at least 1 and at most 40 lowercase
letters.
Output Specification
Output the total number of letters of the longest palindrome contained in the input word.
Sample Input 1
banana
Output for Sample Input 1
5
Explanation for Output for Sample Input 1
The palindrome anana has 5 letters.
Sample Input 2
abracadabra
Output for Sample Input 2
3
Explanation for Output for Sample Input 2
The palindromes aca and ada have 3 letters, and there are no other palindromes in the input
which are longer.
Sample Input 3
abba
Output for Sample Input 3
4
```
#### Solution
j3_2016.py
<hr>

### Problem J4: Arrival Time
#### Problem Description
```
Fiona commutes to work each day. If there is no rush-hour traffic, her commute time is 2 hours.
However, there is often rush-hour traffic. Specifically, rush-hour traffic occurs from 07:00 (7am)
until 10:00 (10am) in the morning and 15:00 (3pm) until 19:00 (7pm) in the afternoon. During
rush-hour traffic, her speed is reduced by half.
She leaves either on the hour (at XX:00), 20 minutes past the hour (at XX:20), or 40 minutes past
the hour (at XX:40).
Given Fiona’s departure time, at what time does she arrive at work?
Input Specification
The input will be one line, which contains an expression of the form HH:MM, where HH is one of
the 24 starting hours (00, 01, . . ., 23) and MM is one of the three possible departure minute times
(00, 20, 40).
Output Specification
Output the time of Fiona’s arrival, in the form HH:MM.
Sample Input 1
05:00
Output for Sample Input 1
07:00
Explanation for Output for Sample Input 1
Fiona does not encounter any rush-hour traffic, and leaving at 5am, she arrives at exactly 7am.
Sample Input 2
07:00
Output for Sample Input 2
10:30
Explanation for Output for Sample Input 2
Fiona drives for 3 hours in rush-hour traffic, but only travels as far as she normally would after
driving for 1.5 hours. During the final 30 minutes (0.5 hours) she is driving in non-rush-hour
traffic.
Sample Input 3
23:20
6
Output for Sample Input 3
01:20
Explanation for Output for Sample Input 3
Fiona leaves at 11:20pm, and with non-rush-hour traffic, it takes two hours to travel, so she arrives
at 1:20am the next day.
```
#### Solution
j4_2016.py
<hr>

### Problem J5: Tandem Bicycle
#### Problem Description
```
Since time immemorial, the citizens of Dmojistan and Pegland have been at war. Now, they have
finally signed a truce. They have decided to participate in a tandem bicycle ride to celebrate the
truce. There are N citizens from each country. They must be assigned to pairs so that each pair
contains one person from Dmojistan and one person from Pegland.
Each citizen has a cycling speed. In a pair, the fastest person will always operate the tandem
bicycle while the slower person simply enjoys the ride. In other words, if the members of a pair
have speeds a and b, then the bike speed of the pair is max(a, b). The total speed is the sum of the
N individual bike speeds.
For this problem, in each test case, you will be asked to answer one of two questions:
• Question 1: what is the minimum total speed, out of all possible assignments into pairs?
• Question 2: what is the maximum total speed, out of all possible assignments into pairs?
Input Specification
The first line will contain the type of question you are to solve, which is either 1 or 2.
The second line contains N (1 ≤ N ≤ 100).
The third line contains N space-separated integers: the speeds of the citizens of Dmojistan.
The fourth line contains N space-separated integers: the speeds of the citizens of Pegland.
Each person’s speed will be an integer between 1 and 1 000 000.
For 8 of the 15 available marks, questions of type 1 will be asked. For 7 of the 15 available marks,
questions of type 2 will be asked.
Output Specification
Output the maximum or minimum total speed that answers the question asked.
Sample Input 1
1
3
5 1 4
6 2 4
Output for Sample Input 1
12
8
Explanation for Output for Sample Input 1
There is a unique optimal solution:
• Pair the citizen from Dmojistan with speed 5 and the citizen from Pegland with speed 6.
• Pair the citizen from Dmojistan with speed 1 and the citizen from Pegland with speed 2.
• Pair the citizen from Dmojistan with speed 4 and the citizen from Pegland with speed 4.
Sample Input 2
2
3
5 1 4
6 2 4
Output for Sample Input 2
15
Explanation for Output for Sample Input 2
There are multiple possible optimal solutions. Here is one optimal solution:
• Pair the citizen from Dmojistan with speed 5 and the citizen from Pegland with speed 2.
• Pair the citizen from Dmojistan with speed 1 and the citizen from Pegland with speed 6.
• Pair the citizen from Dmojistan with speed 4 and the citizen from Pegland with speed 4.
Sample Input 3
2
5
202 177 189 589 102
17 78 1 496 540
Output for Sample Input 3
2016
Explanation for Output for Sample Input 3
There are multiple possible optimal solutions. Here is one optimal solution:
• Pair the citizen from Dmojistan with speed 202 and the citizen from Pegland with speed 1.
• Pair the citizen from Dmojistan with speed 177 and the citizen from Pegland with speed 540.
• Pair the citizen from Dmojistan with speed 189 and the citizen from Pegland with speed 17.
• Pair the citizen from Dmojistan with speed 589 and the citizen from Pegland with speed 78.
• Pair the citizen from Dmojistan with speed 102 and the citizen from Pegland with speed 496.
This sum yields 202 + 540 + 189 + 589 + 496 = 2016.
```
#### Solution
j5-2016.py
<hr>

## Solution of Canadian Computing Competition 2017 (Junior) in python
### Problem J2: Shifty Sum
#### Problem Description
```
Suppose we have a number like 12. Let’s define shifting a number to mean adding a zero at the
end. For example, if we shift that number once, we get the number 120. If we shift the number
again we get the number 1200. We can shift the number as many times as we want.
In this problem you will be calculating a shifty sum, which is the sum of a number and the numbers
we get by shifting. Specifically, you will be given the starting number N and a non-negative integer
k. You must add together N and all the numbers you get by shifting a total of k times.
For example, the shifty sum when N is 12 and k is 1 is: 12 + 120 = 132. As another example, the
shifty sum when N is 12 and k is 3 is 12 + 120 + 1200 + 12000 = 13332.

Input Specification
The first line of input contains the number N (1 ≤ N ≤ 10000). The second line of input contains
k, the number of times to shift N (0 ≤ k ≤ 5).
Output Specification
Output the integer which is the shifty sum of N by k.
Sample Input
12
3
Output for Sample Input
13332
```

### Solution: 
j2_2017.py
