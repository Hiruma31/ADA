import settings
# RegExp
import re
# PyAIML
import aiml
import commands


def command_handler():
    """
    Handle the converted to text order to dispatch to the right module
    """

def regexp_handled(text_order):
    # RegExp  Handler test
    re_test = re.search('^()$',text_order)
    if re_test:
        print "Test complete."


def aiml_handled():
    # PyAIML handler test
    KERNEL = aiml.Kernel()
    # Load the AIML file
    KERNEL.learn("resources/test_AIML.aiml")
    # Set the name as a constant
    KERNEL.setBotPredicate("name", settings.SYSTEM_NAME)

    while True:
        input = raw_input("> ")
        response = KERNEL.respond(input)
        print response      # Print the answer
        print commands.getoutput("/usr/bin/espeak -v en+f4 -p 99 -s 160 \"" + response + "\"")  # Say the answer