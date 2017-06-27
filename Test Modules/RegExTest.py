import re

text_sample = """
Micros

Stationery Office.  Crown Copyright. Licence No: 0100040692.
Unauthorised reproduction infringes Crown Copyright and may lead to prosecution or civil
proceedings.
This drawing is the property of Network Rail. It shall not be reproduced in whole or in part, nor
disclosed to a third party, without the written permission of the appropriate Programme
Director.
Copyright 2010 Network Rail.
Note: This drawing has been extracted from a model that contains information imported directly from models
provided by other disciplines, and may be subject to further design development up to the AFC issue date.
Note: The works illustrated in the ar
ea outlined in blue are subject to amendments
through a parallel GRIP4
& 5 design process. They are indicative and provided for context only
GRIP 5
 1 : 100B0229/04/1629/04/16
29/04/16Mechanical Engineering ServicesMPMGSTEGIP19-ARP-DRG-EDR-52-091
Queen Street Station - North Hanover Site
MPMGSTP01WORK IN PROGRESSRevDateDescriptionDrwnChk'd
B0105/04/16GRIP 4MGRF

B0229/04/16GRIP 4 REVISED DRAWINGMGST

"""

def RegExTest(input_text):
    regex_format = input("Enter Sample Drawing Number: ")
    output_text = ""
    regex_variable = "."
    for char in regex_format:
        if char == "-":
            output_text += "-"
        else:
            output_text += regex_variable
    output_text += ""
    print (output_text)
    return re.search(output_text, input_text)



if __name__ == '__main__':
    text_return = RegExTest(text_sample)
    print (text_return.group(0))