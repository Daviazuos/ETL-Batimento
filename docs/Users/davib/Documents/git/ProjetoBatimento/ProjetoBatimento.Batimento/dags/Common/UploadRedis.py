import redis

def SendToReddis(file):
    RedisConn = redis.Redis(host='127.0.0.1', port=6379, db=0)
    for Fileline in file:
        RedisConn.mset({Fileline[1:15]: Fileline})