/*
http://community.topcoder.com/stat?c=problem_statement&pm=1747

Single Round Match 148 Round 1 - Division I, Level Three
*/

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

class NumberGuessing {
public:
    int range;
    vector<int> guesses;

    int bestGuess(int range, vector<int> guesses, int numLeft) {
        this->range = range;
        this->guesses = guesses;
        unsigned long guessesSize = guesses.size();
        for (int i = 0; i <= numLeft; ++i) {
            this->guesses.push_back(0);
        }
        bestSolution(guessesSize, numLeft);
        return this->guesses[guesses.size()];
    }

    void bestSolution(unsigned long guessesSize, int numLeft) {
        if (numLeft == 0) {
            guesses[guessesSize] = bestLast(guessesSize);
            return;
        }
        vector<int> best;
        int bestChance = 0;
        int chance = 0;
        vector<int>::iterator end = guesses.begin() + guessesSize;
        for (int i = 1; i <= range; ++i) {
            if (find(guesses.begin(), end, i) == end) {
                guesses[guessesSize] = i;
                bestSolution(guessesSize + 1, numLeft - 1);
                chance = getChance(i);
                if (chance > bestChance) {
                    bestChance = chance;
                    best = guesses;
                }
            }
        }
        guesses = best;
    }

    int bestLast(unsigned long guessesSize) {
        if (guessesSize == 0) {
            return 1;
        }
        vector<int> sorted = guesses;
        sort(sorted.begin(), sorted.end() - 1);
        int best = 0;
        int bestChance = 0;
        int chance = 0;
        chance = sorted[0] - 1;
        if (chance > bestChance) {
            bestChance = chance;
            best = sorted[0] - 1;
        }
        for (int i = 0; i < guessesSize - 1; ++i) {
            chance = (sorted[i + 1] - sorted[i]) / 2;
            if (chance > bestChance) {
                bestChance = chance;
                best = sorted[i] + 1;
            }
        }
        chance = range - sorted[guessesSize - 1];
        if (chance > bestChance) {
            bestChance = chance;
            best = sorted[guessesSize - 1] + 1;
        }
        return best;
    }

    int getChance(int target) {
        int left = -target + 1;
        int right = range * 2 - target + 1;
        for (int i = 0; i < guesses.size(); ++i) {
            int g = guesses[i];
            if (g > left and g < target) {
                left = g;
            }
            if (g < right and g > target) {
                right = g;
            }
        }
        return 1 + (target - left - 1) / 2 + (right - target - 1) / 2;
    }
};
