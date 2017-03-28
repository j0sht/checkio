defmodule AbsoluteSorting do
  def checkio(ls), do: Enum.sort_by ls, &abs/1
end

IO.puts inspect AbsoluteSorting.checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
IO.puts inspect AbsoluteSorting.checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
IO.puts inspect AbsoluteSorting.checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]
