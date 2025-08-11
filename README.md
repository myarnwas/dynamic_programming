# Longest Increasing Subsequence (LIS) - Dynamic Programming

## Overview
This project implements the Longest Increasing Subsequence problem using a bottom-up Dynamic Programming approach with **O(n²)** time complexity.

The LIS problem:  
> Given an array, find the length of the longest subsequence of elements in increasing order.

## Algorithm
1. Create a DP array where `dp[i]` stores the length of the LIS ending at index `i`.
2. Initialize all values of `dp` to 1 (each element alone is an LIS of length 1).
3. For each index `i`, check all previous indices `j < i`:
   - If `arr[j] < arr[i]`, update `dp[i] = max(dp[i], dp[j] + 1)`.
4. The result is `max(dp)`.

## Time Complexity
- **O(n²)** due to the nested loops.
