# Dynamic Programming: Coin Change Problem

## Overview
This project demonstrates a dynamic programming solution for the classic Coin Change problem:  
**Given an amount and a set of coin denominations, find the number of ways to make up that amount using the coins.**

Dynamic Programming (DP) is an optimization technique that solves complex problems by breaking them down into simpler subproblems and storing the results of subproblems to avoid redundant computations.

## How the solution works
- Create a DP array `dp` of size `amount + 1`.
- Initialize `dp[0] = 1` since there is exactly one way to make amount 0 — by choosing no coins.
- Iterate over each coin and update the `dp` array for amounts that can be reached using that coin.
- The value `dp[amount]` at the end will be the total number of ways to form the amount.

## Usage
Run the Python script to see the number of ways to make a given amount using the specified coins.

