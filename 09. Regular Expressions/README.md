# Regular Expressions in Python

Regular expressions (regex) are a powerful tool for searching, matching, and manipulating text based on patterns. Python provides built-in support for regular expressions through the `re` module, allowing you to perform complex string operations efficiently.

Regular expressions are a versatile tool for text processing and manipulation in Python. By mastering regular expressions, you can perform sophisticated string operations efficiently, making your code more expressive and powerful.

### Basic Regular Expression Operations

- **Pattern Matching:** Use the `re.match()` function to search for a pattern at the beginning of a string.

  ```python
  import re

  pattern = r'hello'
  text = 'hello world'
  match = re.match(pattern, text)
  ```

- **Pattern Search:** Use the `re.search()` function to search for a pattern anywhere in a string.

  ```python
  pattern = r'world'
  text = 'hello world'
  match = re.search(pattern, text)
  ```

- **Pattern Compilation:** Compile a regular expression pattern using `re.compile()` for efficiency when using the same pattern multiple times.

  ```python
  pattern = re.compile(r'hello')
  match = pattern.match(text)
  ```

### Matching and Grouping

- **Grouping:** Use parentheses `()` to group parts of a pattern together and extract matched substrings.

  ```python
  pattern = r'(hello) (world)'
  match = re.match(pattern, text)
  group1 = match.group(1)
  group2 = match.group(2)
  ```

### Special Characters and Quantifiers

- **Special Characters:** Regular expressions support special characters such as `.` (any character), `^` (start of string), `$` (end of string), etc.

  ```python
  pattern = r'^hello.*world$'
  ```

- **Quantifiers:** Use quantifiers such as `*` (zero or more occurrences), `+` (one or more occurrences), `?` (zero or one occurrence), etc.

  ```python
  pattern = r'\d+'  # Matches one or more digits
  ```

### Character Classes and Escaping

- **Character Classes:** Use square brackets `[]` to specify a set of characters to match.

  ```python
  pattern = r'[aeiou]'  # Matches any vowel
  ```

- **Escaping:** Use a backslash `\` to escape special characters in a pattern.

  ```python
  pattern = r'\$'  # Matches a literal dollar sign
  ```

### Substitution and Replacement

- **Substitution:** Use the `re.sub()` function to replace occurrences of a pattern in a string with a specified replacement.

  ```python
  text = 'hello world'
  new_text = re.sub(r'world', 'Python', text)
  ```

### Advanced Operations and Flags

- **Flags:** Use flags such as `re.IGNORECASE`, `re.MULTILINE`, etc., to modify the behavior of regular expression operations.

  ```python
  pattern = re.compile(r'hello', re.IGNORECASE)
  ```

- **Advanced Operations:** Regular expressions support advanced operations such as lookahead assertions, capturing groups, non-capturing groups, etc.

---