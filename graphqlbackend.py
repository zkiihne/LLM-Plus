from graphene import ObjectType, String, Boolean, ID, Field, Int,List , Float

class Query(ObjectType):
    query = List(user_input=String(), model=String(), context=String())
    
    def resolve_query(self, model, context, user_input):
        llm_util = Util(llm=model, context=context, user_input=user_input)
        response = llm_util.send_query()
        return [response]
