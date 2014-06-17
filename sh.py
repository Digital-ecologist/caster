#
# This file is a command-module for Dragonfly.
# (c) Copyright 2008 by Christo Butcher
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#

"""
Command-module for git

"""


#---------------------------------------------------------------------------

from dragonfly import (Grammar, AppContext, MappingRule,
                       Key, Text)


class CommandRule(MappingRule):

    mapping = {
        "initialize":       Text( "git init" )+Key("enter"),
        "add":              Text( "git add ." )+Key("enter"),
        "status":           Text( "git status" )+Key("enter"),
        "commit":           Text( "git commit -am ''" )+Key("left"),
        "push":             Text( "git push" )+Key("enter"),
        "pull":             Text( "git pull" )+Key("enter"),
        "CD up":            Text( "cd .." )+Key("enter"),
        "CD":               Text( "cd " ),
        "list":             Text( "ls" )+Key("enter"),
        "make directory":   Text( "mkdir " ),
        "exit":             Text( "exit" )+Key("enter"),
        
        }
    extras = [
              
             ]
    defaults ={}


#---------------------------------------------------------------------------

context = AppContext(executable="sh")
grammar = Grammar("MINGW32", context=context)
grammar.add_rule(CommandRule())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None