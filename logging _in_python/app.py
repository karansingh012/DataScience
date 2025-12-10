import logging
## logging setting
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)


logger=logging.getLogger("ArithmeticApp")
logger.setLevel(logging.DEBUG)


def add(a,b):
    result =  a+b
    logger.debug(f"adding {a}+{b}={result}")
    return result

def sub(a,b):
    result =  a-b
    logger.debug(f"subtraction {a}-{b}={result}")
    return result

def multiplications(a,b):
    result =  a*b
    logger.debug(f"adding {a}*{b}={result}")
    return result

def division(a,b):
    try:
        result = a/b
        logger.debug(f"adding {a}/{b}={result}")
        return result
    except ZeroDivisionError:
        logger.error("division by zero error")
        return None


add(12,13)
sub(20,10)
multiplications(10,20)
division(12,4)


# # ...existing code...
# import logging
# ## logging setting
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S',
#     handlers=[
#         logging.FileHandler("app1.log"),
#         logging.StreamHandler()
#     ]
# )

# logger=logging.getLogger("ArithmeticApp")
# logger.setLevel(logging.DEBUG)

# # ensure the named logger also has a stream handler if running in odd envs
# if not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
#     logger.addHandler(logging.StreamHandler())

# def add(a,b):
#     result =  a+b
#     logger.debug(f"adding {a}+{b}={result}")
#     return result

# def sub(a,b):
#     result =  a-b
#     logger.debug(f"subtraction {a}-{b}={result}")
#     return result

# def multiplications(a,b):
#     result =  a*b
#     logger.debug(f"adding {a}*{b}={result}")
#     return result

# def division(a,b):
#     try:
#         result = a/b
#         logger.debug(f"adding {a}/{b}={result}")
#         return result
#     except ZeroDivisionError:
#         logger.error("division by zero error")
#         return None

# # call only when run as script
# if __name__ == "__main__":
#     print("Running app.py — results printed plus logged")
#     print("add:", add(12,13))
#     print("sub:", sub(20,10))
#     print("mul:", multiplications(10,20))
#     print("div:", division(12,4))
# # ...existing code...