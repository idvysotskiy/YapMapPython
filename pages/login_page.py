from pages.base_page import BasePage
from pages.profile_page import ProfilePage


class LoginPage(BasePage):
    menu = ProfilePage()
    profile = ProfilePage()

    sign_in_btn = "com.yapmap.yapmap:id/sign_in_button"
    email_field = '//*[@resource-id="com.yapmap.yapmap:id/email_edit_text_layout"]/android.widget.FrameLayout[1]'
    password_field = '//*[@resource-id="com.yapmap.yapmap:id/password_edit_text_layout"]/android.widget.FrameLayout[1]'

    def authorization(self):
        self.click(self.sign_in_btn)
        self.set_text(self.email_field, 'hell1k@yandex.ru')
        self.set_text(self.password_field, '12345678Qq!')
        self.click(self.sign_in_btn)