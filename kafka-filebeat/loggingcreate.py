import logging
print(logging.debug)
logging.basicConfig(filename='app.log',level=10,filemode='a',format=' %(levelname)s - %(message)s')
logging.debug("Logging test...")
logging.info("The program is working as expected")
logging.warning("The program may not function properly")
logging.error("The program encountered an error")
logging.critical("The program crashed")
