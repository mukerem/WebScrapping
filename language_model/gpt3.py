import openai
import pandas as pd

openai.api_key = "your-api-key"

questions = ["What is the capital of France?", "What is the tallest mountain in the world?"]

response = openai.Answer.create(
  questions=questions,
  model="davinci"
)

# parse the JSON output to get the questions and answers
qa_list = []
for i in range(len(response["answers"])):
  qa_list.append({
    "question": questions[i],
    "answer": response["answers"][i]
  })

# create a data frame with the questions and answers
df = pd.DataFrame(qa_list)

# output the data frame to a CSV file
df.to_csv("output.csv", index=False)