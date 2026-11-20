def deleteAllOccurrences(arr: List[int], X: int) -> List[int]:
  write_idx = 0

  for val in arr:
    if val != X:
      arr[write_idx] = val
      write_idx += 1

  for i in range(write_idx, len(arr)):
    arr[i] = 0

  return arr