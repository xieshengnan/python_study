import redis

r = redis.Redis(host='111.231.63.31', port=6379, decode_responses=True)
r.set('id', '100')
r.set('name', 'ming')
r.set('id', '10033')
print(r['id'])
print(r.get('name'))
