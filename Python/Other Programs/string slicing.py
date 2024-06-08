#Given a string of braces named bound_by, and a string named tag_name. The task is to print a new string such that tag_name is in the middle of bound_by.

def join_middle(bound_by, tag_name):
  # complete the statement below to return the string as required
  
  print( bound_by[0 : 2   ] + tag_name + bound_by[ 2: ])

join_middle( "[[]]","tag" )