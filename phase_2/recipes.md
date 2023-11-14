User Story:
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.


Function Signature: estimate_reading_time
Parameters and type: text: string
Return type: float
Side effects: none

Test Examples:
test_three_hundred_words_takes_one_point_five_minutes 300 word string input returns 1.5
test_seven_hundred_words_takes_three_point_five_minutes: 700 word input string returns 3.5

Implement the behaviour:
tests now pass


User Story:
As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.
Function Signature: check_sentence_grammar
Parameters and type: sentence (type:string)
Return type: boolean 
Side effects: none

Test Examples:
check_sentence_grammer('Will this pass?') will return True
check_sentence_grammer('this will not pass!') will return False
check_sentence_grammar('This will not pass') will return False
check_sentence_grammar('This is a sentence and it will pass.') will return True

Implement the behaviour:
function now works


User Story:
As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.
Aft
Function Signature: checks_contains_todo
Parameters and type: text (type:string)
Return type: Boolean
Side effects: none

Test Examples:
check_contains_todo(text which contains # TODO) will return True (test with # TODO in multiple positions)
check_contains_todo(text without # TODO) will return False
Implement the behaviour:
function now works