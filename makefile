
# Makefile for directory maintainence

top :
	echo "The only useful target in this makefile is 'clean'"
	echo "The 'clean' target removes the python cache"

clean :
	- rm -rf gpa_calculator/__pycache__
	- rm -rf __pycache__

