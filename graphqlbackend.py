from graphene import ObjectType, String, Boolean, ID, Field, Int,List , Float
from utils import Util

class Response(ObjectType):
    user_input = String()
    response = String()
    model = String()
    
class Query(ObjectType):
    ask_model = List(Response, dummy=String(), user_input=String(), model=String(), context=String())
    
    def resolve_ask_model(self, dummy, model, context, user_input):
        llm_util = Util(llm=model, context=context, user_input=user_input)
        response = llm_util.send_query()
        return_dict = {}
        return_dict.update({"response":response})
        return_dict.update({"user_input":user_input})
        return_dict.update({"model":model})
        return [return_dict]
