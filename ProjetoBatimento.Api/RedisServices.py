import redis
import uuid
import json

RedisConn = redis.Redis(host='127.0.0.1', port=6379, db=0)

def SendToReddis(args):
    Id = str(uuid.uuid1())
    IdCreated = json.dumps({Id:dict(args)})
    RedisConn.mset({Id:IdCreated})
    return IdCreated

def ReceiveFromReddisById(Id):
    Values = RedisConn.mget(Id)
    Values = json.loads(Values[0])
    return Values