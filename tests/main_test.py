import sys
import unittest
from lambda_files.chat_gpt_interactions import num_tokens_from_string 

class TestTikToken(unittest.TestCase):
    def test_tiktoken(self):
        str = "Hello there from test case land!"
        self.assertEqual(num_tokens_from_string(str, "gpt2"), 7)

# class TestCommandHandler(unittest.TestCase):
#     def test_longmessage_command(self): 
#         command = "longmessage"


#     def test_chatgptmessage_command(self): 
#         command = "chatgptmessage"
        
