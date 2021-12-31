import logging
import sys

app_log = logging.getLogger("client_log")
app_log.setLevel(logging.INFO)
app_log_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
if __name__ == "__main__":
    my_file = logging.FileHandler("client_log.log")
else:
    my_file = logging.FileHandler("log/client_log.log")
my_file.setFormatter(app_log_formatter)

my_stream = logging.StreamHandler(sys.stderr)
my_stream.setFormatter(app_log_formatter)

app_log.addHandler(my_file)
app_log.addHandler(my_stream)


if __name__ == "__main__":
    app_log.critical("Критическая ошибка")
    app_log.warning("Ошибка")
    app_log.info("Инфо")