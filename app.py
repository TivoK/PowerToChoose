from menu import scrape_rates

if __name__ == '__main__':
    try:
       scrape_rates()
    except ValueError:
        print("Value Error - Check Logs/Web Page Locators.")
    except:
        print("An Occurred please see Logs.")

