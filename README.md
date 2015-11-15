# Impossible-UBS-interview-question
Code for printing the answers to the "impossibile" UBS Interview question, not limited to 4 digits

In Sep 2011, Business Insider posted an article titled "Can You Answer This Impossible Interview Question Posed To An Interviewee At UBS?" Read this article <a href="http://www.businessinsider.com/interview-question-ubs-quant-2011-9?IR=T&" target="_blank">here</a>.

<b>And here is the question:</b><br>
<i>The number 1978 is such a number that if you add the first 2 sets of numbers, you'll will get the middle 2 sets of numbers. So in 1978, 19+78=97; so the question is write a formula that can find numbers that satisfy these conditions.</i>

My python code prints out all numbers which satisfies the given conditions. Contrary to most responses published online, based on my interpretation of the question, I have limited two assumptions:<br>
1) The first digit of the required number cannot be 0<br>
2) The interviewer did not specify that the required number must only be 4 digits

The Method "interview" takes in N, the number of "special numbers" that the user wants to return, and returns the first N "special numbers". The while loop can be changed to 'while True:' to search for numbers in an infinite loop.

<b>Formula:</b><br>
Beginning from all 4 digit numbers, let ABCD be a 4digit number each number be represented by a combination of it's integer characters a,b,c,d. Then the formula for finding all 4 digit numbers is thus based on algebraic manipulation that
10a + b + 10c + d = 10b + c<br>
Rearranging gives<br>
(10a + d) + (10c + b) = (10b + c)<br>
(10a + d) = 9(b-c)<br>

For all non negative, non 0 integers abcd, (10a+d) must be a multiple of 9, beginning from 18. <br>
Thus 9(b-c) >= 18<br>
(b-c) >= 2<br>
b >= c+2<br>
b > c+1<br>

Thus the formula to find such a number will start from identifying an appropriate B and C, which must satisfy B > C+1.

Since 2 <= B <= 9, and 0 <= C <= 7, each B and C have 8 possibilities. The pair of numbers for (B,C) that satisfies B>C+1 leaves us with 9c2 = 36 combinations. (A,D) will then be the positive difference between B and C, multiplied by 9.

Eg. <br>
(B,C) = (6,2)<br>
Since 9(B-C) = 36<br>
It follows that if (A,D) = (3,6)<br>
Then ABCD = 3626<br>
Where AB = 36, CD =26, AB + CD = 62 = BC<br>


The following outlines the solution procedure for all 4 digit numbers, which I think is a basic answer for an interviewee, but the pattern that is outlined in 6 digits, 8digits and higher digit numbers follow a different pattern. Do contact me if you found well defined formulas for higher digit numbers that follow this pattern! :)


