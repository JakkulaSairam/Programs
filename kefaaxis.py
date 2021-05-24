"""
Kefa was travelling in a one directional axis. He started at X = 0.
Petya had given Kefa the directions in the form of a string of '+'s and '-'s.
A '+' denoted that Kefa is supposed to move one unit in the positive direction.
Similarly, a '-' denoted that Kefa is supposed to move one unit in the negative direction.

Unfortunately, Kefa forgot some parts of the directions given to him by Petya, these parts are denoted by the character '?'.
Whenever Kefa has to process a '?', he tosses a coin. If heads, he moves one unit in the positive direction 
and if tails he moves one unit in the negative direction.

You are given the actual directions given by Petya and the directions that Kefa remembers.

Your task is to calculate the probability that Kefa will end up in the correct position.

Input
Input consists of two lines.
First line contains the string denoting the actual directions
Second line contains the string denoting the directions that Kefa remembers

Output
Print the probability that Kefa ends up in the correct final position

Notes
Length of the strings do not exceed 10

Sample Input 0

++-+-
+-+-+
Sample Output 0

1.000000
Sample Input 1

+-+-
+-??
Sample Output 1

0.500000
Sample Input 2

+++
??-
Sample Output 2

0.0000
"""
