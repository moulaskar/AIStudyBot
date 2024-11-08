
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def get_prompt(question, logger):
    # Define the prompt template with a placeholder for the question
    template = """
    Question: {question}

    Answer:
    """
    prompt = PromptTemplate(template=template, input_variables=["question"])
    msg = f'get_prompt - {prompt} generated for {question}'
    logger.logMsg(msg)
    return prompt

def run_service(llm, question, logger):
    prompt = get_prompt(question, logger)

    try:
        # Create an LLMChain to manage interactions with the prompt and model
        llm_chain = LLMChain(prompt=prompt, llm=llm)
    except Exception as err:
        msg = f'run_service - Creating LLMChain failed : {err}'
        logger.logMsg(msg)
        return None

    logger.logMsg("Chatbot initialized, ready to chat...")
    answer = llm_chain.run(question)
    return answer