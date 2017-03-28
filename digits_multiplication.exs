# You are given a positive integer.
# Your function should calculate the product of the digits excluding any zeroes.
defmodule DigitsMultiplication do
  def checkio(n) do
    n
    |> Integer.to_string
    |> String.codepoints
    |> Stream.filter(&(&1 != "0"))
    |> Stream.map(&String.to_integer/1)
    |> Enum.into([])
    |> Enum.reduce(&*/2)
  end
end

IO.puts inspect DigitsMultiplication.checkio(123405) == 120
IO.puts inspect DigitsMultiplication.checkio(999) == 729
IO.puts inspect DigitsMultiplication.checkio(1000) == 1
IO.puts inspect DigitsMultiplication.checkio(1111) == 1
