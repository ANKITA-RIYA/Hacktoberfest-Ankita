

// Rat in a Maze Problem-I 

// Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
// Note: In a path, no cell can be visited more than one time.

// Example 1:

// Input:
// N = 4
// m[][] = {{1, 0, 0, 0},
//          {1, 1, 0, 1}, 
//          {1, 1, 0, 0},
//          {0, 1, 1, 1}}
// Output:
// DDRDRR DRDDRR
// Explanation:
// The rat can reach the destination at 
// (3, 3) from (0, 0) by two paths - DRDDRR 
// and DDRDRR, when printed in sorted order 
// we get DDRDRR DRDDRR.


#include<bits/stdc++.h>
using namespace std;

    void path(vector<vector<int>> &m, int n, int x, int y, vector<string> &ans, string curr_path){      
        if(x == n || y == n || x <0 || y <0){
            return;
        }

        if(m[x][y] == 0){
            return;
        }

        if( x == n-1 && y == n-1){
            ans.push_back(curr_path);
            return;
        }
        
        m[x][y] = 0;
        curr_path += 'D';
        path(m, n, x+1, y,ans, curr_path);
        
        curr_path += 'U';
        path(m, n, x-1, y,ans, curr_path);
              
        curr_path += 'R';
        path(m, n, x, y+1, ans, curr_path);
          
        curr_path += 'L';
        path(m, n, x, y-1, ans, curr_path);
    }
    
    vector<string> findPath(vector<vector<int>> &m, int n) {
        vector<string> ans;
       path(m, n, 0, 0, ans, "");
       
       
       return ans;
    }


int main(){
    
    vector<vector<int>> m = {{1, 0, 0, 0},
         {1, 1, 0, 1}, 
         {1, 1, 0, 0},
         {0, 1, 1, 1}};

     vector<string> ans =  findPath(m,4);

     for(auto i : ans){
         cout<<i;
     }
}