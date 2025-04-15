from llama_cpp import Llama

LLM_MODEL_PATH = "models\capybarahermes-2.5-mistral-7b.Q4_K_M.gguf"
llm = Llama(model_path=LLM_MODEL_PATH, n_ctx=2048)

def explain_sql(sql_query):
    prompt = f"""
    You are an expert SQL tutor. Explain what the following SQL query does in simple terms:

    {sql_query}

    Explanation:
    """

    output = llm(prompt, max_tokens=256, stop=["\n\n"], echo=False)
    return output["choices"][0]["text"].strip()
