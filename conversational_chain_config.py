import dotenv, os
dotenv.load_dotenv()

# CONFIGURATION VARIABLES:
SELECTOR_KWARGS = dict(
    model_name="gpt-3.5-turbo",
    condenser_llm="gpt-3.5-turbo",
    embeddings_model="text-embedding-ada-002",
    temperature=0.1,
)
VECTOR_STORE_DIR=os.path.join("vectordb", SELECTOR_KWARGS["embeddings_model"])
SOURCE_DOCS_PATH="data/Copy of ctg-studies.csv"
MAX_CHAT_HISTORY_TOKENS=1024
USE_COMPRESSOR_RETREIVER=True
DB_IMPL="duckdb+parquet"
SPLIT_TEXT=False
TEXT_CHUNK_SIZE=None
TEXT_CHUNK_OVERLAP=None
SYSTEM_PROMPT_STR = """Use the following pieces of context to answer the users question. 
If you don't know the answer, just say that you don't know, don't try to make up an answer.
"""
USE_FEW_SHOTS_TEMPLATE = True
VERBOSE=False