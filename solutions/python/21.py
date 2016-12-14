def likes(names):
    template_string = '{users} like{plural} this'
    kwargs = {
      'users': '',
      'plural': ''
    }
    if len(names) < 2:
      kwargs['users'] = names[0] if names else 'no one'
      kwargs['plural'] = 's'
    elif len(names) == 2:
      kwargs['users'] = ' and '.join(names)
    elif 2 < len(names) < 4:
      kwargs['users'] = (', '.join(names[:-1])
        + ' and ' + ' and '.join(names[-1:]))
    else:
      kwargs['users'] = (', '.join(names[:2]) 
        + ' and ' + str(len(names) - 2) 
        + ' others')
    return template_string.format(**kwargs)