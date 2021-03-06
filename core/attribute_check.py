"""
MIT License

Copyright (c) 2020 NaveenKumar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from utils.display import print_message, Colors


def attribute_check(tree, element):
    """
    Performs additional attribute checks on IfController or LoopController
    @param tree: The parsed JMX
    @param element: The element to check
    """
    root = tree.getroot()
    # Set flag = 1 for issue found
    flag = 0
    for node in root.iter(element):
        #
        for child in node.getchildren():
            for i, j in child.attrib.items():
                # print(i, j)
                if str(j) == 'IfController.useExpression':
                    # Set flag = 0 for no issues
                    flag = 0
                elif str(j) == 'LoopController.loops':
                    loop_count = child.text
                    if int(loop_count) == -1:
                        flag = 0
                else:
                    flag = 1
    if flag == 1:
        if element == 'IfController':
            print_message(message_color=Colors.white, message="For performance, check \"Interpret Condition as Variable"
                                                              " Expression\" in If Controller.")
        elif element == 'LoopController':
            print_message(message_color=Colors.white, message="Loop Count is set to infinity. Double check "
                                                              "the count before you start the test.")
