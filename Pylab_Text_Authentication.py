from pypdf import PdfReader
# reads data from pdf and will split into small chunks

user_input = { "first_name": "Hari", "last_name": "Arasavalli", "loan_amount": "5 Lakhs",
               "loan_tenure": "12 Months", "annual_income": "10 Lakhs",
               "loan_purpose": "Personal"}



user_details = { "Identity Information" : {
                 "name": "Hari Arasavalli",
                 "aadhar": "4833 6868 0808",
                 "gender": "Male",},
                  "Financial Information":{
                  "Income": "10 Lakhs",
                  "PAN": "xxxxx0797H",
                  "Loans": "Nil"}
                              }


reader = PdfReader('./Aadhar-sriram.pdf')
chunks = []
chunk_length: int = 1000

for page in reader.pages:
    text_page = page.extract_text()
# print(text_page)
    chunks.extend([text_page[i:i+chunk_length].replace('\n','')
                     for i in range(0, len(text_page), chunk_length)])

customer_details = chunks[0].split('')

print("==============================================")

if user_input['first_name'] in customer_details:
    print("User authenticated successfully")
    print(user_details)
else:
   print("Information mismatch, Please contact our support")















