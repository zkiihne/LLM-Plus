# cli for creating and using queries

# options for command:
# llm-plus
# --LLM [ChatGPT] 
# --context [string:string]
# --data_source [pokimon, todolist]
# --response_format [json, all_caps]
# --input_file [filename]

# a preview will be shown, then you will be asked to input your prompt text


def main():
    parser = argparse.ArgumentParser(description="Generate your LLM query.")
    parser.add_argument("-LLM", "--LLM", type=str, help="The LLM model you want to use", required=True)
    parser.add_argument("-c", "--context", type=str, help="The context you want to use in string:string format", required=False)
    parser.add_argument("-d", "--data_source", type=str, help="The datasources you want to include", required=False, choices=[
            "pokimon","todo-list"])
    parser.add_argument("-r", "--response_format", type=str, help="Any special formatting you want in the response", required=False, choices=[
            "json","all_caps"])
    args = parser.parse_args()
    
    if args.llm == "ChatGPT":
        if not ChatGPT.verify_context(args.context):
            logging.error("Your context string for ChatGPT is wrong.")
            exit(1)
        if not args.data_source in Utils.get_data_sources()
                 logging.error(
                "Your context string for ChatGPT is wrong."
            )
            exit(1)
#     qr_code = QRCode(name=args.name, birth=args.birth, vaccine=[Vaccination(args.manufacturer[i], args.date[i]) for i in range(len(args.date))])
#     generate_qr_code(qr_code)
def throw_error(error_text):
                logging.error("Your context string for ChatGPT is wrong.")
            exit(1)
if __name__ == "__main__":
    try:
        main()
    except ValidationException as e:
        logging.error(e)
    except Exception as e:
        logging.exception(e)
