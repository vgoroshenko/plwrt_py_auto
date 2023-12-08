class ABPageLocators:
    NO_AB_TEXT = 'h3'
    AB_PAGE = "//a[contains(@href, 'abtest')]"


class AddRemoveLocators:
    ADD_REMOVE_PAGE = "//a[contains(@href, '/add_remove_elements/')]"
    ADD_BUTTON = "button[onclick='addElement()']"
    DELETE_BUTTON = ".added-manually"
    DELETE_BUTTONS = "#elements"


class BasicAuthLocators:
    BASIC_AUTH_PAGE = "//a[contains(@href, 'basic')]"
    CONGRAT_MESSAGE = 'p'
    FAILED_MESSAGE = 'body'


class BrokenImagesLocators:
    BROKEN_IMAGE_PAGE = "//a[contains(@href, '/broken_images')]"
    PAGE_NAME = 'h3'


class ChallengingDomLocators:
    PAGE_NAME = 'h3'
    CHALLENGING_DOM_PAGE = "//a[@href='/challenging_dom']"
    FIRST_BUTTON = "[class='button']"
    SECOND_BUTTON = ".button.alert"
    THIRD_BUTTON = ".button.success"
    ANSWER = '#canvas'


class CheckboxesLocators:
    PAGE_NAME = 'h3'
    CHECKBOXES_PAGE = "//a[@href='/checkboxes']"
    FIRST_CHECKBOX = 'input:nth-of-type(1)'
    SECOND_CHECKBOX = 'input:nth-of-type(2)'


class ContextMenuLocators:
    PAGE_NAME = 'h3'
    CONTEXT_PAGE = "//a[@href='/context_menu']"
    BOX_BUTTON = '#hot-spot'


class BasePageLocators:
    PAGE_NAME = '.example h3'


class DisappearingElementsLocators:
    DISAPPERATING_PAGE = "//a[@href='/disappearing_elements']"
    BUTTON_LIST = '//li//a'


class DragAndDropLocators:
    DRAG_AND_DROP_PAGE = "//a[@href='/drag_and_drop']"
    BOX_A = '#column-a'
    BOX_B = '#column-b'


class DropdownLocators:
    DROPDOWN_PAGE = "//a[@href='/dropdown']"
    DROPDOWN_BUTTON = '#dropdown'
    DROPDOWN_FIRST_ELEMENT = "option[value='1']"
    DROPDOWN_SECOND_ELEMENT = "option[value='2']"


class DynamicContentLocators:
    DYNAMIC_CONTENT_PAGE = "//a[@href='/dynamic_content']"
    CHANGE_CONTENT_BUTTON = "//a[contains(@href, 'with')]"
    ALL_TEXT_CONTENT_ELEMENTS = '#content:nth-child(1) .row .large-10'


class DynamicallyLoadedLocators:
    DYNAMICALLY_LOADED_PAGE = "//a[@href='/dynamic_loading']"
    EXAMPLE_ONE_BUTTON = "//a[@href='/dynamic_loading/1']"
    EXAMPLE_TWO_BUTTON = "//a[@href='/dynamic_loading/2']"
    START_BUTTON = "button"
    LOADING_BAR = '#loading'
    FINISH_TEXT = '#finish'


class EntryAdLocators:
    LOADED_PAGE = "//a[@href='/entry_ad']"
    CLOSE_BUTTON = "div[class='modal-footer']"
    RE_ENABLE_BUTTON = '#restart-ad'
    POPUP = '.modal'


class ExitIntentLocators:
    LOADED_PAGE = "//a[@href='/exit_intent']"
    CLOSE_BUTTON = "div[class='modal-footer']"
    POPUP = '.modal'


class FileDownloadLocators:
    LOADED_PAGE = "//a[@href='/download']"
    FILE = "div[class='example'] a"


class FileUploadLocators:
    LOADED_PAGE = "//a[@href='/upload']"
    FILE_UPLOAD = "#file-upload"
    FILE_SUBMIT = '#file-submit'
    FILE_UPLOAD_DRAG_AND_DROP = '#drag-drop-upload'
    UPLOADED_FILE = '#uploaded-files'
    UPLOADED_FILE_ERROR_SUMMARY = '#summary'


class FormAuthenticationLocators:
    PAGE_NAME = "h2"
    LOADED_PAGE = "//a[@href='/login']"
    FIELD_USERNAME = '#username'
    FIELD_PASSWORD = '#password'
    BUTTON_LOGIN = '.radius'
    BUTTON_LOGOUT = '.button.secondary'
    BUTTON_CLOSE_MESSAGE = '.close'
    SUCCESS_LOGIN_PAGE = "h2"
    SUCCESS_MESSAGE = '.flash.success'
    ERROR_MESSAGE = '.flash.error'


# class FramesLocators:
#     LOADED_PAGE = "//a[@href='/frames']")
#     NESTED_FRAMES_BUTTON = "//a[@href='/nested_frames']")
#     IFRAMES_BUTTON = "//a[@href='/iframe']")
#     FRAMES = "frame")
#     FRAME_LEFT = 'frame[name="frame-left"]')
#     FRAME_BODY = 'body')
#     FIELD_IFRAME = '#tinymce > p')
#     IFRAMES = (By.TAG_NAME, 'iframe')
#     IFRAME_ID = '#mce_0_ifr')
#
#
# class GeolocationLocators:
#     LOADED_PAGE = "//a[@href='/geolocation']")
#     BUTTON_WHERE_I_AM = '.example button')
#     BUTTON_GOOGLE_MAP = '#map-link > a')
#     LATITUDE_COORD = '#lat-value')
#     LONGITUDE_COORD = '#long-value')
#
# class HorizontalSliderLocators:
#     LOADED_PAGE = "//a[@href='/horizontal_slider']")
#     SLIDER = '.sliderContainer > input')
#     SLIDER_VALUE = '#range')
#
# class HoverLocators:
#     LOADED_PAGE = "//a[@href='/hovers']")
#     PERSONS = '.figure')
#     PERSONS_NAME = '.figcaption h5')
#     PERSONS_LINK = '.figcaption a')
#
# class InfinityScrollLocators:
#     LOADED_PAGE = "//a[@href='/infinite_scroll']")
#     SCROLLED_ROW = '.jscroll-added')
#
# class InputsLocators:
#     LOADED_PAGE = "//a[@href='/inputs']")
#     INPUT = '[type="number"]')
#
# class JQueryUIMenusLocators:
#     LOADED_PAGE = "//a[contains(@href, '/jqueryui/menu')]")
#     BUTTON_ENABLED = '#ui-id-2')
#     BUTTON_DOWNLOADS = '#ui-id-4')
#     BUTTON_BACK = '#ui-id-5')
#     BUTTON_PDF = '#ui-id-5')
#     BUTTON_CSV = '#ui-id-5')
#     BUTTON_EXCEL = '#ui-id-5')
#
# class JSAlertsLocators:
#     LOADED_PAGE = "//a[@href='/javascript_alerts']")
#     JS_ALERT = "button[onclick='jsAlert()']")
#     JS_ALERT_CONFIRM = "button[onclick='jsConfirm()']")
#     JS_ALERT_PROMT = "button[onclick='jsPrompt()']")
#     RESULT_TEXT = "#result")
#
# class JSOnloadLocators:
#     LOADED_PAGE = "//a[@href='/javascript_error']")
#     PAGE_NAME = "p")
#
# class KeyPressesLocators:
#     LOADED_PAGE = "//a[@href='/key_presses']")
#     INPUT_TEXT = '#target')
#     INPUT_TEXT_RESULT = '#result')
#
# class LargeDomLocators:
#     LOADED_PAGE = "//a[@href='/large']")
#
# class MultipleWindowLocators:
#     LOADED_PAGE = "//a[@href='/windows']")
#     BUTTON = '.example a')
#
# class NotificationMessagesLocators:
#     LOADED_PAGE = "//a[@href='/notification_message']")
#     BUTTON_ACTION = 'p a')
#     BUTTON_CLOSE_NOTIF = '.close')
#     NOTIFICATION = '#flash')
#
# class RedirectLinkLocators:
#     LOADED_PAGE = "//a[@href='/redirector']")
#     BUTTON_REDIRECT = '#redirect')
#     BUTTON_200 = "//a[@href='status_codes/200']")
#     BUTTON_301 = "//a[@href='status_codes/301']")
#     BUTTON_404 = "//a[@href='status_codes/404']")
#     BUTTON_501 = "//a[@href='status_codes/500']")
#     BUTTON_RETURN = "//a[@href='/status_codes']")
#     STATUS_CODE_TEXT = 'p')
#
# class SecureFileDownloadLinkLocators:
#     LOADED_PAGE = "//a[@href='/download_secure']")
#     BUTTON_DOWNLOAD = '.example a')
#
# class ShadowDOMLocators:
#     LOADED_PAGE = "//a[@href='/shadowdom']")
#     PAGE_NAME = "h1")
#     FIRST_TEXT = 'span')
#     SECOND_TEXT = "ul li:nth-child(1)")
#     THIRD_TEXT = 'ul li:nth-child(2)')
#
# class ShiftingContentLocators:
#     LOADED_PAGE = "//a[@href='/shifting_content']")
#     BUTTON_EXAMPLE_1 = "//a[@href='/shifting_content/menu']")
#     BUTTON_EXAMPLE_2 = "//a[@href='/shifting_content/image']")
#     BUTTON_EXAMPLE_3 = "//a[@href='/shifting_content/list']")
#     BUTTON_MOVED = '.shift')
#     BUTTON_MODE_RANDOM = "//a[@href='/shifting_content/menu?mode=random']")
#     BUTTON_MODE_PIXEL_SHIFT = "//a[@href='/shifting_content/menu?pixel_shift=100']")
#     BUTTON_MODE_IMAGE_PIXEL_SHIFT = "//a[@href='/shifting_content/image?pixel_shift=100']")
#     BUTTON_MODE_RANDOM_PIXEL_SHIFT = "//a[@href='/shifting_content/menu?mode=random&pixel_shift=100']")
#     BUTTON_IMAGE_TYPE = "//a[contains(@href, 'type')]")
#     LIST_TEXT = "div[class^='large-6']")
#
# class StatusCodeLocators:
#     LOADED_PAGE = "//a[@href='/status_codes']")
#     BUTTON_200 = "//a[@href='status_codes/200']")
#     BUTTON_301 = "//a[@href='status_codes/301']")
#     BUTTON_404 = "//a[@href='status_codes/404']")
#     BUTTON_501 = "//a[@href='status_codes/500']")
#     BUTTON_RETURN = "//a[@href='/status_codes']")
#     STATUS_CODE_TEXT = 'p')
class UrlLocators:
    MAIN_URL = "http://172.17.0.1:5000/"
     #MAIN_URL = "http://localhost:5000/"
