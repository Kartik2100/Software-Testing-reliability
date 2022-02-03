

# How to run
Run the test suite using this command:

	python3 A3_mocking.py


# Test Status

I think the second task needs mocks and the first and thrid task do not. For the first task, it is possible to test the function without mocks like in Assignment 1. For the second task, we are trying to see within the method itself that something like getLetterForNumericGrade is getting called properly. A mock is useful in this situation to see if the assert is called
within the method. In task three it seems like a mock is not needed since we are testing the return value of whether or not it is returning properly.

Task 1:
What the test case will verify?
The test will verify that the mock is converting the percentage for each numeric percentage to a correct corresponding letter grade.
I should convert the percentage to letter grade show that this conversion occured.
100->A+
95->A+
90->A+
89->A
87->A
85->A
84->A-
82->A-
80->A-
79->B+
78->B+
77->B+
76->B
74->B
73->B
72->B-
71->B-
70->B-
69->C+
68->C+
67->C+
66->C
65->C
63->C
62->C-
61->C-
60->C-
59->D+
58->D+
57->D+
56->D
54->D
53->D
52->D-
51->D-
50->D-
49->F
25->F
0->F

Whether mocks are used, and if so how?
Mocks will not be used since we are just trying to find out whether the expected values are correct when the function is called.

What supplied arguments will be provided and to which functions?
The supplied argument will be the percentage of each corresponding grade and it will be applied to the getLetterForNumericGrade method for each iteration of a grade.

What expected values will be observed?
The expected values that will be observed is the set of all letter grades that this program uses.
This would be A+,A,A-,B+,B,B-,C+,C,C-,D+,D,D-,F.

Whether the test passes?
All tests passes.

Task 2:
What the test case will verify?
The test will verify if using adding grades, that if the lettergrade conversion is working fine within them.
If addLetterGrade is adding properly.
If addNumericGrade is coverting to letter grade properly.

	Test 1: Check if lettergrade converter is working when adding one percentage mark with its parameter. If will check for 99 percent.

	Test 2: Check if lettergrade converter is working when adding two percentage marks with its parameter. If will check for 99 percent and 60 percent.

	Test 3: Check if lettergrade converter is working when adding five percentage marks with its parameter. If will check for 99, 60, 25, 59, 72 percent.

	Test 4: Check to see if one letter grade is being added to the term by checking if addGrade is being utilized in addLetterGrade. I will use the grade A.

	Test 5: Check to see if two letter grade is being added to the term by checking if addGrade is being utilized in addLetterGrade. I will use the grade A and grade B.

Whether mocks are used, and if so how?
Mocks will be used to see if the the assert is called for the conversion within the function of adding the grades.

What supplied arguments will be provided and to which functions?
The grade itself and the term will be provided for the arguments for each adding grade function.

What expected values will be observed?
If the conversion function is being utilized and that the grade is added to the term.

Whether the test passes?
All tests passes.

Task 3:
What the test case will verify?
If the grade are placed and that the right grades are returned back when finding them in the term.
If the term gets removed properly, when finding, it should return none.

	Test 1: Adds one grade to the term and shows that the term contains that grade. The grade used is A+.

	Test 2: Adds two grade to the term and shows that the term contains those grades. The grades used is A+, F.

	Test 3: Adds a grade in each term in two terms, and shows that the terms contains those grades. The grade used for term one is A+ and for term two is D-. 

	Test 4: Adds two grade in each term in two terms, and shows that the terms contains those grades. The grades used for term one is A+ and B- and for term two is D- and F. 

	Test 5: Creates a new term and removes it after. The output returns None. The term used is Fall.

	Test 6: Creates two new terms and removes it after. The output returns None. The terms used is Fall and Winter.
	
Whether mocks are used, and if so how?
Mocks will not be used, instead, unittest will then be used to see the return value. 

What supplied arguments will be provided and to which functions?
The grade that is being place in the terms and the term name.

What expected values will be observed?
Whether or not the grade added is there and whether or not the term is there when deleted.

Whether the test passes?
All tests passes.
