def insertZeroAfterEveryElement(arr: List[int]) -> List[int]:
  n = len(arr)
  if n == 0:
    return arr

  read = (n - 1) // 2
  write = n - 1

  while write >= 0:
    if write == n - 1 and n % 2 == 0:
      arr[write] = 0
      write -= 1
      continue

    arr[write] = arr[read]
    write -= 1
    if write >= 0:
      arr[write] = 0
      write -= 1
    read -= 1  # <-- Move read pointer left

  return arr