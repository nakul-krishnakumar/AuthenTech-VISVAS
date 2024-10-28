from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.progressbar import ProgressBar
from kivy.uix.label import Label

class AuthentechApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # App Title
        title_label = Label(text="Authentech Visvas", font_size=24, bold=True)
        layout.add_widget(title_label)

        # Upload Buttons
        upload_original_btn = Button(text="Upload Original Signature", size_hint=(1, None), height=40)
        upload_test_btn = Button(text="Upload Test Signature", size_hint=(1, None), height=40)
        layout.add_widget(upload_original_btn)
        layout.add_widget(upload_test_btn)

        # Progress Bar
        progress_bar = ProgressBar(max=100, value=0, size_hint=(1, None), height=20)
        progress_bar_label = Label(text="Performing analysis", font_size=16)
        progress_bar_layout = BoxLayout(orientation='vertical', size_hint=(1, None), height=60)
        progress_bar_layout.add_widget(progress_bar_label)
        progress_bar_layout.add_widget(progress_bar)
        layout.add_widget(progress_bar_layout)

        # Verification Button
        verify_btn = Button(text="VERIFY SIGNATURE", size_hint=(1, None), height=40)
        layout.add_widget(verify_btn)

        return layout

if __name__ == '__main__':
    AuthentechApp().run()