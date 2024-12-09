# Password_Strength_Meter
A Python based password strength Meter which measures the strength of password that evaluates passwords based on length, character diversity, common dictionary words, and repeated characters. It provides actionable feedback to help users create stronger passwords.  
Key Features:

Length Check: Ensures passwords are long enough (at least 8 characters).
Character Variety: Validates the inclusion of lowercase letters, uppercase letters, numbers, and special characters.
Dictionary Word Check: Compares passwords against a provided dictionary to identify weak passwords that include common words.
Repeated Characters Detection: Flags passwords with repeated characters (e.g., "aaa" or "111").
Feedback and Suggestions: Provides tips on improving the password strength based on the analysis.
Usage:

Load a Dictionary: The program loads a dictionary of common words from a JSON file, making it easy to check for weak dictionary-based passwords.
Strength Scoring: The password is scored based on the above criteria and classified as "Weak," "Moderate," or "Strong."
Improvement Tips: Detailed suggestions on how to improve the password, such as adding special characters or avoiding common dictionary words.
How to Use:

Download the given dictionary_word.json file 
Replace the dictionary file path with your path.
Call the check_password_strength(password, dictionary_words) function, where password is the user’s input and dictionary_words is the set of loaded dictionary words.
