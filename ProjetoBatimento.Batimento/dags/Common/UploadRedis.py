import redis

def SendToReddis(file):
    RedisConn = redis.Redis(host="redis", port=6379, db=0)
    for Fileline in file:
        RedisConn.mset({Fileline[1:15]: Fileline})