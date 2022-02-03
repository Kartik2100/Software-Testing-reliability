
import sys

##
## Do the basic conversion back and forth work between letters, percentages
## and GPA values
##

## Convert from percentage to letter.
## @param percentageGrade a numeric grade, such as 78 (percent)
## @return a gradeletter string based on an integer grade [0-100]
def getLetterForNumericGrade(percentageGrade):

	if percentageGrade < 0 or percentageGrade > 100:
		return None

	for gradeConversion in sGradeConversions():
		if gradeConversion.lo <= percentageGrade \
				and percentageGrade <= gradeConversion.hi:
			return gradeConversion.letter

	# we should never get here

##
## Convert from letter to GPA.
## @param letterGrade the grade letter to convert (e.g.; "B-")
## @return GPA from a letter grade
def getGPAforLetterGrade(letterGrade):

	for gradeConversion in sGradeConversions():
		if gradeConversion.letter == letterGrade:
			return gradeConversion.gpa

	## we got an invalid letter grade
	sys.stderr.write(
			"Letter grade '%s' not an allowable grade\n"
			% letterGrade)
	return float("NaN")

##
## Convert from letter grade partition index  to GPA.
## @param letterIndex the index [0-13] of the letter grade
## @return GPA based on index of letter grade
def getGPAforLetterIndex(letterIndex):
	gradeConversions = sGradeConversions()
	return gradeConversions[letterIndex].gpa

##
## Convert from percentage to GPA.
## @param percentageGrade a numeric grade, such as 78 (percent)
## @return GPA based on a numeric percentage grade
def getGPAforNumericGrade(percentageGrade):
	return getGPAforLetterGrade(
			getLetterForNumericGrade(percentageGrade)
		)

### A+ is index zero
GPA_A_PLUS		= 0x00
GPA_A			= 0x01
GPA_A_MINUS		= 0x02
GPA_B_PLUS		= 0x03
GPA_B			= 0x04
GPA_B_MINUS		= 0x05
GPA_C_PLUS		= 0x06
GPA_C			= 0x07
GPA_C_MINUS		= 0x08
GPA_D_PLUS		= 0x09
GPA_D			= 0x10
GPA_D_MINUS		= 0x11
GPA_F			= 0x12

class GPAconversion:
	def __init__(self, description, gpa, letter, lo, hi):
		self.description = description
		self.gpa = gpa
		self.letter = letter
		self.lo = lo
		self.hi = hi

## class method to create the singleton conversions
sGradeConversions__ = None

def sGradeConversions():
	global sGradeConversions__
	if sGradeConversions__ is None:
		sGradeConversions__ = []

			##	           Description		GPA		Letter		Low	High
		sGradeConversions__.append( GPAconversion(
			"Outstanding",		4.3,	"A+",		90,	100	))
		sGradeConversions__.append( GPAconversion(
			"Excellent",		4.0,	"A",		85,	89	))
		sGradeConversions__.append( GPAconversion(
			"Very Good",		3.7,	"A-",		80,	84	))
		sGradeConversions__.append( GPAconversion(
			"Good",				3.3,	"B+",		77,	79	))
		sGradeConversions__.append( GPAconversion(
			"Good",				3.0,	"B",		73,	76	))
		sGradeConversions__.append( GPAconversion(
			"Good",				2.7,	"B-",		70,	72	))
		sGradeConversions__.append( GPAconversion(
			"Satisfactory",		2.3,	"C+",		67,	69	))
		sGradeConversions__.append( GPAconversion(
			"Satisfactory",		2.0,	"C",		63,	66	))
		sGradeConversions__.append( GPAconversion(
			"Satisfactory",		1.7,	"C-",		60,	62	))
		sGradeConversions__.append( GPAconversion(
			"Marginal Pass",	1.3,	"D+",		57,	59	))
		sGradeConversions__.append( GPAconversion(
			"Marginal Pass",	1.0,	"D",		53,	56	))
		sGradeConversions__.append( GPAconversion(
			"Marginal Pass",	0.7,	"D-",		50,	52	))
		sGradeConversions__.append( GPAconversion(
			"Failure",			0.0,	"F",		0,	49	))

	return sGradeConversions__

