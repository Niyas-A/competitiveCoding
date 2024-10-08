class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        vector<int> net_gas(size(gas),0);
        for(auto i=0; i<size(gas); i++){
            net_gas[i] = gas[i] - cost[i];
            }
        if(accumulate(net_gas.begin(), net_gas.end(), 0) < 0){
            return -1; 
        }
        auto tank = 0, start = 0;
        for(auto i=0; i<size(net_gas); i++){
            tank += net_gas[i];
            if(tank<0){
                tank = 0;
                start = i+1;
            }
        }
        return start;
    }
};