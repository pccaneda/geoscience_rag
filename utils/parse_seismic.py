import pandas as pd


def parse_dataframe(df: pd.DataFrame) -> str:
    """Converts dataframe into text
    
    Parameters
    ----------
    df: pd.DataFrame
      Pandas dataframe

    Returns
    -------
    running_text: str
      Running text corresponding to input dataframe
    """

    running_text = ""
    for index, row in df.iterrows():
        running_text += f"Evento {index + 1}: Magnitude {row['mag']}, Local {row['place']}, Tempo {row['time']}\n"

    return running_text