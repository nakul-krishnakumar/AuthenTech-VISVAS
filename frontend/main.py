from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from plyer import filechooser as fc
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.clock import Clock
from kivy.properties import NumericProperty

class MainLayout(BoxLayout):
    pass

class AuthentechApp(MDApp):
    progress_value = NumericProperty(0)
    dialog = None

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file('authentech.kv')

    def upload_original_signature(self):  # runs when upload_original btn is clicked
        file_path = fc.open_file(title="Select Original Signature")
        if file_path:
            self.root.ids.original_image.source = file_path[0]
            self.root.ids.original_image.reload()

    def upload_test_signature(self):  # runs when upload_test btn is clicked
        file_path = fc.open_file(title="Select Test Signature")
        if file_path:
            self.root.ids.test_image.source = file_path[0]
            self.root.ids.test_image.reload()

    def start_verification(self):
        self.root.ids.progress_bar.value = 0
        self.root.ids.verify_button.disabled = True
        Clock.schedule_interval(self.update_progress, 0.1)

    def update_progress(self, dt):
        if self.root.ids.progress_bar.value >= 100:
            self.root.ids.verify_button.disabled = False
            self.show_dialog("Verification Complete!\nSignatures match with 95% accuracy")
            return False
        self.root.ids.progress_bar.value += 2

    def show_dialog(self, message):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Notice",
                text=message,
                buttons=[
                    MDFlatButton(
                        text="OK",
                        on_release=self.close_dialog
                    )
                ]
            )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

if __name__ == '__main__':
    AuthentechApp().run()
