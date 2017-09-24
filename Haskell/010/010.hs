flrt = floor . sqrt . fromIntegral

isComposite :: Int -> Bool
isComposite x = any (\y -> x `mod` y == 0) (2 : [3, 5 .. (floor . sqrt . fromIntegral) x])

primesTo :: Int -> [Int]
primesTo n = takeWhile (<= n) (2: [x | x <- [3..], not (isComposite x)])

sumPrimesBelow :: Int -> Int
sumPrimesBelow n = sum(primesTo n)

main :: IO ()
main = do
  let answer = sumPrimesBelow 2000000
  putStrLn $ "Answer: " ++ show answer
