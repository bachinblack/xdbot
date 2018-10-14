import sys


class Params:
    LANG = sys.argv[0] or "en"
    BAN = sys.argv[1] or "zoe"
    PICK = sys.argv[2] or "nautilus"


class Constants:
    RES_ACCEPT_GAME = "accept_game.png"
    RES_PREPICK = "prepick.png"

    RES_TITLE_PICK = "title_pick.png"
    RES_FIND_PICK = "find_pick.png"
    RES_LOCK_PICK = "lock_pick.png"
    
    RES_TITLE_BAN = "title_ban.png"
    RES_FIND_BAN = "find_ban.png"
    RES_LOCK_BAN = "lock_ban.png"
