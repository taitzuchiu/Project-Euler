flrt = floor . sqrt . fromIntegral

isComposite :: Int -> Bool
isComposite x = any (\y -> x `mod` y == 0) [2 .. (floor . sqrt . fromIntegral) x]

primesTo :: Int -> [Int]
primesTo n = takeWhile (<= n) [x | x <- [2..], not (isComposite x)]

primeFactors :: Int -> [Int]
primeFactors n = [x | x <- primesTo (flrt n), n `mod` x == 0]

main :: IO ()
main = do
  let answer = last (primeFactors 600851475143)
  putStrLn $ "Answer: " ++ show answer
