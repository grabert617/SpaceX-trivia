import unittest

from data import question_data

class TestTriviaQuestions(unittest.TestCase):
    
    def test_questions_have_answers(self):
        for question in question_data:
            self.assertIn("correct_answer", question, f"Question {question['question']} does not have a correct answer.")
    
    def test_question_answers_are_true_or_false(self):
        for question in question_data:
            self.assertIn(question['correct_answer'], ["True", "False"], f"Question {question['question']} has an invalid answer: {question['correct_answer']}")
    
    def test_number_of_questions(self):
        self.assertEqual(len(question_data), 10, "The number of questions is incorrect.")
    
    def test_first_question(self):
        self.assertEqual(question_data[0]["question"], "Elon Musk founded SpaceX in 2002", "The first question is incorrect.")
        self.assertEqual(question_data[0]["correct_answer"], "True", "The first question's answer is incorrect.")
    
    def test_second_question(self):
        self.assertEqual(question_data[1]["question"], "SpaceX first rocket was called Falcon 1", "The second question is incorrect.")
        self.assertEqual(question_data[1]["correct_answer"], "True", "The second question's answer is incorrect.")
        
    

if __name__ == '__main__':
    unittest.main()