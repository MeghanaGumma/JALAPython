x='global'

def fn():
    x='local'
    print('inside the fn:',x)

fn()
print('outside the fn:',x)
