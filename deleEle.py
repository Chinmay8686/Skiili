from typing import List


def deleteAtIndex(arr: List[int], P: int) -> List[int]:
  n = len(arr)
  if n == 0 or P < 0 or P >= n:
    return arr

  # Shift elements after index P one position to the left
  for i in range(P, n - 1):
    arr[i] = arr[i + 1]

  # Fill the last position with 0 to keep the size unchanged
  arr[n - 1] = 0

  return arr