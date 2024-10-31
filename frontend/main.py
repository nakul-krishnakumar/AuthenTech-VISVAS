from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from plyer import filechooser as fc        #do import plyer


class MainLayout(BoxLayout):
    def upload_original_signature(self):
        file_path = fc.open_file(title="Select Original Signature")
        if file_path:
            self.ids.original_image.source = file_path[0]  # Set image source
            self.ids.original_image.reload()               # Refresh the image

    def upload_test_signature(self):
        file_path = fc.open_file(title="Select Test Signature")
        if file_path:
            self.ids.test_image.source = file_path[0]     # Set image source
            self.ids.test_image.reload()                  # Refresh the image

class AuthentechApp(App):
    def build(self):
        return MainLayout()

app = AuthentechApp()
app.run()