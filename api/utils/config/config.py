OPENAI_MODEL_NAME = "gpt-3.5-turbo-0125"
# OPENAI_MODEL_NAME = "gpt-4-turbo"
MAX_TOKENS = 1500
TEMPERATURE = 0.0

CHUNK_SIZE = 400
CHUNK_OVERLAP = 50
INDEX_K = 10

NUM_GEN_LINKS = 10
SCRAPE_TIMEOUT = 5
LINK_SEARCH_PROVIDER = 0 # 0: DuckDuckGo, 1: Serper (Google)
PROHIBITED_LINKS = [
  r"youtube\.com",
  r"wikipedia\.org"
]
