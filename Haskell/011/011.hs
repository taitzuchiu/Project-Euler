import System.IO

-- Takes a list of integers written as strings, and returns a list of integers.
strToIntList :: [String] -> [Int]
strToIntList [] = []
strToIntList [str] = [read str]
strToIntList (str:strs) = read str : strToIntList strs

-- Takes rows of grid and returns list of integer lists
getGridRows :: [String] -> [[Int]]
getGridRows [str] = [strToIntList (words str)]
getGridRows (str:strs) = (strToIntList (words str)) : getGridRows strs

-- Returns a list of products formed by 'n' adjacent ints in list.
adjProducts :: Int -> [Int] -> [Int]
adjProducts n (x:xs)
  | n > length (x:xs) = []
  | otherwise         = (product (take n (x:xs))) : adjProducts n xs

-- Takes grid and returns the columns as rows.
getVerticalGrid :: [[Int]] -> [[Int]]
getVerticalGrid intLists
  = [[ (intLists!!x)!!i | x <- [0..((length intLists)-1)]] |
    i <- [0..((length (intLists!!0))-1)]]

main = do
  contents <- readFile "grid.txt"
  rows = getGridRows (lines content)
  putStrLn $ "help"
