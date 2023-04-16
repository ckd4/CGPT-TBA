import logger
import telegram_bot

def main() -> None:
	logger.configure()
	telegram_bot.start()

if __name__ == "__main__":
	main()
