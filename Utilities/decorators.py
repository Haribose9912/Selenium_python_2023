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