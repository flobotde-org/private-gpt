import os
from gradio import blocks
from .private_gpt import PrivateGptUi  # assuming this is where your class is defined

class PrivateGptUi(PrivateGptUi):  # assuming you have a base class with the same name
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._ui_block = None

    def _build_ui_blocks(self) -> blocks.Blocks:
        # your existing code here...

class PrivateGptUi(PrivateGptUi):  # assuming you have a base class with the same name
    def get_ui_blocks(self) -> blocks.Blocks:
        if self._ui_block is None:
            self._ui_block = self._build_ui_blocks()
        return self._ui_block

    def mount_in_app(self, app: FastAPI, path: str) -> None:
        blocks = self.get_ui_blocks()
        blocks.queue()
        logger.info("Mounting the gradio UI, at path=%s", path)
        gr.mount_grado_app(app, blocks, path=path, favicon_path=AVATAR_BOT)

if __name__ == "__main__":
    ui = PrivateGptUi()  # assuming you have a class with this name
    _blocks = ui.get_ui_blocks()
    _blocks.queue()
    _blocks.launch(debug=False, show_api=False)
