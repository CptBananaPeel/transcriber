class FileSelecter:
    def __init__(self, view):
        self.view = view

    def disable(self):
        self.view.disable()

    def enable(self):
        self.view.enable()

    def add_files(self, files):
        self.view.add_files(files)

    def del_current(self, file):
        self.view.del_current()

    def enable_deletion(self):
        self.view.enable_deletion()

    def connect_add_clicked(self, slot):
        self.view.connect_add_clicked(slot)

    def disconnect_add_clicked(self, slot):
        self.view.disconnect_add_clicked(slot)

    def connect_del_clicked(self, slot):
        self.view.connect_del_clicked(slot)

    def disconnect_add_clicked(self, slot):
        self.view.disconnect_del_clicked(slot)

    def connect_current_changed(self, slot):
        self.view.connect_current_changed(slot)

    def disconnect_current_changed(self, slot):
        self.view.disconnect_current_changed(slot)
