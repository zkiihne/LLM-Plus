from llm.ChatGPT import ChatGPTModel

class Util(object):
  
  def __init__(self, llm="ChatGPT", response_format="", data_source="", context=None, file_name=""):
    if llm == "ChatGPT":
        self.llm = ChatGPTModel()
        
    self.response_format = response_format
    self.data_source = data_source
    self.context = context
    self.file_name = file_name
    
    self.intro = "I am going to send you a prompt. It might be long and broken into several parts. Please wait to respond until you see the phrase LLM_PLUS OUT"
    self.outro = "LLM_PLUS OUT"
    self.user_input = "[ user input here ]"
    
  def set_user_input(self, user_input):
    self.user_input = user_input
    
  def preview(self):
    print("Using LLM: " + self.llm.name)
    if self.context is not None:
      print("With context: " + self.context)
    query = self.construct_query()
    if len(query) <= 1000:
      print(query)
    else:
      print(query[0:1000])
    
  def construct_query(self):
    # constructs the query to be sent
    query = ""
    query += "\n" + self.intro
    query += "\n" + self.add_file()
    query += "\n" + self.get_data_sources()
    query += "\n" + self.response_format
    query += "\n" + self.user_input
    query += "\n" + self.outro
    return query
  
  def get_data_sources(self):
    return "None available"
  
  def send_query(self):
    query = self.construct_query()
    if self.context is not None:
      self.llm.add_context(self.context)
    response = self.llm.safe_ask(query)
    return response
  
  def add_file(self):
    if self.file_name is None:
      return "No file added"
    return open(self.file_name, 'r').read()
