# cli for creating and using queries

# options for command:
# llm-plus
# --LLM [ChatGPT] 
# --context [string:string]
# --data_source [pokimon, todolist]
# --response_format [json, all_caps]
# --input_file [filename]

# a preview will be shown, then you will be asked to input your prompt text

import argparse
from utils import Util

data_sources = ["pokimon","todo-list"]
response_formats =["json","all_caps"]
llms = ["ChatGPT"]

def main():
    parser = argparse.ArgumentParser(description="Generate your LLM query.")
    parser.add_argument("-l", "--llm", type=str, help="The LLM model you want to use", required=True, choices=llms)
    parser.add_argument("-c", "--context", type=str, help="The context you want to use in string:string format", required=False)
    parser.add_argument("-d", "--data_source", type=str, help="The datasources you want to include", required=False, choices=data_sources)
    parser.add_argument("-r", "--response_format", type=str, help="Any special formatting you want in the response", required=False, choices=response_formats)
    args = parser.parse_args()
    
# uncomment after ChatGPT is running
#     if args.llm == "ChatGPT":
#         if not ChatGPT.verify_context(args.context):
#             throw_error("Your context string for ChatGPT is wrong.")
    response_format = args.response_format if args.response_format is not None else ""
    data_source = args.data_source if args.data_source is not None else ""

    llm_util = Util(llm=args.llm, context=args.context, data_source=data_source, response_format=response_format)
    llm_util.preview()
    
def throw_error(error_text):
    print(error_text)
    exit(1)
    
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)