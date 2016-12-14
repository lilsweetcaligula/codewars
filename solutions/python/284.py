pattern = (lambda count:
  '\n'.join(
      '{start:*<{width}}{end}'.format(
          start = 1, 
          end = end if end > 1 else '', 
          width = end
      ) for end in range(1, count + 1)
  )
)