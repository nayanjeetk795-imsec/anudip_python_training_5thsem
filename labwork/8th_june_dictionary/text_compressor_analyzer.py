# Text Compression Analyzer

text = "AAABBBCCCDDDAAA"

# 1 & 2. Count occurrences and create frequency dictionary
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# 3. Display unique characters
unique_chars = list(freq.keys())

# 4. Find the most frequent character
most_frequent = ""
max_count = 0

for ch, count in freq.items():
    if count > max_count:
        max_count = count
        most_frequent = ch

# 5. Create compressed output
compressed = ""
count = 1

for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        count += 1
    else:
        compressed += text[i] + str(count)
        count = 1

compressed += text[-1] + str(count)

# 6. Calculate compression ratio
original_length = len(text)
compressed_length = len(compressed)
compression_ratio = (compressed_length / original_length) * 100

# Display results
print("Original Text:", text)

print("\nCharacter Frequencies:")
for ch, count in freq.items():
    print(ch, "->", count)

print("\nUnique Characters:", unique_chars)
print("Most Frequent Character:", most_frequent)
print("Compressed Output:", compressed)
print("Original Length:", original_length)
print("Compressed Length:", compressed_length)
print("Compression Ratio:", round(compression_ratio, 2), "%")