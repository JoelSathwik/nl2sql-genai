from llama_cpp import Llama
import os

# Load the model (do this once to reuse)
LLM_MODEL_PATH = "models\capybarahermes-2.5-mistral-7b.Q4_K_M.gguf" # update if your filename is different
llm = Llama(model_path=LLM_MODEL_PATH, n_ctx=2048)

def generate_sql(question, schema):
    prompt = f"""
    You are an expert SQL developer. Given the following database schema:

    {schema}

    Write an SQL query for the following question:

    {question}

    SQL Query:
    """

    output = llm(prompt, max_tokens=512, stop=["\n\n", ";"], echo=False)
    text = output["choices"][0]["text"].strip()

    if not text.endswith(";"):
        text += ";"

    return text
