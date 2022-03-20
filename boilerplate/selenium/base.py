from selenium.common.exceptions import (
        NoSuchElementException,
        TimeoutException,
        NoSuchFrameException,
        ElementClickInterceptedException,
)
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

# TO BE MOVED INTO A CONFIG FILE
BASEURL = ""

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _current_url(self):
        return self.driver.current_url

    def _visit(self, url):
        if url.startswith("http"):
            self.driver.get(url)
        else:
            self.driver.get(config.BASEURL + url)

    def _switch_to(self, target):
        # Might need to add switch_to.alert and switch_to.active_element
        if target in ["default_content", "default content"]:
            self.driver.switch_to.default_content()
        elif target in ["parent_frame", "parent frame"]:
            self.driver.switch_to.parent_frame()
        else:
            self.driver.switch_to.window(target)

    def _find_element_by_locator(self, locator):
        return self.driver.find_element(locator["by"], locator["value"])

    def _find_element_text_by_locator(self, locator):
        return self._find_by_locator(locator).text

    def _find_elements_by_locator(self, locator):
        return self.driver.find_elements(locator["by"], locator["value"])

    def _find_element_by_xpath_text(self, text):
        return self.driver.find(By.XPATH, f".//*[text()[contains(.,{text})]]")

    def _find_element_by_locator_and_text(self, locator, text):
        elements = self._find_elements_by_locator(locator)  # Assigned to prevent stale reference errors
        for element in elements:
            if element.text.upper() == text.upper():
                return element

        return None

    def _find_element_by_locator_and_text_partial(self, locator, text):
        elements = self._find_elements_by_locator(locator)  # Assigned to prevent stale reference errors
        for element in elements:
            if text.upper() in element.text.upper():
                return element

        return None

    def _get_text_of_elements_by_locator(self, locator):
        texts = []
        if self._element_is_displayed_by_locator(locator, 5):
            for element in self._find_elements_by_locator(locator):
                texts.append(element.text)

        return texts

    def _click_by_locator(self, locator):
        assert self._element_is_clickable_by_locator(locator, timeout=15)
        self._find_element_by_locator(locator).click()

    def _type_at_locator(self, locator, input_text):
        self._find_element_by_locator(locator).send_keys(input_text)

    def _get_frames(self):
        return self.driver.find_elements(By.TAG_NAME, "iframe")

    def _find_frame_containing_locator(self, locator):
        # FIXME: Only goes one level deep, needs to be recursive
        frames = self._get_frames()
        frame_idx = 0

        while frame_idx < len(frames):
            elements = None
            self._switch_to_frame(frame_idx)

            try:
                elements = self._find_elements_by_locator(locator)
            except NoSuchElementException:
                pass

            self._switch_to("parent frame")
            if elements:
                break

            frame_idx += 1
        else:
            raise NoSuchElementException

        return frame_idx

    def _element_exits_within_frame(self, locator):
        frames = self._get_frames()
        frame_idx = 0

        while frame_idx < len(frames):
            self._switch_to_frame(frame_idx)
            elements = self._element_is_displayed_by_locator(locator, 5)
            self._switch_to("parent_frame")
            if elements:
                return True

            frame_idx += 1

        return False

    def _wait(self, timeout, function, *args, **kwargs):
        if timeout:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(
                        lambda *args, **kwargs: function(*args, **kwargs)
                )
            except TimeoutException:
                return False

            return True

        try:
            return function(*args, **kwargs)
        except:
            return False

    def _element_is_no_longer_displayed_by_locator(self, locator, timeout=0):
        self._wait(timeout, expected_conditions.invisibility_of_element_located, (locator["by"], locator["value"]))

    #def _element_is_no_longer_displayed_by_locator(self, locator, timeout=0):
    #    if timeout > 0:
    #        try:
    #            wait = WebDriverWait(self.driver, timeout)
    #            wait.until(
    #                    expected_conditions.invisibility_of_element_located(
    #                        (locator["by"], locator["value"])
    #                    )
    #            )

    #            return True
    #        except TimeoutException:
    #            return False

    #    try:
    #        return self._find_element_by_locator(locator).is_displayed()
    #    except NoSuchelementException:
    #        return False

    def _element_is_displayed_by_locator(locator, timeout=0):
        self._wait(timeout, expected_conditions.visibility_of_element_located, (locator["by"], locator["value"]))

    #def _element_is_displayed_by_locator(locator, timeout=0):
    #    if timeout > 0:
    #        try:
    #            wait = WebDriverWait(self.driver, timeout)
    #            wait.until(
    #                    expected_conditions.visibility_of_element_located(
    #                        (locator["by"], locator["value"])
    #                    )
    #            )

    #            return True
    #        except TimeoutException:
    #            print("_is_displayed TIMED OUT!")
    #            return False

    #    try:
    #        return self._find_element_by_locator(locator).is_displayed()
    #    except NoSuchElementException:
    #        return False

    def _text_is_no_longer_displayed_by_locator(self, locator, text, timeout=0):
        fn = lambda locator, text: self._find_element_by_locator_and_partial_text(locator, text) is None
        self._wait(timeout, fn, locator, text)

    #def _text_is_no_longer_displayed_by_locator(self, locator, text, timeout=0):
    #    if timeout > 0:
    #        try:
    #            wait = WebDriverWait(self.driver, timeout)
    #            wait.until(
    #                    lambda d: self._find_element_by_locator_and_partial_text(locator, text) is None
    #            )

    #            return True
    #        except TimeoutException:
    #            return False
    #        except ValueError:
    #            return False

    #    try:
    #        if self._find_element_by_locator_and_text_partial(locator, text):
    #            return True
    #        except ValueError:
    #            return False

    def _text_is_displayed_by_locator(self, locator, text, timeout=0):
        fn = lambda locator, text: self._find_element_by_locator_and_text_partial(locator, text) is not None
        self._wait(timeout, fn, locator, text)

    #def _text_is_displayed_by_locator(self, locator, text, timeout=0):
    #    if timeout > 0:
    #        try:
    #            wait.until(
    #                    lambda d: self._find_element_by_locator_and_text_partial(locator, text) is not None
    #            )

    #            return True
    #        except TimeoutException:
    #            print("TEXT CHECK TIMEOUT")
    #            return False
    #        except ValueError:
    #            return False

    #    try:
    #        if self._find_element_by_locator_and_text_partial(locator, text):
    #            return True
    #        except ValueError:
    #            return False

    def _element_is_clickable_by_locator(self, locator, timeout=5):
        element = self._find_element_by_locator(locator)
        self._wait(timeout, expected_conditions.element_to_be_clickable, element)

    #def _element_is_clickable(self, original_element, timeout=5):
    #    element = original_element
    #    if timeout > 0:
    #        print("In clickable timeout")
    #        try:
    #            wait = WebDriverWait(self.driver, timeout)
    #            wait.until(
    #                    expected_conditions.element_to_be_clickable(
    #                        element
    #                    )
    #            )
    #        except TimeoutException:
    #            print("IS_CLICKABLE TIMEOUT")
    #            return False
    #        except ElementClickInterceptedException:
    #            print("IS_CLICKABLE INTERCEPTED")
    #            return False

    #        return True

    #    try:
    #        if expected_conditions.element_to_be_clickable(
    #                element
    #            ):

    #            return True
    #        except ElementClickInterceptedException:
    #            return False

    def _frame_count_is(self, target, timeout=0):
        fn = lambda target: len(self._get_frames()) == target
        self._wait(timeout, fn, target)

    #def _frame_count_is(self, target, timeout=0):
    #    if timeout:
    #        try:
    #            wait = WebDriverWait(self.driver, timeout)
    #            wait.until(lambda d: len(self._get_frames()) == target)
    #        except NoSuchElementException:
    #            return False

    #        return True

    #    return len(self._get_frames()) == target

    def _frame_count_above_zero(self, timeout=0):
        fn = lambda: len(self._get_frames())
        self._wait(timeout, fn)

    #def _frame_count_above_zero(self, timeout=0):
    #    if timeout:
    #        try:
    #            wait = WebDriverWait(self.driver, timeout)
    #            wait.until(lambda d: len(self._get_frames()) > 0)
    #        except NoSuchElementException:
    #            return False

    #        return True

    #    try:
    #        return len(self._get_frames()) > 0
    #    except NoSuchElementException:
    #        return False

    def _switch_to_frame(self, target, timeout=0):
        self._wait(timeout, expect_conditions.frame_to_be_available_and_switch_to_it, target)

    #def _switch_to_frame(self, target, timeout=0):
    #    if timeout:
    #        try:
    #            wait = WebDriverWait(self.driver, timeout)
    #            wait.until(
    #                    expected_conditions.frame_to_be_available_and_switch_to_it(
    #                        target
    #                    )
    #                )
    #        except NoSuchFrameException:
    #            return False

    #    else:
    #        self.driver.switch_to.frame(target)

    def has_url(self, locator, timeout=0):
        self._wait(timeout, expected_conditions.url_matches, locator)

    #def has_url(self, locator, timeout=0):
    #    if timeout:
    #        try:
    #            wait = WebDriverWait(self.driver, timeout)
    #            wait.until(expected_conditions.url_matches(locator))
    #        except TimeoutException:
    #            return False
    #        return True

    #    return self.driver.current_url == locator
