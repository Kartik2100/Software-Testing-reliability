#!/usr/bin/env python3

##
## A sample script showing construction and use of mocks
##

from unittest import mock
import unittest

# import the class we are testing
from gpa_calculator import gpa_calculation_mgr, gpa_converter, gpa_term_info


class SampleTestCase(unittest.TestCase):
	## Use the @patch.object decorator to replace the named method
	## on the indicated class with a unittest.MagicMock based replacement.
	##
	## The use of autospec=True means that the MagicMock will be built
	## using the API/signature of the entity being mocked
	##
	## This decorator has scope only for the function/method immediately
	## following the decorator declaration, and after use removes itself
	## from the patched object
	##
	## The mocked object(s) appear as arguments to the function.  If more
	## than one @patch is used, the arguments appear in R-to-L order: for
	## example:
	##    @mock.patch(obj, 'A')
	##    @mock.patch(obj, 'B')
	##    @mock.patch(obj, 'C')
	##    def testfunction(self, mockC, mockB, mockA)
	@mock.patch.object(gpa_converter, 'getLetterForNumericGrade', autospec=True)
	def test_getLetter(self, mock_getLetter):

		## 
		student = gpa_calculation_mgr.calc_manager("STUDENT", "ID")
		student.addNumericGrade("Fall", 87)
		mock_getLetter.assert_called_with(87)
		mock_getLetter.assert_called_once()


## If being run as a program, run the test suite.
## This allows this suite to be loaded and run within other
## larger test suites and treated as a module
if __name__ == '__main__':
        unittest.main()

