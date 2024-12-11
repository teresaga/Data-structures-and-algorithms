def reverse(word):
  ## Check
  if type(word) != "string" and len(word) < 2:
    return "String should be larger than 1"
  
  word_array = list(word)
  half_len = len(word_array) // 2 #floor

  for i in range(half_len):
    aux = word_array[i]
    word_array[i] = word_array[len(word_array) - 1 - i]
    word_array[len(word_array) - 1 - i] = aux

  return "".join(word_array)

# O(n)

def reverse2(word):
  word_array = list(word)
  i = 0
  j = len(word_array) - 1
  
  while i < j:
    word_array[i], word_array[j] = word_array[j], word_array[i]
    i += 1
    j -= 1

  return "".join(word_array)

def reverse3(word):
  return "".join(reverse(list(word)))

word = "abcd"
reverse4 = lambda x: "".join(reverse(list(x))) # It is not recommended, def provide better readability

print(reverse4(word))