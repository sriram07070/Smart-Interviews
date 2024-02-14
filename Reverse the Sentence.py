Reverse the Sentence

Max Score: 50

Given a sentence, reverse the entire sentence word-by-word.



Note:

Solve using stack or in-place swap. Do not simply scan, split and print in reverse order.



Input Format
The first line of input contains T - the number of test cases It's followed by T lines, each containing a sentence S of space-separated words of lowercase English alphabet. All the words are separated by a single space.



Output Format

For each test case, print the reversed sentence, separated by a newline.



Constraints

1 <= T <= 1000

1 <= len(S) <= 1000



Example

Input

3

hello world

a b c d

data structures and algorithms



Output

world hello

d c b a

algorithms and structures data



Explanation



Self Explanatory.



  for _ in range(int(input())):
    s=input()
    stack=[]
    for w in s.split():
        stack.append(w)
    rw=[]
    while stack:
        rw.append(stack.pop())
    r=" ".join(rw)
    print(r)
