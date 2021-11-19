#include <vector>

using std::vector;

class RLEIterator {
   private:
    vector<int>& storage;
    int size = 0;
    int index = 0;
    int offset = 0;

   public:
    RLEIterator(vector<int>& encoding) : storage(encoding) { size = encoding.size(); }

    int next(int n) {
        offset += n;
        while (index < size && offset > storage[index]) {
            offset -= storage[index];
            index += 2;
        }

        if (index < size && offset <= storage[index]) {
            return storage[index + 1];
        }
        return -1;
    }
};

/**
 * Your RLEIterator object will be instantiated and called as such:
 * RLEIterator* obj = new RLEIterator(encoding);
 * int param_1 = obj->next(n);
 */