class Util(object):
  
  def __init__(self, llm="ChatGPT", response_format="", data_source="", context=None):
    self.llm = llm
    self.response_format = response_format
    self.data_source = data_source
    self.context = context
    
    self.intro = "This is an intro"
    self.user_input = "[ user input here ]"
    
  def set_user_input(self, user_input):
    self.user_input = user_input
    
  def preview(self):
    print("Using LLM: " + self.llm)
    print("With context: " + self.context)
    print(construct_query())
    
  def construct_query(self):
    # constructs the query to be sent
    query = self.intro
    query += "\n" + self.get_data_source(data_source)
    query += "\n" + self.response_format
    query += "\n" + self.user_input
    return query
  
  def send_query(self):
    query = self.construct_query()
    if (self.context is not None):
      self.llm.add_context(self.context)
    response = self.llm.ask(query)
    return response
