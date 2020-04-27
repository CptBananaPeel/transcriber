from PyQt5 import QtWidgets, QtCore

from transcriber.searchable_list.widget import SearchableListWidget


class FileSelecterView(QtWidgets.QWidget):
    files_added = QtCore.pyqtSignal()
    files_removed = QtCore.pyqtSignal()

    def __init__(self):
        super(FileSelecterView, self).__init__()

        self._layout = QtWidgets.QVBoxLayout()

        self.files = SearchableListWidget(
            self, search_text="Search Loaded Files"
        )
        self.files.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection
        )
        self.add_file = QtWidgets.QPushButton("Load DAT File(s)", self)
        self.del_file = QtWidgets.QPushButton("Remove", self)
        self.del_file.setEnabled(False)

        self.add_file.setToolTip(
            "Select DAT files to transcribe. File names typically end in '(Float).DAT'."
        )
        self.del_file.setToolTip(
            "Remove selected files. These will no longer be transcribed."
        )

        self.add_file.clicked.connect(self.load_dat)
        self.del_file.clicked.connect(self.del_current)
        self.connect_current_changed(self.enable_deletion)
        self.files.doubleClicked.connect(self.del_current)

        self._layout.addWidget(self.add_file)
        self._layout.addWidget(self.files)
        self._layout.addWidget(self.del_file)
        self.setLayout(self._layout)

    def filenames(self):
        return [self.files.item(i).text() for i in range(self.files.count())]

    def load_dat(self):
        filenames, _ = QtWidgets.QFileDialog.getOpenFileNames(
            parent=self,
            caption="Select Float File(s) - DAT",
            filter="DAT (*.DAT)",
        )
        if filenames:
            self.add_files(filenames)
            self.files_added.emit()

    def add_files(self, files):
        self.files.addItems([f for f in files if f not in self.filenames()])

    def del_current(self):
        for item in self.files.selectedItems():
            self.files.takeItem(self.files.row(item))
        if not self.files.count():
            self.del_file.setEnabled(False)
        self.files_removed.emit()

    def enable_deletion(self):
        self.del_file.setEnabled(True)

    def connect_files_added(self, slot):
        self.files_added.connect(slot)

    def disconnect_files_added(self, slot):
        self.files_added.disconnect(slot)

    def connect_files_removed(self, slot):
        self.files_removed.connect(slot)

    def disconnect_files_removed(self, slot):
        self.files_removed.disconnect(slot)

    def connect_current_changed(self, slot):
        self.files.currentItemChanged.connect(slot)

    def disconnect_current_changed(self, slot):
        self.files.currentItemChanged.disconnect(slot)
