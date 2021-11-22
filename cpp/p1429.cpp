#include <queue>
#include <unordered_set>
#include <vector>

using std::queue;
using std::unordered_set;
using std::vector;

class FirstUnique {
   private:
    queue<int> que;
    unordered_set<int> good;
    unordered_set<int> bad;

    void clean() {}

   public:
    FirstUnique(vector<int>& nums) {
        for (const auto& e : nums) {
            if (good.count(e)) {
                good.erase(e);
                bad.insert(e);
            } else if (!bad.count(e)) {
                que.push(e);
                good.insert(e);
            }
        }
    }

    int showFirstUnique() {
        while (!que.empty() && bad.count(que.front())) {
            que.pop();
        }
        if (que.empty()) {
            return -1;
        }
        return que.front();
    }

    void add(int value) {
        if (bad.count(value)) {
            return;
        }
        if (good.count(value)) {
            good.erase(value);
            bad.insert(value);
        } else {
            que.push(value);
            good.insert(value);
        }
    }
};