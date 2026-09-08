class MinStack {

public:
    MinStack() {
        head = -1;
        capacity = 10;
        container = new int[capacity];
    }
    
    void push(int val) {
        if (container != nullptr) {
            container[++head] = val;
        }
    }
    
    void pop() {
        if (head >= 0) {
            head--;
        }
    }
    
    int top() {
        return container[head];
    }
    
    int getMin() {
        int minNumber = container[head];

        for (int i = 0; i < head; i++) {
            if (container[i] < minNumber) {
                minNumber = container[i];
            }
        }

        return minNumber;
    }

private:
    int capacity;
    int* container;
    int head;
};
