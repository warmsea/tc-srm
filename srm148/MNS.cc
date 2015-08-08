/*
http://community.topcoder.com/stat?c=problem_statement&pm=1744

Single Round Match 148 Round 1 - Division I, Level Two
Single Round Match 148 Round 1 - Division II, Level Three
*/

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

class MNS {
public:

    int combos(vector<int> numbers) {
        sort(numbers.begin(), numbers.end());
        int result = 0;
        while (true) {
            if (ok(numbers)) {
                ++result;
            }
            if (!next_permutation(numbers.begin(), numbers.end())) {
                break;
            }
        }
        return result;
    }

    bool ok(vector<int> numbers) {
        int sum[] = {
            numbers[0] + numbers[1] + numbers[2],
            numbers[3] + numbers[4] + numbers[5],
            numbers[6] + numbers[7] + numbers[8],
            numbers[0] + numbers[3] + numbers[6],
            numbers[1] + numbers[4] + numbers[7],
            numbers[2] + numbers[5] + numbers[8]
        };
        for (int i = 0; i < 5; ++i) {
            if (sum[i] != sum[i + 1]) {
                return false;
            }
        }
        return true;
    }

};
