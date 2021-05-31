def find_uppercase_recursive(input_str, idx=0):
  if input_str[idx].isupper():
    return input_str[idx]
  if idx == len(input_str) - 1:
    return "No uppercase character found"
  return find_uppercase_recursive(input_str, idx+1)