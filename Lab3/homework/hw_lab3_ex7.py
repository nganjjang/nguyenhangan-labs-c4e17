def remove_dollar_sign(s):
    string_with_no_dollars = s.replace('$', '')
    return string_with_no_dollars

string_with_no_dollars = remove_dollar_sign('This is a sentence with a lot of money $$$$$')
print(string_with_no_dollars)
