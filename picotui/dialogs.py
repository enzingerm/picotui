from .widgets import *


def add_ok_cancel_buttons(d):
    hw = d.w // 2
    off1 = (hw + 1) // 2 - 4
    off2 = (d.w - hw) + hw // 2 - 4
    b = WButton(8, "OK")
    d.add(off1, d.h - 1, b)
    b.finish_dialog = ACTION_OK

    b = WButton(8, "Cancel")
    d.add(off2, d.h - 1, b)
    b.finish_dialog = ACTION_CANCEL


class DTextEntry(Dialog):

    def __init__(self, entry_w, text, title=""):
        super().__init__(10, 5, title=title)
        self.entry = WTextEntry(entry_w, text)
        self.entry.finish_dialog = ACTION_OK
        self.add(1, 1, self.entry)

    def result(self):
        res = self.loop()
        if res == ACTION_OK:
            return self.entry.get_text()


class DMultiEntry(Dialog):

    def __init__(self, entry_w, entry_h, lines, title=""):
        super().__init__(10, 5, entry_w + 2, entry_h + 3, title=title)
        self.widget = WMultiEntry(entry_w, entry_h, lines)
        self.add(1, 1, self.widget)
        add_ok_cancel_buttons(self)

    def result(self):
        res = self.loop()
        if res == ACTION_CANCEL:
            return res
        return self.widget.content
