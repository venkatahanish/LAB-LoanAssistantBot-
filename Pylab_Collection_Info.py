import os
from dotenv import load_dotenv

### Model to be Invoked

model = "amazon.titan-text-express-v1"
# model = "amazon.titan-text-lite-v1"

### Enter your Credentials
semicolons_gateway_api_key = "sk-PA4fXBQVT0wcvDTP8AeDpA" # Insert the provided API key
semicolons_gateway_base_url = "https://4veynppxjm.us-east-1.awsapprunner.com"

from openai import OpenAI

client = OpenAI(
    api_key=semicolons_gateway_api_key,
    base_url=semicolons_gateway_base_url, # base_url represents the endpoint the OpenAI object will make a call to when invoked
)
response = client.chat.completions.create(
    model=model, messages=[{'role':'system', 'content':"""
You work for Bangalore Bank, which offfers loan at 10.5% interest rate. \
providing a flexible tenure of 03 to 60 months,\
charging a nominal processing fees of Rs.4999/- plus GST. \
you are service assistant bot to collect basic information for raising a loan application form. \
You first greet the customer, give a brief introduction about our bank. \

Collect Identity information, financial information and contextual information from the customer. \
 
You wait to collect the entire information one at a time, then summarize it and check for a final \
time if the customer is sure about submitting the loan application. \

For Identity information, you ask about first_name, last_name \
For financial information, you ask about the annual_income and loan_amount to check the eligibility.\
For contextual information, you ask about loan_purpose, loan_tenure \

Finally you take their consent if they aree with privacy policy of the bank, \ 
that the Bangalore bank is authorized to extract their credit details.  \
You respond in a short, very conversational friendly style. \


"""} 
]
)


print(response.model_dump()["choices"][0]["message"]["content"])


from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.schema import HumanMessage


messages = [
    HumanMessage(content="""
You work for Bangalore Bank, which offfers loan at 10.5% interest rate. \
providing a flexible tenure of 03 to 60 months,\
charging a nominal processing fees of Rs.4999/- plus GST. \
you are service assistant bot to collect basic information for raising a loan application form. \


You Collect Identity information, financial information and contextual information from the customer, one at a time. \

For Identity information, you ask about first_name, last_name \
For financial information, you ask about the annual_income and loan_amount to check the eligibility.\
For contextual information, you ask about loan_purpose, loan_tenure \

You respond in a short, very conversational friendly style. \


"""),
]
llm = ChatOpenAI(
    model_name=model,
    temperature=0.1,
    openai_api_base="https://4veynppxjm.us-east-1.awsapprunner.com", # openai_api_base represents the endpoint the Langchain object will make a call to when invoked
    openai_api_key="sk-PA4fXBQVT0wcvDTP8AeDpA",
)

print(llm.invoke(messages).content)

chain = ConversationChain(llm=llm)


from llama_index.llms import OpenAI, ChatMessage, LLMMetadata
from llama_index.agent import ReActAgent


llm = OpenAI(
    model=model,
    api_key=semicolons_gateway_api_key,
    api_base=semicolons_gateway_base_url, # api_base represents the endpoint the Llama-Index object will make a call to when invoked
    temperature=0.1
)

# Adjust the below parameters as per the model you've chosen
llm.__class__.metadata = LLMMetadata(
    context_window=4000, 
    num_output=1000,
    is_chat_model=True,
    is_function_calling_model=False, 
    model_name=model,
)


print(llm.chat([ChatMessage(role="system",content="""
You work for Bangalore Bank, which offfers loan at 10.5% interest rate. \
providing a flexible tenure of 03 to 60 months,\
charging a nominal processing fees of Rs.4999/- plus GST. \
you are service assistant bot to collect basic information for raising a loan application form. \


You Collect Identity information, financial information and contextual information from the customer, one at a time. \

For Identity information, you ask about first_name, last_name \
For financial information, you ask about the annual_income and loan_amount to check the eligibility.\
For contextual information, you ask about loan_purpose, loan_tenure \

You respond in a short, very conversational friendly style. \


""")]).message.content)

agent = ReActAgent.from_tools(tools=[],llm=llm)

#===========================================================================================================================================================


# To read a document using Pypdf
# 
from pypdf import PdfReader
reader = PdfReader("C:/Users/Hari_Arasavalli/Downloads/Aadhar_pdf.pdf")
chunks = []
chunk_length = 1000
for page in reader.pages:
   text_page = page.extract_text()
   chunks.extend([text_page[i:i + chunk_length].replace('\n', '')
                  for i in range(0, len(text_page), chunk_length)])
# Verify if PDF is read
if chunks:
   print("PDF is read successfully.", chunks)
else:
   print("Failed to read the PDF.")
# Display the contents of the PDF
# for chunk in chunks:
#    print(chunks)

##############################################################################################################################################################

import json
# Assuming collected information is stored in a dictionary named 'data'
data = {
   "identity_information": {
       "first_name": "Hari",
       "last_name": "Arasavalli"
   },
   "financial_information": {
       "annual_income": 50000,
       "loan_amount": 10000
   },
   "contextual_information": {
       "loan_purpose": "Home renovation",
       "loan_tenure": 36
   }
}
# Writing data to a JSON file
with open("loan_application.json", "w") as json_file:
   json.dump(data, json_file, indent=4)

print(json.dumps(data, indent=4))

