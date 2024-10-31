# 100 Prisoners Problem Simulation

The **100 Prisoners Problem** is a classic puzzle in probability theory and combinatorics. In this scenario, 100 prisoners are each assigned a unique number from 1 to 100 and must find their own number among 100 drawers to survive. Each prisoner is allowed to open only 50 drawers and cannot communicate with others. Despite the bleak odds, a known strategy remarkably increases their chances of survival.

## Background

The problem was first proposed by Anna Gál and Peter Bro Miltersen in 2003. The rules are as follows:
- **Each prisoner** may open only **50 drawers**.
- **No communication** is allowed between prisoners.

If each prisoner selects drawers randomly, the probability of all prisoners finding their numbers is astronomically low: approximately \(0.0000000000000000000000000000008\).

## Known Strategy

To improve their odds, prisoners can follow a cycle-based strategy:
1. **Open the drawer** labeled with their own number.
2. If they **find their number**, they succeed.
3. If not, they **open the drawer with the number found inside the current drawer**.
4. Repeat steps 2-3, up to 50 times.

This strategy works by exploiting the **cycle structure** of permutations: each prisoner is guaranteed to follow a path that cycles back to their number, unless the cycle length exceeds 50.

## About This Project

This program simulates the 100 Prisoners Problem using the described strategy, allowing users to see how it drastically improves the probability of all prisoners surviving. Through simulation, users can visualize how the cycle-based approach impacts success rates and understand the underlying math of the strategy.