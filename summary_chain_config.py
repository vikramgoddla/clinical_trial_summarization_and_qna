import dotenv, os
dotenv.load_dotenv()

MODEL_NAME = "gpt-3.5-turbo"
TEMPERATURE = .1
SUMMARY_CHAIN_TYPE = "map_reduce"
SPLIT_TEXT=False
TEXT_CHUNK_SIZE=None
TEXT_CHUNK_OVERLAP=None
SSUMMARY_PROMPT_STR = "Write a concise summary of the following"
VERBOSE=False