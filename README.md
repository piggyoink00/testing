# Fast Modular Exponentiation Algorithm



## About The Project


<img src="https://render.githubusercontent.com/render/math?math=r = m^k mod(n)">

Modular exponentiation, shown in the formula above, is commonly used in the encryption and decryption process in the RSA Algorithm. Since a large exponent would cause the computation to be slow, we could make use of the following formula in a recursive function to improve the efficiency of the algorithm:

<img src="https://render.githubusercontent.com/render/math?math=m^k = m^\frac{k}{2}*m^\frac{k}{2}">

When the exponent k is even, we would just need to calculate <img src="https://render.githubusercontent.com/render/math?math=m^\frac{k}{2}"> once. When the exponent k is odd, deduct 1 from k to make it even. The recursive function has been designed to repeat until the function reaches the base cases of `k = 0`.



## Time Complexity

Whenever the exponent is odd, the next call of the recursive function would be an even exponent due to the step to deduct 1 from an odd exponent. As such, there would be an even exponent value for at least one out of every two recursions. When the exponent value is even, the exponent will be halved by this algorithm. So for a given exponent to reach a value of 1, it would take at most 2*(<img src="https://render.githubusercontent.com/render/math?math=log_2 k">l) steps. Thus, the time complexity of this algorithm would be O(log(k)).


