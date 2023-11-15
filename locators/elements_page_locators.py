from selenium.webdriver.common.by import By


class HeadHunterLocators:
    BUTTON_ADVANCED_SEARCH = (By.CSS_SELECTOR, "span[class = 'bloko-button__icon']") #Кнопка Расширенный поиск
    KEYWORDS = (By.CSS_SELECTOR, "input[data-qa='vacancysearch__keywords-input']")  #Ключевое слово
    KEYWORDS_CHOOSE = (By.CSS_SELECTOR, "ul[class='suggest__items']") #Выбор ключевого слова
    BUTTON_SPECIALIZATION = (By.CSS_SELECTOR, "button[data-qa ='resumesearch__profroles-switcher']") #Специализация
    LIST_SPECIALIZATION = (By.XPATH, "//span[contains(@data-qa, 'node-category-11')]") # Открытие списока специализаций
    LIST_SPECIALIZATION_FIND_TESTER = (By.CSS_SELECTOR, "input[data-qa='bloko-tree-selector-popup-search']") #Поиск специализации
    LIST_SPECIALIZATION_CHOOSE_TESTER = (By.XPATH, "//span[contains(@data-qa, 'bloko-tree-selector-item-text-124')]") #Выбор специализации тестировщик
    LIST_SPECIALIZATION_BUTTON_ACCEPT = (By.CSS_SELECTOR, "button[data-qa = 'bloko-tree-selector-popup-submit']") #Нажатие кнопки Выбрать в специализации
    REGION = (By.CSS_SELECTOR, "input[data-qa='advanced-search-region-add'") #Ввод регионов
    EDUCATION = (By.CSS_SELECTOR, "span[data-qa='advanced-search__education-item-label_not_required_or_not_specified']") #Образование
    EMPLOYMENT_TYPE = (By.CSS_SELECTOR, "span[data-qa='advanced-search__employment-item-label_full']") #Тип занятости
    SCHEDULE_FULL_DAY = (By.CSS_SELECTOR, "span[data-qa='advanced-search__schedule-item-label_fullDay']") #График работы полный день
    SCHEDULE_DISTANT_WORK = (By.CSS_SELECTOR, "span[data-qa='advanced-search__schedule-item-label_remote']") #График работы удаленная работа
    SORT_BY_DATA = (By.CSS_SELECTOR, "span[data-qa='advanced-search__order_by-item-label_publication_time']") #Сортировка по дате
    BUTTON_FIND = (By.CSS_SELECTOR, "button[data-qa='advanced-search-submit-button']") #Нажатие кнопки Найти
