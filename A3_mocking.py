from unittest import mock
import unittest

# import the class we are testing
from gpa_calculator import gpa_calculation_mgr, gpa_converter, gpa_term_info

class TestCases(unittest.TestCase):

    def percentToLetterHelper(self, percentage, expected):
        letter = gpa_converter.getLetterForNumericGrade(percentage)
        self.assertEqual (expected, letter)

    def testAPlusHigh(self): 
        self.percentToLetterHelper(100, "A+")

    def testAPlusMid(self): 
        self.percentToLetterHelper(95, "A+")
    
    def testAPlusLow(self): 
        self.percentToLetterHelper(90, "A+")

    def testAHigh(self): 
        self.percentToLetterHelper(89, "A")

    def testAMid(self): 
        self.percentToLetterHelper(87, "A")
    
    def testALow(self): 
        self.percentToLetterHelper(85, "A")

    def testAMinusHigh(self): 
        self.percentToLetterHelper(84, "A-")

    def testAMinusMid(self): 
        self.percentToLetterHelper(82, "A-")
    
    def testAMinusLow(self): 
        self.percentToLetterHelper(80, "A-")

    def testBPlusHigh(self): 
        self.percentToLetterHelper(79, "B+")

    def testBPlusMid(self): 
        self.percentToLetterHelper(78, "B+")
    
    def testBPlusLow(self): 
        self.percentToLetterHelper(77, "B+")

    def testBHigh(self): 
        self.percentToLetterHelper(76, "B")

    def testBMid(self): 
        self.percentToLetterHelper(74, "B")
    
    def testBLow(self): 
        self.percentToLetterHelper(73, "B")

    def testBMinusHigh(self): 
        self.percentToLetterHelper(72, "B-")

    def testBMinusMid(self): 
        self.percentToLetterHelper(71, "B-")
    
    def testBMinusLow(self): 
        self.percentToLetterHelper(70, "B-")

    def testCPlusHigh(self): 
        self.percentToLetterHelper(69, "C+")

    def testCPlusMid(self): 
        self.percentToLetterHelper(68, "C+")
    
    def testCPlusLow(self): 
        self.percentToLetterHelper(67, "C+")

    def testCHigh(self): 
        self.percentToLetterHelper(66, "C")

    def testCMid(self): 
        self.percentToLetterHelper(65, "C")
    
    def testCLow(self): 
        self.percentToLetterHelper(63, "C")

    def testCMinusHigh(self): 
        self.percentToLetterHelper(62, "C-")

    def testCMinusMid(self): 
        self.percentToLetterHelper(61, "C-")
    
    def testCMinusLow(self): 
        self.percentToLetterHelper(60, "C-")

    def testDPlusHigh(self): 
        self.percentToLetterHelper(59, "D+")

    def testDPlusMid(self): 
        self.percentToLetterHelper(58, "D+")
    
    def testDPlusLow(self): 
        self.percentToLetterHelper(57, "D+")

    def testDHigh(self): 
        self.percentToLetterHelper(56, "D")

    def testDMid(self): 
        self.percentToLetterHelper(54, "D")
    
    def testDLow(self): 
        self.percentToLetterHelper(53, "D")

    def testDMinusHigh(self): 
        self.percentToLetterHelper(52, "D-")

    def testDMinusMid(self): 
        self.percentToLetterHelper(51, "D-")
    
    def testDMinusLow(self): 
        self.percentToLetterHelper(50, "D-")

    def testFHigh(self): 
        self.percentToLetterHelper(49, "F")

    def testFMid(self): 
        self.percentToLetterHelper(25, "F")
    
    def testFLow(self): 
        self.percentToLetterHelper(0, "F")
        
    @mock.patch.object(gpa_converter, 'getLetterForNumericGrade', autospec=True)
    def test_add_one_numeric_grade(self, mock_addPercent):
        student = gpa_calculation_mgr.calc_manager("StudentOne", "ID1")
        student.addNumericGrade("Winter", 99)
        mock_addPercent.assert_called_with(99)

    @mock.patch.object(gpa_converter, 'getLetterForNumericGrade', autospec=True)
    def test_add_two_numeric_grade(self, mock_addPercent):
        student = gpa_calculation_mgr.calc_manager("StudentOne", "ID1")
        student.addNumericGrade("Winter", 99)
        mock_addPercent.assert_called_with(99)
        student.addNumericGrade("Winter", 60)
        mock_addPercent.assert_called_with(60)

    @mock.patch.object(gpa_converter, 'getLetterForNumericGrade', autospec=True)
    def test_add_three_numeric_grade(self, mock_addPercent):
        student = gpa_calculation_mgr.calc_manager("StudentOne", "ID1")
        student.addNumericGrade("Winter", 99)
        mock_addPercent.assert_called_with(99)
        student.addNumericGrade("Winter", 60)
        mock_addPercent.assert_called_with(60)
        student.addNumericGrade("Winter", 25)
        mock_addPercent.assert_called_with(25)
        student.addNumericGrade("Winter", 59)
        mock_addPercent.assert_called_with(59)
        student.addNumericGrade("Winter", 72)
        mock_addPercent.assert_called_with(72)

    @mock.patch.object(gpa_term_info.TermInfo, 'addGrade', autospec=True)
    def test_add_one_letter_grade(self, mock_addLetter):
        student = gpa_calculation_mgr.calc_manager("StudentOne", "ID1")
        student.addLetterGrade("Winter", "A")
        mock_addLetter.assert_called()

    @mock.patch.object(gpa_term_info.TermInfo, 'addGrade', autospec=True)
    def test_add_two_letter_grade(self, mock_addLetter):
        student = gpa_calculation_mgr.calc_manager("StudentOne", "ID1")
        student.addLetterGrade("Winter", "A")
        mock_addLetter.assert_called()
        student.addLetterGrade("Winter", "B")
        mock_addLetter.assert_called()

    def test_add_one_letter_grade_to_term(self):
        addNewTerm = gpa_term_info.TermList(2,3)
        addNewTerm.addTerm("Fall")
        term = addNewTerm.getTerm("Fall")
        courses = gpa_term_info.TermInfo(term, 3)
        courses.addGrade("A+")
        grade = courses.getGrade(0)
        self.assertEqual(grade, "A+")

    def test_add_two_letter_grade_to_term(self):
        addNewTerm = gpa_term_info.TermList(2,3)
        addNewTerm.addTerm("Fall")
        term = addNewTerm.getTerm("Fall")
        courses = gpa_term_info.TermInfo(term, 3)
        courses.addGrade("A+")
        courses.addGrade("F")
        firstGrade = courses.getGrade(0)
        secondGrade = courses.getGrade(1)
        self.assertEqual(firstGrade, "A+")
        self.assertEqual(secondGrade, "F")

    def test_add_two_letter_grade_to_two_terms(self):
        addNewTerm = gpa_term_info.TermList(2,3)
        addNewTerm.addTerm("Fall")
        addNewTerm.addTerm("Winter")
        firstTerm = addNewTerm.getTerm("Fall")
        secondTerm = addNewTerm.getTerm("Winter")
        coursesTermOne = gpa_term_info.TermInfo(firstTerm, 3)
        coursesTermTwo = gpa_term_info.TermInfo(secondTerm, 3)
        coursesTermOne.addGrade("A+")
        coursesTermTwo.addGrade("D-")
        firstGrade = coursesTermOne.getGrade(0)
        secondGrade = coursesTermTwo.getGrade(0)
        self.assertEqual(firstGrade, "A+")
        self.assertEqual(secondGrade, "D-")

    def test_add_four_letter_grade_to_two_terms(self):
        addNewTerm = gpa_term_info.TermList(2,3)
        addNewTerm.addTerm("Fall")
        addNewTerm.addTerm("Winter")
        firstTerm = addNewTerm.getTerm("Fall")
        secondTerm = addNewTerm.getTerm("Winter")
        coursesTermOne = gpa_term_info.TermInfo(firstTerm, 3)
        coursesTermTwo = gpa_term_info.TermInfo(secondTerm, 3)
        coursesTermOne.addGrade("A+")
        coursesTermOne.addGrade("B-")
        coursesTermTwo.addGrade("D-")
        coursesTermTwo.addGrade("F")
        firstGrade = coursesTermOne.getGrade(0)
        secondGrade = coursesTermOne.getGrade(1)
        thirdGrade = coursesTermTwo.getGrade(0)
        forthGrade = coursesTermTwo.getGrade(1)
        self.assertEqual(firstGrade, "A+")
        self.assertEqual(secondGrade, "B-")
        self.assertEqual(thirdGrade, "D-")
        self.assertEqual(forthGrade, "F")

    def test_one_term_removal(self):
        addNewTerm = gpa_term_info.TermList(2,3)
        addNewTerm.addTerm("Fall")
        addNewTerm.removeTerm("Fall")
        term = addNewTerm.getTerm("Fall")
        self.assertEqual(term, None)
    
    def test_two_term_removal(self):
        addNewTerm = gpa_term_info.TermList(2,3)
        addNewTerm.addTerm("Fall")
        addNewTerm.addTerm("Winter")
        addNewTerm.removeTerm("Fall")
        addNewTerm.removeTerm("Winter")
        termOne = addNewTerm.getTerm("Fall")
        termTwo = addNewTerm.getTerm("Winter")
        self.assertEqual(termOne, None)
        self.assertEqual(termTwo, None)
        


if __name__ == '__main__':
	unittest.main()