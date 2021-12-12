#include <vector>

using std::vector;

class NestedInteger {
   public:
    // Constructor initializes an empty nested list.
    NestedInteger();

    // Constructor initializes a single integer.
    NestedInteger(int value);

    // Return true if this NestedInteger holds a single integer, rather than a nested list.
    bool isInteger() const;

    // Return the single integer that this NestedInteger holds, if it holds a single integer
    // The result is undefined if this NestedInteger holds a nested list
    int getInteger() const;

    // Set this NestedInteger to hold a single integer.
    void setInteger(int value);

    // Set this NestedInteger to hold a nested list and adds a nested integer to it.
    void add(const NestedInteger& ni);

    // Return the nested list that this NestedInteger holds, if it holds a nested list
    // The result is undefined if this NestedInteger holds a single integer
    const vector<NestedInteger>& getList() const;
};

class Solution {
   private:
    int sum, sumdep, maxdep;

   public:
    void traverse(const vector<NestedInteger>& l, int dep) {
        if (dep > maxdep) {
            maxdep = dep;
        }

        for (auto& e : l) {
            if (e.isInteger()) {
                int v = e.getInteger();
                sum += v;
                sumdep += dep * v;
            } else {
                traverse(e.getList(), dep + 1);
            }
        }
    }

    int depthSumInverse(vector<NestedInteger>& nestedList) {
        sum = 0;
        sumdep = 0;
        maxdep = 0;
        traverse(nestedList, 0);
        return (maxdep + 1) * sum - sumdep;
    }
};
