
## Import the critical pieces
import sys
from gpa_calculator import *
import gpa_calculator.gpa_converter
from  gpa_calculator.gpa_term_info import *


##
## Manage the information for a student
##

class calc_manager:

	GPA_MAX_COURSES_PER_TERM	= 6
	GPA_MAX_TERMS_PER_STUDENT	= 32

	##
	## Constructor.  Initialize with zeros.
	## @param studentName full name of student
	## @param studentID student ID number
	def __init__(self, studentName, studentID):

		self.terms = TermList(
				self.GPA_MAX_TERMS_PER_STUDENT,
				self.GPA_MAX_COURSES_PER_TERM)
		self.studentName = studentName
		self.studentID = studentID
		self.converter = gpa_calculator.gpa_converter

	##
	## Add a letter grade to the list
	## @param term string describing the term, e.g.; "Fall 2017"
	## @param lettergrade a grade letter, such as "B+"
	## @return negative on failure
	def addLetterGrade(self, termName, lettergrade):

		## search for other uses of this term
		thisTerm = self.terms.getTerm(termName)

		## if self term is new, add it
		if thisTerm is None:
			thisTerm = self.terms.addTerm(termName)

		thisTerm.addGrade(lettergrade)


	##
	## Add a numeric grade to the list
	## @param term string describing the term, e.g.; "Fall 2017"
	## @param percentageGrade a numeric grade, such as 78 (percent)
	## @return negative on failure
	def addNumericGrade(self, term, percentageGrade):

		letterGrade = gpa_calculator.gpa_converter.\
				getLetterForNumericGrade(percentageGrade)

		return ( self.addLetterGrade(term, letterGrade) )


	##
	## @return GPA calculated for the matching term
	## @param term string describing the term, e.g.; "Fall 2017"
	## @return GPA calculated for self term
	def getTermGPA(self, termName):

		## search for other uses of this term
		thisTerm = self.terms.getTerm(termName)

		##  if self term is not found, GPA is negative infinity
		if thisTerm is None:
			return float('-inf')

		## calculate the average over self term
		gpaSummation = 0
		for grade in thisTerm.getGrades():
			gpaSummation += gpa_calculator.gpa_converter.\
					getGPAforLetterGrade( grade )

		return gpaSummation / float(thisTerm.getNGrades())


	##
	## @return overall GPA, calculated across all terms
	def getOverallGPA(self):

		gpaSummation = 0
		for termName in self.terms.getTermNameList():
			gpaSummation += self.getTermGPA(termName)
			thisTerm = self.terms.getTerm(termName)

		nTerms = len(self.terms.getTermNameList())
		return gpaSummation / float(nTerms)

	##
	## Remove an entire term
	def removeInfoForTerm(self, termName):
		self.terms.removeTerm(termName)

