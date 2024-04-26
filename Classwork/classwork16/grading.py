###
#  filename: grading.py
#  purpose: demonstrate simple python coding
#  author: Dr. Johnson
#  date: 2024-04-23
###

homework01     = 0.0
homework02     = 0.0
homework03     = 0.0
homework04     = 0.0
quiz01         = 0.0
quiz02         = 0.0
final          = 0.0
participation  = 0.0
githubstruct   = 0.0

def instructions():
   print( "\n\n   This program will calculate your grade for the course" )
   print( "   There are four homework assignments worth 5% each" )
   print( "   There are two quizzes, one worth 15% the other worth 20%" )
   print( "   There is a final, worth 30%" )
   print( "   Class participation is worth 10%")
   print( "   Your GitHub structure setup is worth 5%")
   print( "   Use these values to calculate your score for the course." )
   return

def gradeEntry( which ):
   prompt = "   Enter your grade for " + which + ": "
   value = float( input( prompt ))
   return value

def main():
   score = 0.0
   instructions()
   homework01 = gradeEntry( "homework01" )
   homework02 = gradeEntry( "homework02" )
   homework03 = gradeEntry( "homework03" )
   homework04 = gradeEntry( "homework04" )
   quiz01 = gradeEntry( "quiz01" )
   quiz02 = gradeEntry( "quiz02" )
   final = gradeEntry( "final" )
   participation = gradeEntry( "participation" )
   githubstruct = gradeEntry( "githubstruct" )
   score = (5.0  * (homework01 / 100.0)) + (5.0  * (homework02 / 100.0)) + \
           (5.0  * (homework03 / 100.0)) + (5.0  * (homework04 / 100.0)) + \
           (15.0 * (quiz01 / 100.0)) + (20.0 * (quiz02 / 100.0)) + \
           (30.0 * (final / 100.0)) + (10.0 * (participation / 100.0)) + \
           (5.0  * (githubstruct / 100.0))
   print( "\n\n   Your score for the course is: ", score )

main()
