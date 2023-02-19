from chatgpt_wrapper import ChatGPT
from transformers import GPT2Tokenizer

class ChatGPTModel(object):
    # gpt2 and gpt3 use the same tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    ongoing_conversation = False
    chatGPTBot = ChatGPT()
    name = "ChatGPT"

    first_request_prompt = "I am going to give you the following document in passages. Do not respond with anything more than ok until the final passage. Here is the first passage: "
    middle_request_prompt = "Here is the next passage: "
    last_request_prompt = "Here is the final passage:"

    def tokenize(self, input_string):
        return self.tokenizer(input_string)

    def count_tokens(self, input_string):
        return len(self.tokenize(input_string)['input_ids'])

    def send_to_chatGPT(self, prompt, reset_conversation=False):
        if reset_conversation:
            self.clear_conversation()
        return self.chatGPTBot.ask(prompt)

    def get_context(self):
        return self.chatGPTBot.parent_message_id + ":" + self.chatGPTBot.conversation_id

    def add_context(self, context_id):
        try:
            (conversation_id, parent_message_id) = context_id.split(":")
            assert conversation_id == "None" or len(conversation_id) == 36
            assert len(parent_message_id) == 36
        except Exception as e:
            print(e)
            raise
        if conversation_id == "None":
            conversation_id = None
        self.chatGPTBot.parent_message_id = parent_message_id
        self.chatGPTBot.conversation_id = conversation_id

    def safe_ask(self, prompt, reset_conversation=False, context=None):
        # reset conversation if needed
        if reset_conversation or not self.ongoing_conversation:
            self.clear_conversation()
            ongoing_conversation = True
        # load context if needed
        if context is not None:
            self.load_context(context)
        # break up text, if less than 8000 will be an array with one element
        text_chunks = self.break_up_text(prompt)
        # send to chatGPt
        response = ""
        for i in range(0, len(text_chunks)):
            first = (i == 0)
            last = (i == len(text_chunks) - 1)
            middle = (not first and not last)
            prompt = ""

            if first:
                prompt += self.first_request_prompt
            elif middle:
                prompt += self.middle_request_prompt
            elif last:
                prompt += self.last_request_prompt

            prompt += text_chunks[i]
            try:
                response = self.chatGPTBot.ask(prompt)
            except Exception as e:
                print(e)
                raise
        return response

    def break_up_text(self, input_string, chunk_size=8000):
        # rather than break it into chunks by token we are doing it in chunks by character.
        # there is roughly 4 characters per token and we can have up to 2000 tokens, leaving us with a 8000 character chunk size.
        return [input_string[y - chunk_size:y] for y in range(chunk_size, len(input_string) + chunk_size, chunk_size)]

    def read_file(self, filename):
        with open(filename, "r", encoding='utf-8') as f:
            string = f.read()
        return string

    def clear_conversation(self):
        try:
            self.chatGPTBot.new_conversation()
            self.ongoing_conversation = False
        except Exception as e:
            print(e)
            raise

    def ask(self, prompt):
        return self.chatGPTBot.ask(prompt)
