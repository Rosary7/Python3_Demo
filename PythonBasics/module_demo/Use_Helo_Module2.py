# Example for  importing specific attributes from a module
# Syntax: from modname import name1[, name2[, ... nameN]]
# Note: Place the module file in '<python_home>/lib' folder

from Create_Helo_Module import func_disp

# We can now call the 'func_disp()' method from 'Create_Helo_Module's module
func_disp()
