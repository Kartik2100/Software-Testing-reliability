
import sys
from .gpa_converter import getGPAforLetterGrade, getLetterForNumericGrade

# Information for all terms
class TermList:
	def __init__(self, maxNumTerms, maxNumCourses):
		self.dict = {}
		self.maxNumTerms = maxNumTerms
		self.maxNumCourses = maxNumCourses

	def getTerm(self, termName):
		if termName in self.dict:
			return self.dict[termName]
		return None

	def getTermNameList(self):
		return list(self.dict.keys())

	def addTerm(self, termName):
		if len(self.dict) >= self.maxNumTerms:
			return None
		newTerm = TermInfo(termName, self.maxNumCourses)
		self.dict[termName] = newTerm
		return newTerm

	def removeTerm(self, termName):
		if termName in self.dict:
			del self.dict[termName]

# Information for a specific term
class TermInfo:
	def __init__(self, termName, maxNumCourses):
		self.termName = termName
		self.maxNumCourses = maxNumCourses
		self.letterGrades = []

	def getTermName(self):
		return self.termName

	def getGrades(self):
		return self.letterGrades

	def getNGrades(self):
		return len(self.letterGrades)

	def getGrade(self, index):
		return self.letterGrades[index]

	def addGrade(self, letterGrade):
		if len(self.letterGrades) >= self.maxNumCourses:
			return False
		self.letterGrades.append(letterGrade)
		return True

