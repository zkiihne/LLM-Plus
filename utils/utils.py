class Util(object):
  
  def __init__(self, llm="ChatGPT", response_format="", data_source="", context=None):
    match llm:
      case "ChatGPT":
        self.llm = ChatGPT()
    self.response_format = response_format
    self.data_source = data_source
    self.context = context
    
    self.intro = "This is an intro"
    self.user_input = "[ user input here ]"
    
  def set_user_input(self, user_input):
    self.user_input = user_input
    
  def preview(self):
    print("Using LLM: " + self.llm.name)
    if self.context is not None:
      print("With context: " + self.context)
    print(self.construct_query())
    
  def construct_query(self):
    # constructs the query to be sent
    query = ""
    query += "\n" + self.intro
    query += "\n" + self.get_data_sources()
    query += "\n" + self.response_format
    query += "\n" + self.user_input
    return query
  
  def get_data_sources(self):
    return "None available"
  
  def send_query(self):
    query = self.construct_query()
    if (self.context is not None):
      self.llm.add_context(self.context)
    response = self.llm.ask(query)
    return response
