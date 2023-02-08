class TestChatGPTUtil(unittest.TestCase):
    testChatGPTUtil = ChatGPTUtil()

    def test_(self):
        self.assertEqual(1 + 1, 2)

    def test_count_tokens(self):
        self.testChatGPTUtil.clear_conversation()

        self.assertEqual(self.testChatGPTUtil.count_tokens("this is just a tester prompt"), 7)
        self.assertEqual(self.testChatGPTUtil.count_tokens(
            "The quick brown fox jumps over the lazy dog. This is a typical prompt used for testing because it contains every letter of the alphabet. You can find it everywhere in test cases if you pay attention."),
                         40)

    def test_read_file(self):
        self.testChatGPTUtil.clear_conversation()

        threektokens_string = self.testChatGPTUtil.read_file("threektokens.txt")
        self.assertEqual(self.testChatGPTUtil.count_tokens(threektokens_string), 3000)

    def test_break_up_text(self):
        self.testChatGPTUtil.clear_conversation()
        threektokens_string = self.testChatGPTUtil.read_file("threektokens.txt")

        self.assertEqual(len(self.testChatGPTUtil.break_up_text(threektokens_string)), 2)

    def test_send_to_chatGPT_3000_tokens(self):
        self.testChatGPTUtil.clear_conversation()
        threektokens_string = self.testChatGPTUtil.read_file("threektokens.txt")
        response = self.testChatGPTUtil.send_large_document_to_chatGPT(threektokens_string)
        self.assertGreater(len(response), 0)

    def test_send_to_chatGPT_load_context(self):
        self.testChatGPTUtil.clear_conversation()
        # Context:  I am going to give you two numbers to add. When you respond, respond with their sum, and only their sum. For example, me:'1+1', you:'2'
        prompt = "1 1"
        context = "12beda58-9cdd-4ea7-b94f-73195241af0f:9e77fd54-611f-4834-a780-c79d807242c2"
        self.testChatGPTUtil.load_context(context)
        response = self.testChatGPTUtil.ask(prompt)
        self.assertEqual(response.strip(), "2")

    def test_load_text_and_ask(self):
        self.testChatGPTUtil.clear_conversation()
        tester_string = self.testChatGPTUtil.read_file("tester.txt")
        self.testChatGPTUtil.send_large_document_to_chatGPT(tester_string)
        print(self.testChatGPTUtil.ask("What happens in a race to X runs when neither team gets to X?"))

    def test_load_context_and_ask(self):
        self.testChatGPTUtil.clear_conversation()
        self.testChatGPTUtil.load_context("2216a727-9fd9-4a48-baed-b5f7a8080917:c173a77c-949a-453e-9c8d-acc31ab8084a")
        print(self.testChatGPTUtil.ask("What happens in a race to X runs when neither team gets to X?"))

if __name__ == "__main__":
    unittest.main()
