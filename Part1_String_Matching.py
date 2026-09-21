# part 1: string matching

# Muhammad Athallah Yakarazi (24/532752/PA/22532)

import pandas as pd
import re # built-in regex library

file_name = 'spam.csv'
df = pd.read_csv(file_name, encoding='latin-1')

# explanation of the regex pattern in the report
email_pattern = r'[a-zA-Z0-9!#\$%&’*+-/=?^_`{}|~]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
url_pattern = r'(?:https?://|www\.)[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?'
phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
money_pattern = r'[$£€]\s?\d+(?:,\d{3})*(?:\.\d{1,2})?'
repeating_pattern = r'[a-zA-Z]*([a-zA-Z!?])\1{2,}[a-zA-Z]*'

# if no match return empty otherwise return the whole match
def regex_match(pattern, text):
    if not isinstance(text, str):
        return []
    return [match.group() for match in re.finditer(pattern, text)]

df['extracted_emails'] = df['v2'].apply(lambda x: regex_match(email_pattern, x))
df['extracted_urls'] = df['v2'].apply(lambda x: regex_match(url_pattern, x))
df['extracted_phones'] = df['v2'].apply(lambda x: regex_match(phone_pattern, x))
df['extracted_money'] = df['v2'].apply(lambda x: regex_match(money_pattern, x))
df['extracted_repeating'] = df['v2'].apply(lambda x: regex_match(repeating_pattern, x))

# the bool here is used to drop empty results so they won't crowd the display
# this is because bool([]) is false and thus won't be copied by copy()
emails_df = df[df['extracted_emails'].apply(bool)].copy()
urls_df = df[df['extracted_urls'].apply(bool)].copy()
phones_df = df[df['extracted_phones'].apply(bool)].copy()
money_df = df[df['extracted_money'].apply(bool)].copy()
repeating_df = df[df['extracted_repeating'].apply(bool)].copy()

# show 3 examples
print(emails_df[['v2', 'extracted_emails']].head(3))
print(urls_df[['v2', 'extracted_urls']].head(3))
print(phones_df[['v2', 'extracted_phones']].head(3))
print(money_df[['v2', 'extracted_money']].head(3))
print(repeating_df[['v2', 'extracted_repeating']].head(3))





