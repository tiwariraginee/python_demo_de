# import pandas as pd

# df = pd.read_json('data.json')

# print(df.to_string()) 


import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":110,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":145,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":409,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)
'''record_count = len(df) '''
'''record_count = df.shape[0]'''
unique_records_df = df.drop_duplicates()
total_unique_records = len(unique_records_df)

print(f'Total number of unique records: {total_unique_records}')

'''print(record_count) '''

