from graphene import ObjectType, String, Boolean, ID, Field, Int,List , Float
from utils import Util

class Response(ObjectType):
    query = String()
    response = String()
    model = String()
    
class Query(ObjectType):
    query = List(Response, user_input=String(), model=String(), context=String())
    
    def resolve_query(self, model, context, user_input):
        llm_util = Util(llm=model, context=context, user_input=user_input)
        response = llm_util.send_query()
        return_dict = {}
        return_dict.update({"response":response})
        return_dict.update({"query":query})
        return_dict.update({"model":model})
        return [return_dict]
