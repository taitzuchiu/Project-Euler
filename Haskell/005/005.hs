notEvenlyDivisibleTo :: Int -> Int -> Bool
notEvenlyDivisibleTo a n = any (\y -> a `mod` y /= 0) ([2..n])

evenlyDivisibleNumbersOneTo :: Int -> Int -> [Int]
evenlyDivisibleNumbersOneTo n x = take n [a | a <- [x..], not (notEvenlyDivisibleTo a x)]

main :: IO ()
main = do
  let answer = 1 `evenlyDivisibleNumbersOneTo` 20
  putStrLn $ "Answer: " ++ show answer
