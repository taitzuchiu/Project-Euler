fibonacciTo :: (Integral a) => a -> [a]
fibonacciTo 1 = [1]
fibonacciTo 2 = [1, 2]
fibonacciTo n = [1, 2] ++ fibonacci 1 2
  where fibonacci x y = [x+y] ++ takeWhile (<= n) (fibonacci y (x+y))

main :: IO ()
main = do
  let answer = sum[ x | x <- fibonacciTo 4000000, even x ]
  putStrLn $ "Answer: " ++ show answer
