import logger
import tgbot

def main() -> None:
	logger.configure()
	tgbot.start()

if __name__ == "__main__":
	main()
