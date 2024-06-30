# Roman to Integer

## Code:

```
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and dic[i] < dic[s+1]:
                sum += dic[s[i + 1]] - dic[s[i]]
                i += 2
            else:
                sum += dic[s[i]]
                i += 1
        return sum
 ```

### Explanation:

#### 1. Dictionary Initialization

`dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}`
A dictionary dic is created to store the integer values corresponding to each Roman numeral character. This allows for quick lookups of Roman numeral values.

#### 2. Variable Initialization

`sum = 0`
`i = 0`
The variable sum is initialized to 0 and will hold the final integer value of the Roman numeral string.
The variable i is initialized to 0 and will be used to iterate through the characters of the string s.

#### 3. While Loop

`while i < len(s)`:
A while loop is used to iterate through the string s as long as i is less than the length of s.

#### 4. Subtractive Notation Handling
```
if i + 1 < len(s) and dic[s[i]] < dic[s[i + 1]]:
    sum += dic[s[i + 1]] - dic[s[i]]
    i += 2
```
This condition checks if there is a subtractive combination.
`i + 1 < len(s)`: Ensures that there is a next character to compare.
`dic[s[i]] < dic[s[i + 1]]`: Checks if the current numeral is less than the next numeral, indicating a subtractive combination (e.g., IV, IX).
If the condition is true, the value of the subtractive combination is calculated by `dic[s[i + 1]] - dic[s[i]]` and added to sum.
The index i is then incremented by 2 to skip the next character since it has already been processed as part of the subtractive combination.

#### 5. Regular Addition

```else:
    sum += dic[s[i]]
    i += 1```

If the subtractive notation condition is not met, the current numeral's value is added to sum.
The index i is incremented by 1 to move to the next character.
#### 6. Return the Result

`return sum`

After processing all the characters in the string s, the final value stored in sum is returned as the integer representation of the Roman numeral string.