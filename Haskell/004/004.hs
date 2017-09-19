checkPalindrome :: String -> Bool
checkPalindrome str
  | length str == 1    = True
  | length str == 2    = (head str == last str)
  | otherwise          = (head str == last str) && checkPalindrome (init (tail str))

main :: IO ()
main = do
  let answer = maximum [x*y | x <- [1..999], y <- [1..999], checkPalindrome (show (x*y))]
  putStrLn $ "Answer: " ++ show answer
