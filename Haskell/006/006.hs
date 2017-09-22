sumOfSquaresTo :: Int -> Int
sumOfSquaresTo n = sum [x*x | x <- [1..n]]

squareOfSumTo :: Int -> Int
squareOfSumTo n = square * square
  where square = sum[1..n]

main :: IO ()
main = do
  let answer = abs ((sumOfSquaresTo 100) - (squareOfSumTo 100))
  putStrLn $ "Answer: " ++ show answer
