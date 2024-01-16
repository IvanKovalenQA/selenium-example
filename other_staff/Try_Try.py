#After Collection Creating
#Verify that collection's image was synced in connected store
element = browser.find_element(By.XPATH, "//img[@class='mXwfQ']")
src_attribute_value = element.get_attribute("src")
search_word = 'renis'
if "renis" in src_attribute_value:
    print(Fore.GREEN + f'Image was added succesfully "{search_word}".')
else:
    print(Fore.RED + f'Image was not added succesfully "{search_word}".')

print(Style.RESET_ALL)

time.sleep(10)





#After Collection Updating
#Verify that collection's image was synced in connected store
element = browser.find_element(By.XPATH, "//img[@class='mXwfQ']")
src_attribute_value = element.get_attribute("src")
search_word = 'tshirt'
if "tshirt" in src_attribute_value:
    print(Fore.GREEN + f'Image was updated succesfully "{search_word}".')
else:
    print(Fore.RED + f'Image was not updated succesfully "{search_word}".')

print(Style.RESET_ALL)