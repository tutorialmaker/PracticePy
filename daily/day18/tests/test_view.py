def test_index(client):
    response = client.get('/')
    assert b"Compute Inverse Matrix" in response.data

    input = {'00': '0.0', '01': '0.0',
             '10': '0.0', '11': '0.0'}
    a = input.copy()
    b = input.copy()
    c = input.copy()
    d = input.copy()
    e = input.copy()

    b['00'] = b['11'] = '1.0'
    c['00'] = 'inf'
    c['01'] = 'Inf'
    c['10'] = 'INFINITY'
    c['11'] = 'iNfINity'
    d['00'] = 'nan'
    d['01'] = 'Nan'
    e['00'] = ''

    response = client.post('/', data=a)
    assert b'Result' in response.data
    assert b'Input matrix is a singular matrix.' in response.data

    response = client.post('/', data=b)
    assert b'Result' in response.data
    assert b'Input matrix is a singular matrix.' not in response.data

    response = client.post('/', data=c, follow_redirects=True)
    assert b'please enter the correct value' in response.data

    response = client.post('/', data=d, follow_redirects=True)
    assert b'please enter the correct value' in response.data

    response = client.post('/', data=e, follow_redirects=True)
    assert b'please enter the correct value' in response.data
