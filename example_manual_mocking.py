#!/usr/bin/env python3

##
## A sample script showing construction and use of mocks
##

# import the mocking tools
import unittest.mock

# import the class we are testing
import gpa_calculator




##
## Mock in a stub from the converter
##


# Remember how we would normally call for a grade conversion
gradeletter = gpa_calculator.gpa_converter.getLetterForNumericGrade(87)
print("Result before mock with 87:", gradeletter)

gradeletter = gpa_calculator.gpa_converter.getLetterForNumericGrade(27)
print("Result before mock with 27:", gradeletter)


# Now prepare a mock to stub in the "conversion" so that we can
# ask questions of it, and install it into the converter
return_an_A_mock = unittest.mock.MagicMock(return_value = 'A')
old_getLetter = gpa_calculator.gpa_converter.getLetterForNumericGrade
gpa_calculator.gpa_converter.getLetterForNumericGrade = return_an_A_mock 

# Now we can call for the conversion to be performed, but use
# the mock to do it:
gradeletter = gpa_calculator.gpa_converter.getLetterForNumericGrade(87)
print("Result from mock call with 87:", gradeletter)

# Now that we have done that, we can ask the mock whether
# it was called correctly
gpa_calculator.gpa_converter.getLetterForNumericGrade.assert_called_with(87)
gpa_calculator.gpa_converter.getLetterForNumericGrade.assert_called_once()

# Note that because we replaced the real function with a mock, it
# will now always return 'A' because that is what we stubbed in
# as the return value:
gradeletter = gpa_calculator.gpa_converter.getLetterForNumericGrade(27)
print("Result from mock call with 27:", gradeletter)
gpa_calculator.gpa_converter.getLetterForNumericGrade.assert_called_with(27)


# Now remove the mock and put everything back
gpa_calculator.gpa_converter.getLetterForNumericGrade = old_getLetter

gradeletter = gpa_calculator.gpa_converter.getLetterForNumericGrade(51)
print("Result from real call with 51:", gradeletter)

