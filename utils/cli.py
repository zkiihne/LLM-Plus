# cli for creating and using queries

# options for command:
# llm-plus
# --LLM [ChatGPT] 
# --context [string:string]
# --data_source [pokimon, todolist]
# --response_format [json, all_caps]
# --input_file [filename]

# a preview will be shown, then you will be asked to input your prompt text
data_sources = ["pokimon","todo-list"]
response_formats =["json","all_caps"]
llms = ["ChatGPT"]

def main():
    parser = argparse.ArgumentParser(description="Generate your LLM query.")
    parser.add_argument("-LLM", "--LLM", type=str, help="The LLM model you want to use", required=True, choices=llms)
    parser.add_argument("-c", "--context", type=str, help="The context you want to use in string:string format", required=False)
    parser.add_argument("-d", "--data_source", type=str, help="The datasources you want to include", required=False, choices=data_sources)
    parser.add_argument("-r", "--response_format", type=str, help="Any special formatting you want in the response", required=False, choices=response_formats)
    args = parser.parse_args()
    
    if args.llm == "ChatGPT":
        if not ChatGPT.verify_context(args.context):
            throw_error("Your context string for ChatGPT is wrong.")
    
    util = util(llm=args.llm, context=args.context, data_source=args.data_source, response_format=args.response_format)
    util.preview()
    
def throw_error(error_text):
    logging.error(error_text)
    exit(1)
if __name__ == "__main__":
    try:
        main()
    except ValidationException as e:
        logging.error(e)
    except Exception as e:
        logging.exception(e)
