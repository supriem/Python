import logging
# TODO: add another function to log form

def main():
    # TODO: set the o/p file and debug level
    fmtstr = " %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
    logging.basicConfig(level = logging.DEBUG,
                        filename = "custom_output.log",
                        filemode = 'w',
                        format = fmtstr)
    logging.info("this is an logging info-level log message")
    logging.warning("this is an logging warning-level msg")

if __name__ == "__main__":
    main()
