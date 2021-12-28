# interviewer - a little bot helping you to prep your job interviews

## What it does
<code>interviewer</code> is a little python library that defines a bot to help you 
practice your interview skills. It basically prompts interview questions in your 
python console and stops the time it takes you to answer those. It is not much, 
but it definitely helped me to pick up some confidence.

## How it works
You can simply get <code>interviewer</code> from PyPi and run something like:

    pip install interviewer

Adjust this to your local python specs of course. To get the mock interview started, 
simply load the class from the library.

    from interviewer import interviewer

Next you can call the class and provide your custom questions as a <code>.txt</code> file.

    my_mock_interview = interviewer(questions_file='path_to_my_questions/question_file.txt')

Once you did that, you can just start the interview and press <code>enter</code> each time
you are done with a question. The time it takes you to answer each questions will be recorded.

    my_mock_interview.start()

To get an overview, of how long it took you to answer, you can use the analyze method.

    my_mock_interview.analyze()

Why is the timing important? First of all, you probably learn to get straight to the point
and second, it created a sense of urgency when practicing, which is certainly a good learning.