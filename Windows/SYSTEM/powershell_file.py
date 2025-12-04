# --- 1. Content of the PowerShell Script (GeneratePrograms.ps1) ---
# This multiline string contains the exact PowerShell code to be executed.
# This ensures run_generator.py is the only file needed.
POWERSHELL_SCRIPT_CONTENT = """
<#
.SYNOPSIS
Generates 54 C source code files (Program1.c through Program54.c)
based on the logic found in the original Linux/Ubuntu shell script.

.DESCRIPTION
This script uses Set-Content to write the content of each C program
directly to the specified .c file, allowing for easy generation
of the solutions on a Windows system using PowerShell.
#>

# Function to write content to a file
function Write-ProgramFile {
    param(
        [Parameter(Mandatory=$true)]
        [string]$FileName,

        [Parameter(Mandatory=$true)]
        [string]$Content
    )
    $Content | Set-Content -Path $FileName -Encoding UTF8 -Force
    Write-Host "Generated: $FileName" -ForegroundColor Green
}

Write-Host "Starting C program file generation..." -ForegroundColor Cyan

# --- Program 1: Swap Three Variables without Temp ---
$P1_Content = @'
#include <stdio.h>

int main()
{
    int a, b, c;
    // Input three integers
    scanf("%d%d%d", &a, &b, &c);
    
    // Swap logic without a temporary variable
    // This method relies on arithmetic properties, which can be tricky 
    // for large numbers due to potential overflow, but works for typical int ranges.
    a = a + b + c;
    c = a - (b + c);
    b = a - (c + b);
    a = a - (b + c);
    
    printf("%d %d %d\\n", a, b, c);
    return 0;
}
'@
Write-ProgramFile -FileName "Program1.c" -Content $P1_Content

# --- Program 2: Count Negatives and Non-Negatives ---
$P2_Content = @'
#include <stdio.h>

int main()
{
    int n;
    int num;
    int negatives = 0;
    int non_negatives = 0;
    int i;
    // Input count of numbers
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        // Input number
        scanf("%d", &num);
        if (num < 0)
        {
            negatives++;
        }
        else
        {
            non_negatives++;
        }
    }
    // Output counts
    printf("%d\\n", negatives);
    printf("%d\\n", non_negatives);
    return 0;
}
'@
Write-ProgramFile -FileName "Program2.c" -Content $P2_Content

# --- Program 3: Average of N Numbers ---
$P3_Content = @'
#include <stdio.h>

int main()
{
    int n;
    int num;
    // Use long long to prevent overflow of sum
    long long sum = 0; 
    int i;
    double average;
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &num);
        sum += num;
    }
    if (n > 0)
    {
        // Cast sum to double for floating point division
        average = (double)sum / n; 
        printf("%lf\\n", average);
    }
    else
    {
        printf("0.000000\\n");
    }
    return 0;
}
'@
Write-ProgramFile -FileName "Program3.c" -Content $P3_Content

# --- Program 4: Sum of Squares of N Numbers ---
$P4_Content = @'
#include <stdio.h>

int main()
{
    int n;
    int num;
    // Use long long for sum of squares to avoid overflow
    long long sum_of_squares = 0; 
    int i;
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &num);
        sum_of_squares += (long long)num * num;
    }
    printf("%lld\\n", sum_of_squares);
    return 0;
}
'@
Write-ProgramFile -FileName "Program4.c" -Content $P4_Content

# --- Program 5: Sum of N Terms of Three Series ---
$P5_Content = @'
#include <stdio.h>

int main()
{
    int n;
    // Sum of arithmetic series (1+2+3+...)
    long long sum_a = 0; 
    // Sum of odd series (1+3+5+...)
    long long sum_b = 0; 
    // Sum of harmonic-like series (1/2 + 1/4 + 1/6 + ...)
    double sum_c = 0.0; 
    int i;
    scanf("%d", &n);
    for (i = 1; i <= n; i++)
    {
        sum_a += i;
        sum_b += (2 * i - 1);
        sum_c += 1.0 / (2.0 * i);
    }
    printf("%lld\\n", sum_a);
    printf("%lld\\n", sum_b);
    printf("%lf\\n", sum_c);
    return 0;
}
'@
Write-ProgramFile -FileName "Program5.c" -Content $P5_Content

# --- Program 6: Alternating Sequence 1 -1 ---
$P6_Content = @'
#include <stdio.h>

int main()
{
    int n;
    int i;
    scanf("%d", &n);
    for (i = 1; i <= n; i++)
    {
        if (i % 2 != 0)
        {
            printf("1");
        }
        else
        {
            printf("-1");
        }
        if (i < n)
        {
            printf(" ");
        }
    }
    printf("\\n");
    return 0;
}
'@
Write-ProgramFile -FileName "Program6.c" -Content $P6_Content

# --- Program 7: Sum of Alternating Odd Series ---
$P7_Content = @'
#include <stdio.h>

int main()
{
    int n;
    long long sum = 0;
    int term;
    int i;
    scanf("%d", &n);
    for (i = 1; i <= n; i++)
    {
        term = 2 * i - 1; // Generates 1, 3, 5, 7, ...
        if (i % 2 != 0)
        {
            sum += term; // Add for odd i (1st, 3rd, 5th term)
        }
        else
        {
            sum -= term; // Subtract for even i (2nd, 4th, 6th term)
        }
    }
    // Series: 1 - 3 + 5 - 7 + 9 - ...
    printf("%lld\\n", sum);
    return 0;
}
'@
Write-ProgramFile -FileName "Program7.c" -Content $P7_Content

# --- Program 8: N Factorial ---
$P8_Content = @'
#include <stdio.h>

// Function to calculate factorial
long long factorial(int n)
{
    long long result = 1;
    int i;
    if (n < 0)
    {
        return 0;
    }
    // Factorial grows very fast, using long long for result
    for (i = 2; i <= n; i++)
    {
        result *= i;
    }
    return result;
}

int main()
{
    int n;
    scanf("%d", &n);
    printf("%lld\\n", factorial(n));
    return 0;
}
'@
Write-ProgramFile -FileName "Program8.c" -Content $P8_Content

# --- Program 9: One Divided by N Factorial ---
$P9_Content = @'
#include <stdio.h>

// Function to calculate 1/N!
double inverse_factorial(int n)
{
    double result = 1.0;
    int i;
    if (n < 0)
    {
        return 0.0;
    }
    for (i = 1; i <= n; i++)
    {
        result /= (double)i;
    }
    return result;
}

int main()
{
    int n;
    scanf("%d", &n);
    printf("%lf\\n", inverse_factorial(n));
    return 0;
}
'@
Write-ProgramFile -FileName "Program9.c" -Content $P9_Content

# --- Program 10: X Power N Div N Factorial ---
$P10_Content = @'
#include <stdio.h>
#include <math.h>

int main()
{
    double x;
    int n;
    double result;
    // Input base (x) and exponent (n)
    scanf("%lf%d", &x, &n); 
    
    if (n < 0)
    {
        printf("0.000000\\n");
        return 0;
    }
    if (n == 0)
    {
        // x^0 / 0! = 1 / 1 = 1
        printf("1.000000\\n");
        return 0;
    }
    
    // Calculate numerator (x^n)
    double numerator = pow(x, n); 
    
    // Calculate denominator (n!) iteratively
    double denominator = 1.0; 
    int i;
    for (i = 1; i <= n; i++)
    {
        denominator *= i;
    }
    
    result = numerator / denominator;
    printf("%lf\\n", result);
    return 0;
}
'@
Write-ProgramFile -FileName "Program10.c" -Content $P10_Content

# --- Program 11: Multiplication by Addition ---
$P11_Content = @'
#include <stdio.h>
#include <stdlib.h> // For abs()

int main()
{
    int a, b;
    int result = 0;
    int i;
    int sign = 1;
    scanf("%d%d", &a, &b);
    
    // Determine the sign of the result
    if ((a < 0 && b > 0) || (a > 0 && b < 0))
    {
        sign = -1;
    }
    
    // Use absolute values for the addition loop
    a = abs(a);
    b = abs(b);
    
    // Multiply a * b by adding 'a' 'b' times
    for (i = 0; i < b; i++)
    {
        result += a;
    }
    
    // Apply the determined sign
    printf("%d\\n", result * sign);
    return 0;
}
'@
Write-ProgramFile -FileName "Program11.c" -Content $P11_Content

# --- Program 12: Check if Character is Alphabetic ---
$P12_Content = @'
#include <stdio.h>
#include <ctype.h> // For isalpha()

// Returns 1 if alphabetic, 0 otherwise (according to C library convention)
int is_alphabetic(char c)
{
    return isalpha(c) != 0;
}

int main()
{
    char c;
    // Note the space before %c to consume any leading whitespace (like newlines)
    if (scanf(" %c", &c) != 1) 
    {
        return 1;
    }
    printf("%d\\n", is_alphabetic(c));
    return 0;
}
'@
Write-ProgramFile -FileName "Program12.c" -Content $P12_Content

# --- Program 13: Sum and Difference of Two Numbers ---
$P13_Content = @'
#include <stdio.h>

// Function to calculate sum and difference using pointers (call by reference)
void calculate_sum_and_diff(int a, int b, int *sum, int *diff)
{
    *sum = a + b;
    *diff = a - b;
}

int main()
{
    int num1, num2;
    int sum_result, diff_result;
    scanf("%d%d", &num1, &num2);
    
    // Pass the addresses of sum_result and diff_result
    calculate_sum_and_diff(num1, num2, &sum_result, &diff_result); 
    
    printf("%d\\n", sum_result);
    printf("%d\\n", diff_result);
    return 0;
}
'@
Write-ProgramFile -FileName "Program13.c" -Content $P13_Content

# --- Program 14: Sum of Individual Digits ---
$P14_Content = @'
#include <stdio.h>
#include <stdlib.h> // For abs()

// Function to calculate the sum of digits
int sum_of_digits(int n)
{
    int sum = 0;
    // Work with the absolute value to handle negative numbers
    n = abs(n); 
    while (n != 0)
    {
        sum += n % 10; // Get the last digit
        n /= 10;       // Remove the last digit
    }
    return sum;
}

int main()
{
    int n;
    scanf("%d", &n);
    printf("%d\\n", sum_of_digits(n));
    return 0;
}
'@
Write-ProgramFile -FileName "Program14.c" -Content $P14_Content

# --- Program 15: Reverse Array Elements ---
$P15_Content = @'
#include <stdio.h>

// Function to reverse the array in-place
void reverse_array(int arr[], int n)
{
    int start = 0;
    int end = n - 1;
    int temp;
    while (start < end)
    {
        // Swap elements at start and end
        temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        
        // Move pointers inward
        start++;
        end--;
    }
}

int main()
{
    int n;
    // Assuming max 100 elements
    int arr[100]; 
    int i;
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    
    reverse_array(arr, n);
    
    // Print the reversed array
    for (i = 0; i < n; i++)
    {
        printf("%d", arr[i]);
        if (i < n - 1)
        {
            printf(" ");
        }
    }
    printf("\\n");
    return 0;
}
'@
Write-ProgramFile -FileName "Program15.c" -Content $P15_Content

# --- Program 16: Count Occurrences of Maximum ---
$P16_Content = @'
#include <stdio.h>
#include <limits.h>

int main()
{
    int n;
    int arr[100];
    int i;
    int max_val = [int]::MinValue; # Use PowerShell notation for INT_MIN
    int count = 0;
    
    scanf("%d", &n);
    
    if (n <= 0)
    {
        printf("0\\n");
        return 0;
    }
    
    # Read array elements
    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    
    # Find the maximum value
    for (i = 0; i < n; i++)
    {
        if (arr[i] > max_val)
        {
            max_val = arr[i];
        }
    }
    
    # Count occurrences of the maximum value
    for (i = 0; i < n; i++)
    {
        if (arr[i] == max_val)
        {
            count++;
        }
    }
    
    printf("%d\\n", count);
    return 0;
}
'@
Write-ProgramFile -FileName "Program16.c" -Content $P16_Content

# --- Program 17: Second Largest Value in Array ---
$P17_Content = @'
#include <stdio.h>
#include <limits.h> // For INT_MIN

int main()
{
    int n;
    int arr[100];
    int i;
    // Initialize max_val and second_max to the smallest possible integer
    int max_val = [int]::MinValue; 
    int second_max = [int]::MinValue;
    
    scanf("%d", &n);
    
    if (n < 2)
    {
        printf("N/A\\n"); // Need at least 2 elements
        return 0;
    }
    
    // Read array elements
    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    
    // Find max and second max in a single pass
    for (i = 0; i < n; i++)
    {
        if (arr[i] > max_val)
        {
            second_max = max_val; // Old max becomes second max
            max_val = arr[i];     // New max
        }
        // Check if the current element is between max and second_max
        else if (arr[i] > second_max && arr[i] != max_val) 
        {
            second_max = arr[i];
        }
    }
    
    // Note: PowerShell uses [int]::MinValue notation for INT_MIN
    if ($second_max -eq [int]::MinValue) 
    {
        // This happens if all numbers are the same (e.g., 5, 5, 5) 
        // or if the implementation of INT_MIN replacement failed.
        printf("N/A\\n"); 
    }
    else
    {
        printf("%d\\n", second_max);
    }
    return 0;
}
'@
Write-ProgramFile -FileName "Program17.c" -Content $P17_Content

# --- Program 18: Find Position of Number X ---
$P18_Content = @'
#include <stdio.h>

int main()
{
    int n;
    int x;
    int arr[100];
    int i;
    // Position starts at -1 (not found)
    int position = -1; 
    
    scanf("%d", &n);
    // Read the array
    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    // Read the number to find
    scanf("%d", &x); 
    
    // Search for x
    for (i = 0; i < n; i++)
    {
        if (arr[i] == x)
        {
            position = i;
            break; // Stop after finding the first occurrence
        }
    }
    
    // Print the 0-based index or -1 if not found
    printf("%d\\n", position); 
    return 0;
}
'@
Write-ProgramFile -FileName "Program18.c" -Content $P18_Content

# --- Program 19: Count Vowels and Consonants ---
$P19_Content = @'
#include <stdio.h>
#include <ctype.h> // For isalpha, tolower
#include <string.h> // For string handling

// Helper function to check for vowels
int is_vowel(char c)
{
    c = tolower(c); // Convert to lower case for comparison
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

int main()
{
    char line[1000];
    int vowels = 0;
    int consonants = 0;
    int i;
    
    // Read a line of input
    if (fgets(line, sizeof(line), stdin) == NULL)
    {
        return 1;
    }
    
    for (i = 0; line[i] != '\0'; i++)
    {
        // Only consider alphabetic characters
        if (isalpha(line[i]))
        {
            if (is_vowel(line[i]))
            {
                vowels++;
            }
            else
            {
                consonants++;
            }
        }
    }
    
    printf("%d\\n", vowels);
    printf("%d\\n", consonants);
    return 0;
}
'@
Write-ProgramFile -FileName "Program19.c" -Content $P19_Content

# --- Program 20: Find String in Line Using Pointers ---
$P20_Content = @'
#include <stdio.h>
#include <string.h>

// Custom implementation of strstr using pointers
char *find_substring(const char *haystack, const char *needle)
{
    const char *h = haystack;
    const char *n = needle;
    
    // Loop through the main string
    while (*h != '\0')
    {
        const char *temp_h = h;
        const char *temp_n = n;
        
        // Check for match starting at current position h
        while (*temp_n != '\0' && *temp_h != '\0' && *temp_h == *temp_n)
        {
            temp_h++;
            temp_n++;
        }
        
        // If the entire needle was matched
        if (*temp_n == '\0')
        {
            return (char *)h; // Return the starting pointer
        }
        
        h++; // Move to the next character in the haystack
    }
    return NULL; // Not found
}

int main()
{
    char line[1000];
    char search_str[100];
    char *result;
    
    // Read two lines (main string and search string)
    if (fgets(line, sizeof(line), stdin) == NULL) return 1;
    if (fgets(search_str, sizeof(search_str), stdin) == NULL) return 1;
    
    // Remove trailing newlines
    line[strcspn(line, "\\n")] = '\\0';
    search_str[strcspn(search_str, "\\n")] = '\\0';
    
    result = find_substring(line, search_str);
    
    if (result != NULL)
    {
        // Calculate the 0-based index position
        printf("Found at position: %ld\\n", result - line); 
    }
    else
    {
        printf("Not found\\n");
    }
    return 0;
}
'@
Write-ProgramFile -FileName "Program20.c" -Content $P20_Content

# --- Program 21: Compare Two Strings Using Pointer ---
$P21_Content = @'
#include <stdio.h>

// Custom implementation of strcmp using pointers
int mystrcmp(const char *s1, const char *s2)
{
    // Compare characters while they are equal and not end of string
    while (*s1 != '\0' && *s2 != '\0' && *s1 == *s2)
    {
        s1++;
        s2++;
    }
    // Return the difference of the characters at the point of mismatch or '\0'
    return *s1 - *s2; 
}

int main()
{
    char str1[100];
    char str2[100];
    int result;
    
    // Read the two strings
    if (fgets(str1, sizeof(str1), stdin) == NULL) return 1;
    if (fgets(str2, sizeof(str2), stdin) == NULL) return 1;
    
    result = mystrcmp(str1, str2);
    
    // Output: 0 if equal, <0 if str1 is less, >0 if str1 is greater
    printf("%d\\n", result); 
    return 0;
}
'@
Write-ProgramFile -FileName "Program21.c" -Content $P21_Content

# --- Program 22: Check String Palindrome Using Pointer ---
$P22_Content = @'
#include <stdio.h>
#include <string.h>

// Function to check for palindrome, ignoring newline characters
int is_palindrome(const char *str)
{
    int len = strlen(str);
    const char *start = str;
    const char *end = str + len - 1;
    
    // Move 'end' pointer back to skip newline/carriage return from fgets
    while (len > 0 && (*end == '\\n' || *end == '\\r'))
    {
        len--;
        end--;
    }
    
    if (len <= 1)
    {
        return 1; // Empty or single-character string is a palindrome
    }
    
    // Compare characters from both ends inwards
    while (start < end)
    {
        if (*start != *end)
        {
            return 0; // Not a palindrome
        }
        start++;
        end--;
    }
    return 1; // Is a palindrome
}

int main()
{
    char str[100];
    if (fgets(str, sizeof(str), stdin) == NULL) return 1;
    
    // Output: 1 for palindrome, 0 otherwise
    printf("%d\\n", is_palindrome(str)); 
    return 0;
}
'@
Write-ProgramFile -FileName "Program22.c" -Content $P22_Content

# --- Program 23: Concatenate Two Strings ---
$P23_Content = @'
#include <stdio.h>
#include <string.h>

int main()
{
    // str1 must be large enough to hold the concatenation
    char str1[200]; 
    char str2[100];
    char *dest = str1;
    char *src = str2;
    
    // Read strings (assuming str1 is read first)
    if (fgets(str1, sizeof(str1) / 2, stdin) == NULL) return 1;
    if (fgets(str2, sizeof(str2), stdin) == NULL) return 1;
    
    // Remove trailing newlines
    str1[strcspn(str1, "\\n")] = '\\0';
    str2[strcspn(str2, "\\n")] = '\\0';
    
    // Move dest pointer to the end of str1 (where '\0' is)
    while (*dest != '\0')
    {
        dest++;
    }
    
    // Copy characters from str2 to the end of str1
    while (*src != '\0')
    {
        *dest = *src;
        dest++;
        src++;
    }
    
    *dest = '\0'; // Null-terminate the new concatenated string
    
    printf("%s\\n", str1);
    return 0;
}
'@
Write-ProgramFile -FileName "Program23.c" -Content $P23_Content

# --- Program 24: Display Pointer Content and Address ---
$P24_Content = @'
#include <stdio.h>

int main()
{
    int arr[] = {10, 20, 30, 40, 50};
    int *ptr_int = arr; // ptr_int points to the first element (10)
    char char_arr[] = "ABCDE";
    char *ptr_char = char_arr; // ptr_char points to the first element ('A')
    
    // Display address and content of the integer pointer
    printf("%p %d\\n", (void *)ptr_int, *ptr_int);
    
    // Increment ptr_int by 1 (moves to the next integer, 20)
    ptr_int++; 
    printf("%p %d\\n", (void *)ptr_int, *ptr_int);
    
    // Display address and content of the character pointer
    printf("%p %c\\n", (void *)ptr_char, *ptr_char);
    
    // Increment ptr_char by 2 (moves two characters forward, to 'C')
    ptr_char = ptr_char + 2; 
    printf("%p %c\\n", (void *)ptr_char, *ptr_char);
    
    return 0;
}
'@
Write-ProgramFile -FileName "Program24.c" -Content $P24_Content

# --- Program 25: Generate Fibonacci Series ---
$P25_Content = @'
#include <stdio.h>

int main()
{
    int n;
    int a = 0; // First term
    int b = 1; // Second term
    int next;
    int i;
    
    scanf("%d", &n);
    
    if (n >= 1)
    {
        printf("%d", a);
    }
    if (n >= 2)
    {
        printf(" %d", b);
    }
    
    // Loop for the remaining terms
    for (i = 3; i <= n; i++)
    {
        next = a + b;
        printf(" %d", next);
        a = b; // Update a to the previous b
        b = next; // Update b to the new next term
    }
    printf("\\n");
    return 0;
}
'@
Write-ProgramFile -FileName "Program25.c" -Content $P25_Content

# --- Program 26: Check if Number is Prime ---
$P26_Content = @'
#include <stdio.h>
#include <math.h>

// Optimized function to check for primality
int is_prime(int n)
{
    int i;
    if (n <= 1)
    {
        return 0; // 0 and 1 are not prime
    }
    if (n <= 3)
    {
        return 1; // 2 and 3 are prime
    }
    // Check divisibility by 2 and 3
    if (n % 2 == 0 || n % 3 == 0)
    {
        return 0;
    }
    
    // Check divisors of the form 6k +/- 1 up to sqrt(n)
    for (i = 5; i * i <= n; i = i + 6)
    {
        if (n % i == 0 || n % (i + 2) == 0)
        {
            return 0;
        }
    }
    return 1; // Is prime
}

int main()
{
    int n;
    scanf("%d", &n);
    // Output 1 for prime, 0 for not prime
    printf("%d\\n", is_prime(n)); 
    return 0;
}
'@
Write-ProgramFile -FileName "Program26.c" -Content $P26_Content

# --- Program 27: Check if Number is Palindrome ---
$P27_Content = @'
#include <stdio.h>

// Function to check if a number is a numerical palindrome
int is_palindrome_number(int n)
{
    int original = n;
    int reversed = 0;
    int remainder;
    
    if (n < 0)
    {
        return 0; // Negative numbers are not considered numerical palindromes
    }
    
    while (n != 0)
    {
        remainder = n % 10;
        // Build the reversed number
        reversed = reversed * 10 + remainder; 
        n /= 10;
    }
    
    return original == reversed;
}

int main()
{
    int n;
    scanf("%d", &n);
    // Output 1 for palindrome, 0 for not palindrome
    printf("%d\\n", is_palindrome_number(n)); 
    return 0;
}
'@
Write-ProgramFile -FileName "Program27.c" -Content $P27_Content

# --- Program 28: Check if Number is Armstrong ---
$P28_Content = @'
#include <stdio.h>
#include <math.h> // For pow() and round()

// Function to check if a number is an Armstrong number
// An n-digit number is an Armstrong number if the sum of 
// its digits raised to the power of n is equal to the number itself.
int is_armstrong(int n)
{
    int original = n;
    int num_digits = 0;
    int temp = n;
    long long sum = 0; // Use long long for sum to avoid overflow
    int remainder;
    
    if (n < 0)
    {
        return 0;
    }
    
    // 1. Count the number of digits
    while (temp != 0)
    {
        temp /= 10;
        num_digits++;
    }
    
    temp = original;
    
    // 2. Calculate the sum of powers of digits
    while (temp != 0)
    {
        remainder = temp % 10;
        // Use round() as pow() returns a double, which can have precision issues
        sum += [long long]::Parse([System.Math]::Round([System.Math]::Pow($remainder, $num_digits))); # PowerShell Math functions
        temp /= 10;
    }
    
    // 3. Compare the original number with the sum
    return original -eq sum; # Use PowerShell comparison operator
}

int main()
{
    int n;
    scanf("%d", &n);
    // Output 1 for Armstrong, 0 otherwise
    printf("%d\\n", is_armstrong(n)); 
    return 0;
}
'@
Write-ProgramFile -FileName "Program28.c" -Content $P28_Content

# --- Program 29: Convert Binary to Decimal ---
$P29_Content = @'
#include <stdio.h>
#include <math.h>

int main()
{
    // Use long long for the binary input as it can be large
    long long binary; 
    int decimal = 0;
    int i = 0; // Power of 2 (i.e., position)
    int remainder;
    
    scanf("%lld", &binary);
    
    while (binary != 0)
    {
        // Get the last digit of the binary number (which is the current bit)
        remainder = binary % 10; 
        binary /= 10;
        
        // If the bit is 1, add 2^i to the decimal sum
        if (remainder == 1) 
        {
            decimal += (int)pow(2, i);
        }
        
        i++;
    }
    
    printf("%d\\n", decimal);
    return 0;
}
'@
Write-ProgramFile -FileName "Program29.c" -Content $P29_Content

# --- Program 30: List Exact Divisors ---
$P30_Content = @'
#include <stdio.h>

int main()
{
    int n;
    int i;
    scanf("%d", &n);
    
    if (n <= 0)
    {
        return 0;
    }
    
    // Iterate from 1 up to the number itself
    for (i = 1; i <= n; i++)
    {
        if (n % i == 0) // If there is no remainder, i is a divisor
        {
            printf("%d\\n", i);
        }
    }
    return 0;
}
'@
Write-ProgramFile -FileName "Program30.c" -Content $P30_Content

# --- Program 31: Complex Number Operations ---
$P31_Content = @'
#include <stdio.h>

// Structure to represent a complex number: real + i*imag
typedef struct
{
    double real;
    double imag;
} Complex;

// Addition: (a + bi) + (c + di) = (a+c) + (b+d)i
Complex add(Complex c1, Complex c2)
{
    Complex result;
    result.real = c1.real + c2.real;
    result.imag = c1.imag + c2.imag;
    return result;
}

// Subtraction: (a + bi) - (c + di) = (a-c) + (b-d)i
Complex subtract(Complex c1, Complex c2)
{
    Complex result;
    result.real = c1.real - c2.real;
    result.imag = c1.imag - c2.imag;
    return result;
}

// Multiplication: (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
Complex multiply(Complex c1, Complex c2)
{
    Complex result;
    result.real = c1.real * c2.real - c1.imag * c2.imag;
    result.imag = c1.real * c2.imag + c1.imag * c2.real;
    return result;
}

// Division: (a + bi) / (c + di) = [(ac + bd) / (c^2 + d^2)] + [(bc - ad) / (c^2 + d^2)]i
Complex divide(Complex c1, Complex c2)
{
    Complex result;
    // Denominator is c^2 + d^2
    double denominator = c2.real * c2.real + c2.imag * c2.imag; 
    
    if (denominator == 0)
    {
        // Handle division by zero
        result.real = 0;
        result.imag = 0;
        return result;
    }
    
    result.real = (c1.real * c2.real + c1.imag * c2.imag) / denominator;
    result.imag = (c1.imag * c2.real - c1.real * c2.imag) / denominator;
    return result;
}

int main()
{
    Complex c1, c2, res;
    
    // Input c1 (real imag)
    scanf("%lf%lf", &c1.real, &c1.imag); 
    // Input c2 (real imag)
    scanf("%lf%lf", &c2.real, &c2.imag); 
    
    // Add
    res = add(c1, c2);
    printf("%lf %lf\\n", res.real, res.imag);
    
    // Subtract
    res = subtract(c1, c2);
    printf("%lf %lf\\n", res.real, res.imag);
    
    // Multiply
    res = multiply(c1, c2);
    printf("%lf %lf\\n", res.real, res.imag);
    
    // Divide
    res = divide(c1, c2);
    printf("%lf %lf\\n", res.real, res.imag);
    
    return 0;
}
'@
Write-ProgramFile -FileName "Program31.c" -Content $P31_Content

# --- Program 32: Student Structure Input and Display ---
$P32_Content = @'
#include <stdio.h>
#include <string.h>

// Structure for Address
typedef struct
{
    int door_no;
    char street[50];
    char place[50];
    int pin;
} Address;

// Structure for Student, including Address
typedef struct
{
    char name[10];
    int roll_no;
    Address address;
} Student;

void display_student(Student s)
{
    printf("%s\\n", s.name);
    printf("%d\\n", s.roll_no);
    printf("%d, %s, %s, %d\\n", s.address.door_no, s.address.street, s.address.place, s.address.pin);
}

int main()
{
    Student students[10]; // Array of 10 students
    int i;
    
    // Input details for 10 students
    for (i = 0; i < 10; i++)
    {
        // Using %9s to prevent buffer overflow (name[10] -> max 9 chars + '\0')
        scanf("%9s", students[i].name); 
        scanf("%d", &students[i].roll_no);
        scanf("%d", &students[i].address.door_no);
        // Using %49s for street and place
        scanf("%49s", students[i].address.street); 
        scanf("%49s", students[i].address.place);
        scanf("%d", &students[i].address.pin);
    }
    
    // Display details for all 10 students
    for (i = 0; i < 10; i++)
    {
        display_student(students[i]);
    }
    return 0;
}
'@
Write-ProgramFile -FileName "Program32.c" -Content $P32_Content

# --- Program 33: Compare Two Files Line by Line ---
$P33_Content = @'
#include <stdio.h>
#include <string.h>

int main()
{
    FILE *fp1, *fp2;
    char filename1[100], filename2[100];
    char line1[256], line2[256];
    int line = 1;
    
    // Input filenames
    scanf("%99s", filename1);
    scanf("%99s", filename2);
    
    fp1 = fopen(filename1, "r");
    fp2 = fopen(filename2, "r");
    
    if (fp1 == NULL || fp2 == NULL)
    {
        fprintf(stderr, "Error opening one or both files.\\n");
        return 1;
    }
    
    // Compare line by line
    while (fgets(line1, sizeof(line1), fp1) != NULL && fgets(line2, sizeof(line2), fp2) != NULL)
    {
        if (strcmp(line1, line2) != 0)
        {
            // Found a mismatch
            printf("%d: %s", line, line1); 
            fclose(fp1);
            fclose(fp2);
            return 0;
        }
        line++;
    }
    
    // Check if one file is longer than the other
    if (fgets(line1, sizeof(line1), fp1) != NULL || fgets(line2, sizeof(line2), fp2) != NULL)
    {
        printf("%d: Files have different lengths\\n", line);
    }
    else
    {
        printf("Files are identical\\n");
    }
    
    fclose(fp1);
    fclose(fp2);
    return 0;
}
'@
Write-ProgramFile -FileName "Program33.c" -Content $P33_Content

# --- Program 34: Append File 2 to File 1 ---
$P34_Content = @'
#include <stdio.h>

int main()
{
    FILE *fp1, *fp2;
    char buffer[256];
    size_t bytes_read;
    
    // Open exam1.dat in append mode ("a")
    fp1 = fopen("exam1.dat", "a"); 
    // Open exam2.dat in read mode ("r")
    fp2 = fopen("exam2.dat", "r"); 
    
    if (fp1 == NULL || fp2 == NULL)
    {
        fprintf(stderr, "Error opening files (ensure exam2.dat exists).\\n");
        if (fp1 != NULL) fclose(fp1);
        if (fp2 != NULL) fclose(fp2);
        return 1;
    }
    
    // Read from fp2 and write to fp1
    while ((bytes_read = fread(buffer, 1, sizeof(buffer), fp2)) > 0)
    {
        fwrite(buffer, 1, bytes_read, fp1);
    }
    
    fclose(fp1);
    fclose(fp2);
    printf("exam2.dat appended to exam1.dat\\n");
    return 0;
}
'@
Write-ProgramFile -FileName "Program34.c" -Content $P34_Content

# --- Program 35: Display File in Reverse Order ---
$P35_Content = @'
#include <stdio.h>
#include <stdlib.h> // For malloc, free

int main()
{
    FILE *fp;
    char filename[100];
    long size;
    char *buffer;
    long i;
    
    // Input filename
    scanf("%99s", filename); 
    fp = fopen(filename, "r");
    
    if (fp == NULL)
    {
        fprintf(stderr, "Error opening file.\\n");
        return 1;
    }
    
    // 1. Get file size: move to end, get position
    fseek(fp, 0, SEEK_END); 
    size = ftell(fp);
    
    // 2. Allocate memory for the file content
    buffer = (char *)malloc(size);
    if (buffer == NULL)
    {
        fprintf(stderr, "Memory allocation failed.\\n");
        fclose(fp);
        return 1;
    }
    
    // 3. Read content: move to start, read all bytes
    fseek(fp, 0, SEEK_SET); 
    if (fread(buffer, 1, size, fp) != size)
    {
        fprintf(stderr, "Error reading file content.\\n");
        free(buffer);
        fclose(fp);
        return 1;
    }
    
    // 4. Print content in reverse order
    for (i = size - 1; i >= 0; i--)
    {
        putchar(buffer[i]);
    }
    
    printf("\\n");
    free(buffer);
    fclose(fp);
    return 0;
}
'@
Write-ProgramFile -FileName "Program35.c" -Content $P35_Content

# --- Program 36: File Manipulations on emp.txt ---
$P36_Content = @'
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Structure for Employee
typedef struct
{
    int id;
    char name[20];
    double salary;
} Employee;

// Helper function to write one employee record to a file
void write_record(FILE *fp, Employee emp)
{
    fprintf(fp, "%d %s %lf\\n", emp.id, emp.name, emp.salary);
}

int main()
{
    FILE *fp;
    Employee emp;
    
    // 1. Open emp.txt in append mode to write
    fp = fopen("emp.txt", "a"); 
    if (fp == NULL)
    {
        fprintf(stderr, "Error opening emp.txt for writing.\\n");
        return 1;
    }
    
    // Write first record
    emp.id = 1;
    strcpy(emp.name, "John");
    emp.salary = 50000.00;
    write_record(fp, emp);
    
    // Write second record
    emp.id = 2;
    strcpy(emp.name, "Jane");
    emp.salary = 60000.50;
    write_record(fp, emp);
    
    fclose(fp);
    
    // 2. Open emp.txt in read mode to display
    fp = fopen("emp.txt", "r"); 
    if (fp == NULL)
    {
        fprintf(stderr, "Error opening emp.txt for reading.\\n");
        return 1;
    }
    
    // Read and print records until EOF
    printf("Records in emp.txt:\\n");
    while (fscanf(fp, "%d %s %lf", &emp.id, emp.name, &emp.salary) == 3)
    {
        printf("ID: %d, Name: %s, Salary: %lf\\n", emp.id, emp.name, emp.salary);
    }
    
    fclose(fp);
    return 0;
}
'@
Write-ProgramFile -FileName "Program36.c" -Content $P36_Content

# --- Program 37: Sort Names in Alphabetical Order ---
$P37_Content = @'
#include <stdio.h>
#include <string.h>
#include <stdlib.h> // For qsort

// Comparison function for qsort (compares two char* pointers)
int compare_names(const void *a, const void *b)
{
    // a and b are pointers to elements of the array being sorted (ptr array),
    // which are char** (pointers to char*). We must dereference twice to get the char*.
    return strcmp(*(const char **)a, *(const char **)b); 
}

int main()
{
    // names: stores the actual strings
    char names[5][30]; 
    // ptr: array of pointers to strings for sorting
    char *ptr[5]; 
    int max_names = 5;
    int n = 0; // Actual number of names read
    int i;
    
    // Read up to 5 names
    for (i = 0; i < max_names; i++)
    {
        if (fgets(names[i], 30, stdin) == NULL)
        {
            break;
        }
        // Remove trailing newline
        names[i][strcspn(names[i], "\\n")] = 0; 
        ptr[i] = names[i];
        n++;
    }
    
    // Sort the array of pointers using qsort
    // qsort(base, num_elements, size_of_element, comparator)
    qsort(ptr, n, sizeof(char *), compare_names); 
    
    // Print the sorted names using the sorted pointers
    for (i = 0; i < n; i++)
    {
        printf("%s\\n", ptr[i]);
    }
    return 0;
}
'@
Write-ProgramFile -FileName "Program37.c" -Content $P37_Content

# --- Program 38: Delete Vowels from Sentence ---
$P38_Content = @'
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Helper function to check for vowels
int is_vowel(char c)
{
    c = tolower(c);
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

int main()
{
    char sentence[81];
    char *read_ptr = sentence; // Pointer to read from
    char *write_ptr = sentence; // Pointer to write to (start of string)
    
    if (fgets(sentence, sizeof(sentence), stdin) == NULL)
    {
        return 1;
    }
    
    // Two-pointer approach: reads from read_ptr and writes to write_ptr
    while (*read_ptr)
    {
        if (!is_vowel(*read_ptr))
        {
            // Copy non-vowels forward
            *write_ptr = *read_ptr; 
            write_ptr++;
        }
        // Always advance the read pointer
        read_ptr++; 
    }
    
    *write_ptr = '\0'; // Null-terminate the modified string
    printf("%s\\n", sentence);
    return 0;
}
'@
Write-ProgramFile -FileName "Program38.c" -Content $P38_Content

# --- Program 39: Delete All Occurrences of The ---
$P39_Content = @'
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Helper function to check if "the" (case-insensitive) is present 
// as a whole word starting at *ptr
int is_match(const char *ptr, const char *word, int len, const char *start_of_sentence)
{
    // Check characters for "the" (case-insensitive)
    if (tolower(*ptr) != 't' || tolower(*(ptr + 1)) != 'h' || tolower(*(ptr + 2)) != 'e')
    {
        return 0;
    }
    
    // Check for word boundary after "the" (space, end of line, or null terminator)
    char after = *(ptr + len);
    if (!(isspace(after) || after == '\0'))
    {
        return 0;
    }
    
    // Check for word boundary before "the" (start of line or space)
    if (ptr == start_of_sentence || isspace(*(ptr - 1)))
    {
        return 1;
    }
    
    return 0;
}

int main()
{
    char sentence[1000];
    const char *word = "the"; // For length check
    int word_len = 3;
    char *read_ptr;
    char *write_ptr;
    
    if (fgets(sentence, sizeof(sentence), stdin) == NULL)
    {
        return 1;
    }
    
    // Remove trailing newline for proper boundary check
    sentence[strcspn(sentence, "\\n")] = '\\0'; 
    
    read_ptr = sentence;
    write_ptr = sentence;
    
    while (*read_ptr)
    {
        if (is_match(read_ptr, word, word_len, sentence))
        {
            // Skip "the" and any following space
            read_ptr += word_len; 
            while (*read_ptr == ' ') {
                read_ptr++;
            }
        }
        else
        {
            // Copy non-matching character
            *write_ptr = *read_ptr; 
            write_ptr++;
            read_ptr++;
        }
    }
    
    *write_ptr = '\0'; // Null-terminate the modified string
    printf("%s\\n", sentence);
    return 0;
}
'@
Write-ProgramFile -FileName "Program39.c" -Content $P39_Content

# --- Program 40: Count Successive Vowels ---
$P40_Content = @'
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Helper function to check for vowels
int is_vowel(char c)
{
    c = tolower(c);
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

int main()
{
    char line[1000];
    char *ptr;
    int count = 0;
    
    if (fgets(line, sizeof(line), stdin) == NULL)
    {
        return 1;
    }
    
    ptr = line;
    
    // Check pairs of characters: ptr and ptr+1
    while (*ptr != '\0' && *(ptr + 1) != '\0')
    {
        // Check if both current and next character are vowels
        if (is_vowel(*ptr) && is_vowel(*(ptr + 1)))
        {
            count++;
        }
        ptr++;
    }
    
    printf("%d\\n", count);
    return 0;
}
'@
Write-ProgramFile -FileName "Program40.c" -Content $P40_Content

# --- Program 41: Implement Built-in String Functions ---
$P41_Content = @'
#include <stdio.h>
#include <stddef.h> // For size_t

// 1. Implementation of strlen
size_t mystrlen(const char *s)
{
    const char *p = s;
    while (*p != '\0')
    {
        p++;
    }
    return p - s; // Distance between start and end
}

// 2. Implementation of strcat
char *mystrcat(char *dest, const char *src)
{
    char *ret = dest;
    // Move dest pointer to the end of the destination string
    while (*dest != '\0')
    {
        dest++;
    }
    // Copy source string to the end of destination
    while ((*dest++ = *src++) != '\0')
        ;
    return ret;
}

// 3. Implementation of strcpy
char *mystrcpy(char *dest, const char *src)
{
    char *ret = dest;
    // Copy until the null terminator is copied
    while ((*dest++ = *src++) != '\0') 
        ;
    return ret;
}

// 4. Implementation of strcmp
int mystrcmp(const char *s1, const char *s2)
{
    while (*s1 != '\0' && *s2 != '\0' && *s1 == *s2)
    {
        s1++;
        s2++;
    }
    return *s1 - *s2;
}

// 5. Implementation of substr (custom for extracting substring)
char *mysubstr(char *dest, const char *src, size_t start_index, size_t length)
{
    size_t i;
    // Copy up to 'length' characters starting from 'start_index'
    for (i = 0; i < length && src[start_index + i] != '\0'; i++)
    {
        dest[i] = src[start_index + i];
    }
    dest[i] = '\0'; // Null-terminate the substring
    return dest;
}

int main()
{
    char s1[100] = "hello";
    char s2[50] = " world";
    char dest[100];
    char sub[20];
    
    printf("mystrlen('hello'): %lu\\n", mystrlen(s1));
    
    // mystrcat
    mystrcat(s1, s2);
    printf("mystrcat: %s\\n", s1); 
    
    // mystrcpy
    mystrcpy(dest, s1);
    printf("mystrcpy: %s\\n", dest);
    
    // mystrcmp
    printf("mystrcmp(s1, dest): %d\\n", mystrcmp(s1, dest)); 
    
    // mysubstr (extract "world" from "hello world")
    mysubstr(sub, dest, 6, 5);
    printf("mysubstr: %s\\n", sub);
    
    return 0;
}
'@
Write-ProgramFile -FileName "Program41.c" -Content $P41_Content

# --- Program 42: Check String Palindrome ---
$P42_Content = @'
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Checks if a string is a palindrome, ignoring case and trailing newlines
int is_palindrome(const char *str)
{
    int len = strlen(str);
    int i = 0; // Start pointer index
    int j = len - 1; // End pointer index
    
    // Ignore trailing newlines/carriage returns
    while (j >= 0 && (str[j] == '\\n' || str[j] == '\\r'))
    {
        j--;
    }
    
    // Compare characters from both ends inwards
    while (i < j)
    {
        // Compare case-insensitively
        if (tolower(str[i]) != tolower(str[j])) 
        {
            return 0; // Not a palindrome
        }
        i++;
        j--;
    }
    return 1; // Is a palindrome
}

int main()
{
    char str[100];
    if (fgets(str, sizeof(str), stdin) == NULL)
    {
        return 1;
    }
    // Output 1 for palindrome, 0 otherwise
    printf("%d\\n", is_palindrome(str)); 
    return 0;
}
'@
Write-ProgramFile -FileName "Program42.c" -Content $P42_Content

# --- Program 43: Display File in Uppercase ---
$P43_Content = @'
#include <stdio.h>
#include <ctype.h> // For toupper

int main()
{
    FILE *fp;
    char filename[100];
    int c;
    
    // Input filename
    scanf("%99s", filename); 
    fp = fopen(filename, "r");
    
    if (fp == NULL)
    {
        fprintf(stderr, "Error opening file.\\n");
        return 1;
    }
    
    // Read character by character until EOF
    while ((c = fgetc(fp)) != EOF)
    {
        // Convert to uppercase and print
        putchar(toupper(c)); 
    }
    
    fclose(fp);
    return 0;
}
'@
Write-ProgramFile -FileName "Program43.c" -Content $P43_Content

# --- Program 44: Count File Components ---
$P44_Content = @'
#include <stdio.h>
#include <ctype.h>

int main()
{
    FILE *fp;
    char filename[100];
    int c;
    // Use long for counters in case of large files
    long chars = 0; 
    long spaces = 0;
    long tabs = 0;
    long newlines = 0;
    
    // Input filename
    scanf("%99s", filename); 
    fp = fopen(filename, "r");
    
    if (fp == NULL)
    {
        fprintf(stderr, "Error opening file.\\n");
        return 1;
    }
    
    // Read character by character
    while ((c = fgetc(fp)) != EOF)
    {
        chars++;
        if (c == ' ')
        {
            spaces++;
        }
        else if (c == '\t')
        {
            tabs++;
        }
        else if (c == '\\n')
        {
            newlines++;
        }
    }
    
    fclose(fp);
    
    printf("Total characters: %ld\\n", chars);
    printf("Spaces: %ld\\n", spaces);
    printf("Tabs: %ld\\n", tabs);
    printf("Newlines: %ld\\n", newlines);
    
    return 0;
}
'@
Write-ProgramFile -FileName "Program44.c" -Content $P44_Content

# --- Program 45: Copy File Contents ---
$P45_Content = @'
#include <stdio.h>

int main()
{
    FILE *src_fp, *dest_fp;
    char src_filename[100], dest_filename[100];
    int c;
    
    // Input source and destination filenames
    scanf("%99s", src_filename); 
    scanf("%99s", dest_filename);
    
    // Open source file for reading ("r")
    src_fp = fopen(src_filename, "r"); 
    if (src_fp == NULL)
    {
        fprintf(stderr, "Error opening source file.\\n");
        return 1;
    }
    
    // Open destination file for writing ("w")
    dest_fp = fopen(dest_filename, "w"); 
    if (dest_fp == NULL)
    {
        fprintf(stderr, "Error opening destination file.\\n");
        fclose(src_fp);
        return 1;
    }
    
    // Read character by character from source and write to destination
    while ((c = fgetc(src_fp)) != EOF)
    {
        fputc(c, dest_fp);
    }
    
    fclose(src_fp);
    fclose(dest_fp);
    
    printf("File copied successfully\\n");
    return 0;
}
'@
Write-ProgramFile -FileName "Program45.c" -Content $P45_Content

# --- Program 46: Write Strings to File ---
$P46_Content = @'
#include <stdio.h>
#include <string.h>

int main()
{
    FILE *fp;
    char filename[100];
    char str[100];
    
    // Input filename to write to
    scanf("%99s", filename); 
    // Open file in write mode ("w"). This will create or overwrite the file.
    fp = fopen(filename, "w"); 
    
    if (fp == NULL)
    {
        fprintf(stderr, "Error opening file for writing.\\n");
        return 1;
    }
    
    printf("Enter strings (type QUIT or quit on a new line to finish):\\n");
    
    // Read strings from standard input
    while (fgets(str, sizeof(str), stdin) != NULL)
    {
        // Check for the termination sequence
        if (strcmp(str, "QUIT\\n") == 0 || strcmp(str, "quit\\n") == 0)
        {
            break;
        }
        // Write the string (including the newline character from fgets) to the file
        fputs(str, fp); 
    }
    
    fclose(fp);
    printf("Strings written to file\\n");
    return 0;
}
'@
Write-ProgramFile -FileName "Program46.c" -Content $P46_Content

# --- Program 47: Read Strings from File ---
$P47_Content = @'
#include <stdio.h>

int main()
{
    FILE *fp;
    char filename[100];
    char str[100];
    
    // Input filename to read from
    scanf("%99s", filename); 
    // Open file in read mode ("r")
    fp = fopen(filename, "r"); 
    
    if (fp == NULL)
    {
        fprintf(stderr, "Error opening file for reading.\\n");
        return 1;
    }
    
    printf("Content of %s:\\n", filename);
    
    // Read strings line by line from the file
    while (fgets(str, sizeof(str), fp) != NULL)
    {
        // Print the string (fgets includes the newline, so no extra \n is needed)
        printf("%s", str); 
    }
    
    fclose(fp);
    return 0;
}
'@
Write-ProgramFile -FileName "Program47.c" -Content $P47_Content

# --- Program 48: Book Structure and Display ---
$P48_Content = @'
#include <stdio.h>
#include <string.h>

// Structure for a Book
typedef struct
{
    char title[100];
    double price;
    int pages;
} Book;

int main()
{
    Book book;
    
    // Read title (uses fgets for strings with spaces)
    printf("Enter book title:\\n");
    if (fgets(book.title, sizeof(book.title), stdin) == NULL)
    {
        return 1;
    }
    // Remove the trailing newline read by fgets
    book.title[strcspn(book.title, "\\n")] = 0; 

    // Read price and pages
    printf("Enter book price and pages:\\n");
    // Note: for simpler input on the canvas, we will assume price and pages 
    // are entered after the title, potentially on new lines.
    scanf("%lf", &book.price);
    scanf("%d", &book.pages);
    
    printf("\\nBook Details:\\n");
    printf("Title: %s\\n", book.title);
    printf("Price: %lf\\n", book.price);
    printf("Pages: %d\\n", book.pages);
    
    return 0;
}
'@
Write-ProgramFile -FileName "Program48.c" -Content $P48_Content

# --- Program 49: Determine Tomorrow's Date ---
$P49_Content = @'
#include <stdio.h>

// Structure for Date
typedef struct
{
    int day;
    int month;
    int year;
} Date;

// Helper to check for leap year
int is_leap(int year)
{
    return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
}

// Helper to get days in a month
int days_in_month(int month, int year)
{
    if (month == 2) // February
    {
        return is_leap(year) ? 29 : 28;
    }
    else if (month == 4 || month == 6 || month == 9 || month == 11) // 30-day months
    {
        return 30;
    }
    else // 31-day months
    {
        return 31;
    }
}

// Main logic to calculate the next day
Date get_tomorrow(Date today)
{
    Date tomorrow = today;
    int max_day = days_in_month(today.month, today.year);
    
    tomorrow.day++;
    
    // Check for month rollover
    if (tomorrow.day > max_day)
    {
        tomorrow.day = 1;
        tomorrow.month++;
        
        // Check for year rollover
        if (tomorrow.month > 12)
        {
            tomorrow.month = 1;
            tomorrow.year++;
        }
    }
    return tomorrow;
}

int main()
{
    Date today, tomorrow;
    // Input day, month, year
    scanf("%d%d%d", &today.day, &today.month, &today.year); 
    
    tomorrow = get_tomorrow(today);
    
    // Output tomorrow's date
    printf("%d %d %d\\n", tomorrow.day, tomorrow.month, tomorrow.year); 
    return 0;
}
'@
Write-ProgramFile -FileName "Program49.c" -Content $P49_Content

# --- Program 50: Display Students List in Ascending Order ---
$P50_Content = @'
#include <stdio.h>
#include <string.h>
#include <stdlib.h> // For qsort

// Structure for Student
typedef struct
{
    char name[50];
    int roll_no;
    int age;
} Student;

// Comparison function for qsort (sorts by name)
int compare_students(const void *a, const void *b)
{
    // Cast generic pointers back to Student* and compare names
    return strcmp(((Student *)a)->name, ((Student *)b)->name); 
}

int main()
{
    int n;
    Student students[100];
    int i;
    
    // Input number of students
    scanf("%d", &n); 
    
    // Input student details
    for (i = 0; i < n; i++)
    {
        scanf("%49s", students[i].name);
        scanf("%d", &students[i].roll_no);
        scanf("%d", &students[i].age);
    }
    
    // Sort the array using qsort
    // The sorting is based on the comparison of student names
    qsort(students, n, sizeof(Student), compare_students); 
    
    // Display the sorted list
    printf("\\nSorted Students (by Name):\\n");
    for (i = 0; i < n; i++)
    {
        printf("%s %d %d\\n", students[i].name, students[i].roll_no, students[i].age);
    }
    return 0;
}
'@
Write-ProgramFile -FileName "Program50.c" -Content $P50_Content

# --- Program 51: Display Student Mark Sheet ---
$P51_Content = @'
#include <stdio.h>

// Structure for Mark Sheet
typedef struct
{
    int roll_no;
    char name[50];
    int marks[3]; // Assuming 3 subjects
    int total;
    double percentage;
} MarkSheet;

// Function to calculate total and percentage
void calculate_marks(MarkSheet *ms)
{
    int i;
    ms->total = 0;
    for (i = 0; i < 3; i++)
    {
        ms->total += ms->marks[i];
    }
    // Calculate percentage (total / number of subjects)
    ms->percentage = (double)ms->total / 3.0; 
}

int main()
{
    MarkSheet ms;
    int i;
    
    // Input details
    scanf("%d", &ms.roll_no);
    scanf("%49s", ms.name);
    for (i = 0; i < 3; i++)
    {
        scanf("%d", &ms.marks[i]);
    }
    
    calculate_marks(&ms);
    
    // Display Mark Sheet
    printf("Mark Sheet\\n");
    printf("Roll No: %d\\n", ms.roll_no);
    printf("Name: %s\\n", ms.name);
    printf("Marks:\\n");
    for (i = 0; i < 3; i++)
    {
        printf("Subject %d: %d\\n", i + 1, ms.marks[i]);
    }
    printf("Total Marks: %d\\n", ms.total);
    printf("Percentage: %lf\\n", ms.percentage);
    
    return 0;
}
'@
Write-ProgramFile -FileName "Program51.c" -Content $P51_Content

# --- Program 52: Display Shopping Bill ---
$P52_Content = @'
#include <stdio.h>

// Structure for a single Item
typedef struct
{
    char item_name[50];
    int quantity;
    double price;
    double total;
} Item;

// Structure for the entire Bill
typedef struct
{
    Item items[10]; // Max 10 items
    int count;
    double grand_total;
} Bill;

// Function to calculate individual item totals and the grand total
void calculate_bill(Bill *bill)
{
    int i;
    bill->grand_total = 0;
    for (i = 0; i < bill->count; i++)
    {
        // Item total = Quantity * Price
        bill->items[i].total = bill->items[i].quantity * bill->items[i].price; 
        bill->grand_total += bill->items[i].total;
    }
}

int main()
{
    Bill bill;
    int i;
    
    // Input number of items
    scanf("%d", &bill.count); 
    
    // Input item details
    for (i = 0; i < bill.count; i++)
    {
        scanf("%49s", bill.items[i].item_name);
        scanf("%d", &bill.items[i].quantity);
        scanf("%lf", &bill.items[i].price);
    }
    
    calculate_bill(&bill);
    
    // Display Shopping Bill
    printf("Shopping Bill\\n");
    printf("Item | Quantity | Price/Unit | Total\\n");
    printf("-----|----------|------------|-------\\n");
    for (i = 0; i < bill.count; i++)
    {
        printf("%s | %d | %lf | %lf\\n", 
               bill.items[i].item_name, 
               bill.items[i].quantity, 
               bill.items[i].price, 
               bill.items[i].total);
    }
    printf("--------------------------------\\n");
    printf("Grand Total: %lf\\n", bill.grand_total);
    
    return 0;
}
'@
Write-ProgramFile -FileName "Program52.c" -Content $P52_Content

# --- Program 53: Shift Unsigned Integer ---
$P53_Content = @'
#include <stdio.h>

// Function to count the number of set bits (ones)
int count_ones(unsigned int n)
{
    int count = 0;
    // Loop until n becomes 0
    while (n > 0) 
    {
        // Check the least significant bit (LSB)
        if (n & 1) 
        {
            count++;
        }
        // Right shift n by 1 (discards LSB)
        n >>= 1; 
    }
    return count;
}

// Function to perform a bitwise shift
unsigned int shift_integer(unsigned int n, int count)
{
    if (count > 0)
    {
        // Positive count means left shift (n * 2^count)
        return n << count; 
    }
    else if (count < 0)
    {
        // Negative count means right shift (n / 2^|count|)
        return n >> -count; 
    }
    else
    {
        return n;
    }
}

int main()
{
    unsigned int n;
    int ones_count;
    unsigned int result;
    
    // Input unsigned integer
    scanf("%u", &n); 
    
    ones_count = count_ones(n);
    printf("Number of set bits: %d\\n", ones_count);
    
    // Left shift by the number of ones
    result = shift_integer(n, ones_count); 
    printf("Left Shift by %d: %u\\n", ones_count, result);
    
    // Right shift by the number of ones
    result = shift_integer(n, -ones_count); 
    printf("Right Shift by %d: %u\\n", ones_count, result);
    
    return 0;
}
'@
Write-ProgramFile -FileName "Program53.c" -Content $P53_Content

# --- Program 54: Copy File Using Command Line Args ---
$P54_Content = @'
#include <stdio.h>
#include <stdlib.h>

// This program takes two command-line arguments: source_file and destination_file
int main(int argc, char *argv[])
{
    FILE *src_fp, *dest_fp;
    int c;
    
    // Check if exactly two arguments (excluding program name) were provided
    if (argc != 3) 
    {
        fprintf(stderr, "Usage: %s <source_file> <destination_file>\\n", argv[0]);
        return 1;
    }
    
    // Open source file (argv[1]) for reading
    src_fp = fopen(argv[1], "r"); 
    if (src_fp == NULL)
    {
        fprintf(stderr, "Error opening source file: %s\\n", argv[1]);
        return 1;
    }
    
    // Open destination file (argv[2]) for writing
    dest_fp = fopen(argv[2], "w"); 
    if (dest_fp == NULL)
    {
        fprintf(stderr, "Error opening destination file: %s\\n", argv[2]);
        fclose(src_fp);
        return 1;
    }
    
    // Copy content character by character
    while ((c = fgetc(src_fp)) != EOF)
    {
        fputc(c, dest_fp);
    }
    
    fclose(src_fp);
    fclose(dest_fp);
    
    printf("File '%s' successfully copied to '%s'.\\n", argv[1], argv[2]);
    
    return 0;
}
'@
Write-ProgramFile -FileName "Program54.c" -Content $P54_Content

Write-Host "`nAll 54 C files (Program1.c through Program54.c) have been successfully generated." -ForegroundColor Yellow
"""

PS_SCRIPT_NAME = "GAP.ps1"