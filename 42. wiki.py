import wikipedia

# Choose your search phrase
query = "Philosophy of life"

# Search and fetch summary
try:
    summary = wikipedia.summary(query, sentences=3)  # Get 3-sentence summary
    print(f"\nSummary for '{query}':\n")
    print(summary)
except wikipedia.exceptions.DisambiguationError as e:
    print("Your query is ambiguous. Try one of these instead:")
    print(e.options)
except wikipedia.exceptions.PageError:
    print("The page does not exist. Try a different query.")

query2 = "Python (programming language)"

try:
    summary2 = wikipedia.summary(query2, sentences=5)
    print(summary2)

except wikipedia.excpetions.PageError:
    print("The page does not exist.")
