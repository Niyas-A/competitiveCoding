class RandomizedSet {
    map<int,int> mp;
    vector<int> v;
public:
    RandomizedSet() {

    }
    
    bool insert(int val) {
        if(mp[val] == 0){
            v.push_back(val);
            mp[val]++;
            return true;
        }
        else {
            return false;
        }
    }
    
    bool remove(int val) {
        if(mp[val] == 0){
            return false;
        }
        else {
            mp[val]--;
            auto it = find(v.begin(), v.end(), val);
            v.erase(it);
            return true;
        }
    }
    
    int getRandom() {
        int r = random()%v.size();
        return v[r];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */