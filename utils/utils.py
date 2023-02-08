class Util(object):
  
  llm = none;
  
  def load_llm(self, name):
    
    match name:
      case "ChatGPT":
        llm = ChatGPT()
      case "Bard":
        # Bard has not been released
