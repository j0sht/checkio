# Write a function that will receive a positive integer and return:
# "Fizz Buzz" if the number is divisible by 3 and by 5;
# "Fizz" if the number is divisible by 3;
# "Buzz" if the number is divisible by 5;
# The number as a string for other cases.
defmodule FizzBuzz do
  def checkio(n), do: fizz_buzz(n, rem(n, 3), rem(n, 5))
  defp fizz_buzz(_, 0, 0), do: "Fizz Buzz"
  defp fizz_buzz(_, 0, _), do: "Fizz"
  defp fizz_buzz(_, _, 0), do: "Buzz"
  defp fizz_buzz(n, _, _), do: n |> Integer.to_string
end

IO.puts inspect FizzBuzz.checkio(15) == "Fizz Buzz"
IO.puts inspect FizzBuzz.checkio(6) == "Fizz"
IO.puts inspect FizzBuzz.checkio(5) == "Buzz"
IO.puts inspect FizzBuzz.checkio(7) == "7"
