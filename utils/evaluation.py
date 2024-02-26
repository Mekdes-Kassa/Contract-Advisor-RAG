from typing import List

from datasets import Dataset


from ragas.metrics import (
    answer_relevancy,
    faithfulness,
    context_recall,
    context_precision,
    context_relevancy,
    answer_correctness,
    answer_similarity
)

class RagaEvaluator:
    def __init__(self):
        self= [
            context_precision,
            faithfulness,
            answer_relevancy,
            context_recall,
            context_relevancy,
            answer_correctness,
            answer_similarity
        ]


    def evaluate(self, ragas_dataset: Dataset) -> dict:
        result = evaluate(

            ragas_dataset,

            metrics=self.metrics

        )

        return result