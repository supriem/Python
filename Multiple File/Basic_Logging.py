# demonstrate the logging api python
import logging
# TODO: use the built-in logging module

def main():
    # TODO: use basicconfig to configure logging
    logging.basicConfig(level = logging.DEBUG,
                        filename = "output.log")
    # Try out each log levels
    
    logging.debug(" This is a debug msg")
    logging.info(" This is a info msg")
    logging.warning(" This is a warning msg")
    logging.error(" This is an error msg")
    logging.critical(" This is a critical msg")
if __name__ == "__main__":
    main()