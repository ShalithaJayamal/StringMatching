# StringMatching

String Matching with Wildcards 
 
 
In this question string matching has to be done with wildcards and naive method is used. 
 match ​function is used to match 2 strings and it is in this function the wildcards are implemented. 
 
Searching proceeds by taking n number (number of characters in the pattern) of characters in every step and the starting index is stored in a list which will be returned at the end. 
 
The sample cases are included at the end of the program as general cases for all possibilities like looking for pattern in an empty string, looking for the empty pattern in a non-empty string etc. 
 
The reason for choosing brute force method for this is that there are cases where Knuth-Morris-Pratt algorithm doesn’t work as expected and finding unique hash values for a string with wildcards that matches with a similar string without wildcards is a bit tricky.   
DNA Substring Search with a Modified Version of Rabin-Karp Algorithm 
 
 
 
In this question a DNA pattern has to be matched against a DNA database with multiple records and only the first encounter is needed to be reported. 
 
How this problem is different from general pattern matching cases is this has a much smaller alphabet. A,C,T, and G are only four characters and therefore we have implemented a hash function that makes use of the fundamental theorem of arithmetic. 
 
Fundamental theorem of arithmetic says that every number has a unique prime factorization. So if we assigned prime numbers to every character in the alphabet, we can generate a number as the hash value for any given pattern. 
 
In this algorithm we have assigned prime numbers in the order shown below. A => 2 C => 3 T => 5 G => 7 
 
To understand how the hash function works let’s take CAT as an example. Hash value of CAT is derived like (prime_number_of_C)​×(prime_number_of_A)​2​×(prime_number_of_T)​3 ​= 3×2​2​×7​3​ = ​2401 
 
Note that CAT and only CAT can generate this hash value (2401). No other pattern of letters would ever produce the same number. Therefore comparison can be done without worrying about spurious hits. 
 
The other important point is how the hash value advances when considering next 3 letters. Let’s take another example. Consider GTATCATGGC is the text and we are looking for CAT in this. 
 
This algorithm first takes GTA and generates its hash value like in the previous example. But when it advances into the next step the text will now be TAT. G has dropped and T is added to the end of the text.  
 
Now if we go onto generating the hash value for TAT from the beginning this algorithm would become an O(mn) algorithm which is not very efficient. To avoid this, we generate another hash value, which has the name subStringHash_. ​Let’s call this shadow hash for the sake of understanding. 
 
How this shadow hash value is calculated is very similar to the normal hash value. But we avoid taking powers. 
 
If we denote the corresponding prime number of G as g, T as t and so on, CAT will have the hash value  and shadow hash value  
 
How this new hash is used is shown in the example below. 
 
GTATCATGGC is the DNA sequence and we are looking for CAT in this. The algorithm will first consider GTA. GTA has the hash value  And the shadow hash value would be just  When we go to the next step, the sub string becomes TAT which will have the hash value  
How we derive this value from is as below. 
 
Note that the numerator is the hash value of CAT and the denominator is the shadow hash value of the same substring.  And as the final step all you have to do is multiply the value given by this fraction by  
In programming terms would give us the hash value in the next step. ​len(pattern)​ would be 3 in this case because we are considering 3 letters in every step. This method is of O(1) and therefore put the whole algorithm in O(m+n) class. 
 
So we have used the essence of Rabin-Karp algorithm with a different hash function instead of the rolling hash used in the original Rabin-Karp algorithm. 
 
An advantage of this hash function over the original rolling hash function is this will not have spurious hits. But the disadvantage is that the computer will be dealing with large numbers if the pattern we are looking for is of significant length
