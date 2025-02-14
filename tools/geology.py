from config.core import config
from pinecone import Pinecone
import streamlit as st


pc = Pinecone(st.secrets["PINECONE_API_KEY"])
index = pc.Index('geologia')

def geology_info(query: str) -> str:
  """Queries pinecone database for geological information.
  
  Parameters
  ----------
  query: str
    Query string.

  Returns
  -------
  text: str
    Best text chunk match for query.
  """

  # Embeds query
  x = pc.inference.embed(
      model='multilingual-e5-large',
      inputs=[query],
      parameters={
          'input_type': 'query'
      }
  )

  # Finds best match to embedded query
  results = index.query(
      namespace='ns1',
      vector=x[0].values,
      top_k=3,
      include_values=False,
      include_metadata=True
  )

  return results.matches[0].metadata['text']