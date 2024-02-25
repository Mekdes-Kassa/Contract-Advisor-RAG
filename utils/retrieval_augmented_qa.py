from operator import itemgetter
from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough

class RetrievalAugmentedQAChain:
    def init(self, base_retriever, model_name="gpt-3.5-turbo", temperature=0):
        self.base_retriever = base_retriever
        self.primary_qa_llm = ChatOpenAI(model_name=model_name, temperature=temperature)

        # Define the retrieval-augmented QA chain
        self.chain = (
            # INVOKE CHAIN WITH: {"question" : "<<SOME USER QUESTION>>"}
            # "question" : populated by getting the value of the "question" key
            # "context"  : populated by getting the value of the "question" key and chaining it into the base_retriever
            {"context": itemgetter("question") | self.base_retriever, "question": itemgetter("question")}
            # "context"  : is assigned to a RunnablePassthrough object (will not be called or considered in the next step)
            #              by getting the value of the "context" key from the previous step
            | RunnablePassthrough.assign(context=itemgetter("context"))
            # "response" : the "context" and "question" values are used to format our prompt object and then piped
            #              into the LLM and stored in a key called "response"
            # "context"  : populated by getting the value of the "context" key from the previous step
            | {"response": prompt | self.primary_qa_llm, "context": itemgetter("context")}
        )

    def invoke(self, input_data):
        """
        Invoke the retrieval-augmented QA chain with input data.

        Args:
        - input_data (dict): Input data containing the user question.

        Returns:
        - result (dict): Output of the retrieval-augmented QA chain.
        """
        return self.chain.invoke(input_data)

# Example usage:
# Assuming base_retriever, model_name, and temperature are defined elsewhere
retrieval_augmented_qa_chain = RetrievalAugmentedQAChain(base_retriever, model_name="gpt-3.5-turbo", temperature=0)
result = retrieval_augmented_qa_chain.invoke({"question": "<<SOME USER QUESTION>>"})