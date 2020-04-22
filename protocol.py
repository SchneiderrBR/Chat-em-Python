class Ptc:

    @staticmethod
    def disconnect(message: str) -> bytes:
        return ('{"op": "DISCONNECT", "message": "' + message + '"}').encode()

    @staticmethod
    def error(message: str) -> bytes:
        return ('{"op": "ERROR", "message": "' + message + '"}').encode()

    @staticmethod
    def login(username: str, hash: str = None) -> bytes:
        if hash != None:
            return ('{"op": "LOGIN", "name": "' + username + '", "hash": "' + hash + '"}').encode()
        else:
            return ('{"op": "LOGIN", "name": "' + username + '"}').encode()

    @staticmethod
    def message(target: str, mesage: str, username: str = None, hash: str = None) -> bytes:
        if hash != None:
            return (
                    '{"op": "MESSAGE", "name": "' + username + '", "target": "' + target + '", "message": "' + mesage + '", hash: "' + hash + '"}').encode()
        elif username != None:
            return (
                    '{"op": "MESSAGE", "name": "' + username + '", "target": "' + target + '", "message": "' + mesage + '"}').encode()
        else:
            return ('{"op": "MESSAGE", "target": "' + target + '", "message": "' + mesage + '"}').encode()

    @staticmethod
    def join(channel: str, username: str, passw: str = None) -> bytes:
        if passw != None:
            return (
                    '{"op": "JOIN", "user": "' + username + '", "channel": "' + channel + '", "pass": "' + passw + '"}').encode()
        else:
            return ('{"op": "JOIN", "user": "' + username + '", "channel": "' + channel + '"}').encode()

    @staticmethod
    def part(channel: str, username: str) -> bytes:
        return ('{"op": "PART", "user": "' + username + '", "channel": "' + channel + '"}').encode()

    @staticmethod
    def admin(channel: str, username: str) -> bytes:
        return ('{"op": "ADMIN", "user": "' + username + '", "channel": "' + channel + '"}').encode()

    @staticmethod
    def kick(channel: str, username: str, message: str = None) -> bytes:
        if message != None:
            return (
                    '{"op": "KICK", "user": "' + username + '", "channel": "' + channel + '", "message": "' + message + '"}').encode()
        else:
            return ('{"op": "KICK", "user": "' + username + '", "channel": "' + channel + '"}').encode()

    @staticmethod
    def ack(success: str, hash: str) -> bytes:
        return ('{"op": "ACK", "hash": "' + hash + '", "success": ' + success + '}').encode()

    @staticmethod  ###### TEM QUE DAR UMA OLHADA NESSE CARA #####    LISTA DE OBJ? CHAVE VALOR? DUAS LISTAS?
    def channels(channelList: list = None) -> bytes:
        if channelList != None:
            for a in channelList:  ### str = str undefined, funciona?
                lst = lst + '{"name": "' + a.name + '", "pass": "' + a.passw + '"},'
            return ('{"op": "CHANNELS", "channels": [' + lst[:-1] + '] }').encode()
        else:
            return '{"op": "CHANNELS"}'.encode()

    @staticmethod
    def users(userList: list, hash: str, channel: str = None) -> bytes:
        if channel != None:
            return (
                        '{"op": "USERS", "channel": "' + channel + '", "userList": "' + userList + '", "hash": "' + hash + '"}').encode()
        else:
            return ('{"op": "USERS", "hash": "' + hash + '"}').encode()
