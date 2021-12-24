"""
bot.py contains the main class interviewer. Per default the questions are gathered
from interviewer/questions.txt. However, users can provide their own custom questions.
"""

# import libs
import random
import os
import time
import pprint

# main class
class interviewer:

    # define the class object
    def __init__(self, questions_file=None):

        # if no question file is provided load the default
        if questions_file is None:

            # store the questions
            self.questions = open('interviewer/questions.txt').read().splitlines()

        # if user provides question file
        else:

            # store the questions
            self.questions = open(questions_file).read().splitlines()

        # random seed
        random.seed(10)

        # randomly shuffle order of the list
        random.shuffle(self.questions)

    # main method for questions
    def start(self):

        # construct the message
        msg_text = """

        ██╗███╗   ██╗████████╗███████╗██████╗ ██╗   ██╗██╗███████╗██╗    ██╗███████╗██████╗         
        ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗██║   ██║██║██╔════╝██║    ██║██╔════╝██╔══██╗        
        ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝██║   ██║██║█████╗  ██║ █╗ ██║█████╗  ██████╔╝        
        ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗╚██╗ ██╔╝██║██╔══╝  ██║███╗██║██╔══╝  ██╔══██╗        
        ██║██║ ╚████║   ██║   ███████╗██║  ██║ ╚████╔╝ ██║███████╗╚███╔███╔╝███████╗██║  ██║        
        ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝ ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝        
                                                                                                                                             
        
            Welcome to your interview trainings bot. I will be challenging you,
            with a number of relevant questions. I have prepared {number_of_questions}
            question for you, so let's get started and good luck to you.
        
        """.format(number_of_questions = len(self.questions))

        # print
        print(msg_text)

        # construct data set to track timing
        summary = {}

        # welcome message
        pprint.pprint('Welcomne to your mock interview. Please tell me a bit about yourself.')

        # store the time
        start_time = time.time()

        # wait for input
        input('>>> press enter when you are done <<<')

        # get the response time
        response_time = round((time.time() - start_time)/60, 2)

        # store in summary
        summary['Introduction'] = {}

        # store time in introduction
        summary['Introduction']['response_time'] = response_time

        # loop through all questions
        for question in self.questions:

            # record the time
            start_time = time.time()

            # get position of the question
            question_position = self.questions.index(question)

            # print out question
            print(str('Q: ' + question))

            # wait for input 
            input('>>> press enter when you are done <<<')

            # record time
            response_time = round((time.time() - start_time)/60, 2)

            # add sub list to dict
            summary[str('Question ' + str(question_position))] = {}

            # add question
            summary[str('Question ' + str(question_position))]['question'] = question

            # add response tie
            summary[str('Question ' + str(question_position))]['response time'] = response_time

        # store the summary
        self.summary = summary
    
    # main function to analyze
    def analyze(self):

        # pretty print the summary
        pprint.pprint(self.summary)