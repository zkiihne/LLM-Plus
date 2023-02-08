class Util(object):
  
  def __init__(self, llm="ChatGPT", ):
    self.llm = llm
    
    self.user_input = "[ user input here ]"
      
  def set_user_input(self, user_input):
    self.user_input = user_input
    
  def preview(self):
    print(construct_query)
    
  def construct_query(self):
    # constructs the query to be sent
