# Yes, you can use a decorator in Python to implement retrying mechanisms for functions, including Selenium actions
# that may raise exceptions like InvalidElementStateException. Using a decorator can make your code cleaner and more
# modular, as it separates the retry logic from the main test case.
#
# Here's an example of how you can create a retry decorator to handle the InvalidElementStateException for Selenium
# actions:
#
# python
# Copy code
import time


# from selenium import webdriver
# from selenium.common.exceptions import InvalidElementStateException
#
# # Initialize the WebDriver instance
# driver = webdriver.Chrome()

# Decorator function for retrying the function multiple times
def retry_on_exception(exception_type, retries=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(retries + 1):
                try:
                    return func(*args, **kwargs)
                except exception_type as e:
                    print(f"Caught {exception_type.__name__}. Retrying...")
                    time.sleep(delay)
            raise exception_type(f"{exception_type.__name__} occurred {retries} times. Giving up.")

        return wrapper

    return decorator

# def retry_stale_element(func):
#     def wrapper(*args, **kwargs):
#         max_retries = 3
#         retries = 0
#         while retries < max_retries:
#             try:
#                 return func(*args, **kwargs)
#             except StaleElementReferenceException:
#                 print("StaleElementReferenceException occurred. Retrying...")
#                 retries += 1
#                 time.sleep(2)  # Wait for 2 seconds before retrying
#         raise StaleElementReferenceException(
#             "Max retries exceeded. Failed to handle StaleElementReferenceException.")
#     return wrapper
#
# @retry_stale_element #Decorator to handle stale element exception
# def click_element(element):
#         element.click()
# element =self.driver.find_element_by_xpath(self.mp.Loadmore)
# click_element(element)


# Exception handling

# element = WebDriverWait(self.driver, 10).until(
#     EC.presence_of_element_located((By.link_text, "Courses"))
# )
# # click the element
# element.click()
# try:
#     # wait 10 seconds before looking for element
#     element = WebDriverWait(self.driver, 10).until(
#         EC.presence_of_element_located((self.mp.cityselect))
#     )
# finally:
#     # else quit
#     self.driver.quit()
