import openai
import json

class Davinci003Model(object):

    ongoing_conversation = False
    name = "Davinci003"
    model_name = "text-davinci-003"
    api_key = None
    def get_key(self):
        with open('key.json', mode='r') as key_file:
            key = json.loads(key_file.read())['key']
        self.api_key = key
        
    def safe_to_send(self, prompt):
        if len(prompt) > 8000:
            return False    
        return True
        
    def get_context(self):
        return ""

    def add_context(self, context_id):
        # add a context
        pass
    
    def safe_ask(self, prompt, reset_conversation=False, context=None):
        # ask model with any length query
        if not self.safe_to_send(prompt):
            return "Prompt is not fit for this model"
        result = self.ask(prompt)

    def ask(self, prompt):
        # vanilla ask
        if self.api_key is None:
            self.get_key()
            openai.api_key = self.api_key
        response = openai.Completion.create(
          engine=self.model_name,
          prompt=prompt,
          temperature=0.75,
          max_tokens=2048,
          top_p=1.0,
          frequency_penalty=0.0,
          presence_penalty=0.0
        )
        return response['choices'][0]['text']
