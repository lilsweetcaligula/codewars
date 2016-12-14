def count_arara(n):
    from itertools import chain
    return ' '.join(chain(n // 2 * ['adak'], n % 2 * ['anane']))