from langchain.prompts import ChatPromptTemplate

class ChatPromptTemplateBuilder:
    def init(self, template):
        self.template = template

    def build(self, context, question):
        """
        Build a chat prompt template with the provided context and question.

        Args:
        - context (str): The context for the prompt.
        - question (str): The question for the prompt.

        Returns:
        - prompt (ChatPromptTemplate): The constructed chat prompt template.
        """
        return ChatPromptTemplate.from_template(self.template.format(context=context, question=question))

# Example usage:
    '''
template = """You are a legal expert tasked with acting as the best lawyer and contract analyzer. Your task is to thoroughly understand the provided context and answer questions related to legal matters, contracts, and relevant laws. You must provide accurate responses based solely on the information provided in the context. If the necessary information is not present in the context,':

### CONTEXT
{context}

### QUESTION
Question: {question}
"""

prompt_builder = ChatPromptTemplateBuilder(template)
context = "This is the context of the legal matter."
question = "What are the legal implications of the contract?"
prompt = prompt_builder.build(context, question)
'''