# 0x06. Regular expression

## Concepts
A regular expression, also called `regexp`, is a sequence of characters that define a search pattern. It is mainly used in pattern matching with strings, or string matching.
While powerful, it is also complex.

Different languages use different regexp engines.
Regular expressions are everywhere and software engineers, no matter their positions, will have to use them during their careers. System administrators and DevOps are the ones using them the most because they are very handy for log parsing.

## How to write REGEX
1. start by undeerstanding special characters eg. `,`, `*`, `.`, `+`, `?`, etc.
2. choose a tool or programming language that supports regex, eg Python, Ruby, Perl, grep etc
3. Write your pattern using the special charactersand literal characters
4. Use the appropriate function or method to search for the pattern in a string


## REGEX Quick Reference
| Regex Pattern      | Description                                          |
|--------------------|------------------------------------------------------|
| `[abc]`            | A single character of: a, b, or c                   |
| `[^abc]`           | Any single character except: a, b, or c             |
| `[a-z]`            | Any single character in the range a-z               |
| `[a-zA-Z]`         | Any single character in the range a-z or A-Z         |
| `^`                | Start of line                                        |
| `$`                | End of line                                          |
| `\A`               | Start of string                                      |
| `\z`               | End of string                                        |
| `.`                | Any single character                                 |
| `\s`               | Any whitespace character                             |
| `\S`               | Any non-whitespace character                         |
| `\d`               | Any digit                                            |
| `\D`               | Any non-digit                                        |
| `\w`               | Any word character (letter, number, underscore)      |
| `\W`               | Any non-word character                               |
| `\b`               | Any word boundary                                    |
| `( ... )`          | Capture everything enclosed                          |
| `(a|b)`            | a or b                                               |
| `a?`               | Zero or one of a                                    |
| `a*`               | Zero or more of a                                   |
| `a+`               | One or more of a                                    |
| `a{3}`             | Exactly 3 of a                                       |
| `a{3,}`            | 3 or more of a                                       |
| `a{3,6}`           | Between 3 and 6 of a                                 |
| `options: i`       | Case insensitive                                     |
| `options: m`       | Make dot match newlines                              |
| `options: x`       | Ignore whitespace in regex                           |
| `options: o`       | Perform `#{...}` substitutions only once             |

