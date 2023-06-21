import re
import pandas as pd
with open(r"C:\Users\annjoy.njoroge\Desktop\Python\langchain\Statements.txt", "r") as f1:
    text = f1.read()

codes = re.findall(r"R\w{8}", text)
balances = re.findall(r"New M-PESA balance is (Ksh\d+(?:,\d{3})?(?:\.\d{2})?)\..*?", text)
dates = re.findall(r"on \d{2}/\d{1}/\d{2}", text) 
time = re.findall(r" at (\d{1,2}:\d{2} [AP]M)", text) 
types = re.findall(r"(?i)\b(?:received|sent|paid|airtime|[AP]MWithdraw)\b", text)
sender = re.findall(r"(?i)from\b([A-Z\s]+) ", text)
#with open(r"C:\Users\annjoy.njoroge\Desktop\Python\langchain\Output.txt", "w") as output_file:
   # Create a dictionary with the extracted information

max_length = max(len(codes), len(sender), len(balances), len(dates), len(time), len(types))

# Pad the arrays with None values to make them of the same length
codes += [None] * (max_length - len(codes))
sender += [None] * (max_length - len(sender))
balances += [None] * (max_length - len(balances))
dates += [None] * (max_length - len(dates))
time += [None] * (max_length - len(time))
types += [None] * (max_length - len(types))
data = {
    "Code": codes,
    "Sender": sender,
    "Balance": balances,
    "Date": dates,
    "Time": time,
    "Types": types
}

df = pd.DataFrame(data)
df.to_csv(r"C:\Users\annjoy.njoroge\Desktop\Python\langchain\Output.csv", index=False)      
print(df)