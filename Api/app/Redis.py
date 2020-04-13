import redis
redisio = redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True)
 
class RedisDataname:
    reset_passpowd_vcode = 'vcode-resetpasspowd-'

def CreateResetPasspowdVcode(vcode, accountid):
    try:
        valuename = RedisDataname.reset_passpowd_vcode + str(vcode)
        value = str(accountid)
        time = (60 * 10)
        print(valuename, value, time)
        redisio.setex(valuename, time, value)
        return True
    except Exception as e:
        print(e)
        return False

def GetResetPasspowdVcode(vcode):
    valuename = RedisDataname.reset_passpowd_vcode + str(vcode)
    return redisio.get(valuename)

def DestructionPasspowdVcode(vcode):
    valuename = RedisDataname.reset_passpowd_vcode + str(vcode)
    redisio.delete(valuename)
    return True