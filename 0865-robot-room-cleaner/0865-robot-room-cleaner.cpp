/**
 * // This is the robot's control interface.
 * // You should not implement it, or speculate about its implementation
 * class Robot {
 *   public:
 *     // Returns true if the cell in front is open and robot moves into the cell.
 *     // Returns false if the cell in front is blocked and robot stays in the current cell.
 *     bool move();
 *
 *     // Robot will stay in the same cell after calling turnLeft/turnRight.
 *     // Each turn will be 90 degrees.
 *     void turnLeft();
 *     void turnRight();
 *
 *     // Clean the current cell.
 *     void clean();
 * };
 */

class Solution {
    set<pair<int, int>> seen;
    vector<pair<int, int>> directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

public:
    void goBack(Robot& robot) {
        robot.turnRight();
        robot.turnRight();
        robot.move();
        robot.turnRight();
        robot.turnRight();
    }

    void backtrack(int row, int col, int d, Robot& robot) {
        robot.clean();
        seen.insert(make_pair(row, col));

        for (int i=0; i<4; i++) {
            pair<int, int> direction = directions[d];
            int nx = row + direction.first;
            int ny = col + direction.second;

            if (!seen.count(make_pair(nx, ny)) && robot.move()) {
                backtrack(nx, ny, d, robot);
                goBack(robot);
            }
            d = (d+1)%4;
            robot.turnRight();
        }
    }


    void cleanRoom(Robot& robot) {
        backtrack(0, 0, 0, robot);
    }
};