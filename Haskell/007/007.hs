flrt = floor . sqrt . fromIntegral

isComposite :: Int -> Bool
isComposite x = any (\y -> x `mod` y == 0) (2 : [3, 5 .. (floor . sqrt . fromIntegral) x])

nPrimes :: Int -> [Int]
nPrimes n = take n (2: [x | x <- [3..], not (isComposite x)])

main :: IO ()
main = do
  let answer = last (nPrimes 10001)
  putStrLn $ "Answer: " ++ show answer
