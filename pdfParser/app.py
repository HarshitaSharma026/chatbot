import nest_asyncio
import os
from dotenv import load_dotenv
from llama_parse import LlamaParse

load_dotenv()
nest_asyncio.apply()

doc = LlamaParse(result_type="markdown").load_data("./the20odyssey.pdf")

filename = "odyssey.md"
with open(filename, 'w') as file:
    file.write(doc[0].text)


# for brochure : took 3 mins to parse --got nothing useful
# for academic calender : took ~10 secs to parse  -- accurate parsing