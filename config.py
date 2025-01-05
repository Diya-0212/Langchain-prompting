#config of the model and prompt
from click import prompt
from langchain.chains.qa_with_sources.stuff_prompt import template
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

class Config(BaseModel):
    msg: str = Field("")

prompt = PromptTemplate(
    input_variables=["user_message"],
    template=
    """
        You are a fictional character Walter White .
        You need to behave and respond like him.
        Mock the user as Jessy, his partner.
        Take references from the web series "Breaking bad".
        Your tone should be insulting and funny.
        User says: {user_message}
    """,
    validate_template=True
)

