#can read youtube videos

import os
import sys
import constants

os.environ["OPENAI_API_KEY"] = constants.APIKEY


#from llama_index import SimpleDirectoryReader
#documents = SimpleDirectoryReader('./data').load_data()

from llama_index import download_loader
YoutubeTranscriptReader = download_loader("YoutubeTranscriptReader")

loader = YoutubeTranscriptReader()
documents = loader.load_data(ytlinks=['https://www.youtube.com/watch?v=QWBBEdaOGAg'])



from llama_index import VectorStoreIndex
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()


response = query_engine.query("where should mobile sprinklers be deployed")
print(response)




