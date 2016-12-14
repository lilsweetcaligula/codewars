import itertools
move_zeros = (lambda array:
    list(
      itertools.chain(
        (value for value in array if not (type(value) in (int, float) and value == 0)),
        (value for value in array if type(value) in (int, float) and value == 0)
      )
    )
)