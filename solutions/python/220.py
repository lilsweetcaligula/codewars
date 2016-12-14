def greet(name):
    return [lambda name: 'Hello, {}!'.format(name), lambda name: 'Hello, my love!'][name == 'Johnny'](name)