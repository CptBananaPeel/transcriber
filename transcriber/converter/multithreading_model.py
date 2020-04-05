from PyQt5 import QtCore

from transcriber.converter import model, dbfconverter


class MultiThreadingConverterModel(model.ConverterModel):
    def __init__(self):
        super(MultiThreadingConverterModel, self).__init__()
        self.pool = QtCore.QThreadPool()

    @QtCore.pyqtSlot(list, set, int, int, list)
    def convert(self, filenames, tags, total_tags, num_cpu, tag_lookup):
        self.total_files = len(filenames)
        self.conversion_started.emit()
        self.pool.setMaxThreadCount(num_cpu)
        for filename in filenames:
            worker = dbfconverter.create_worker(
                filename, tags, total_tags, tag_lookup)
            worker.connect_finished(self.update_conversion_total)
            worker.connect_error(self.conversion_error.emit)
            self.pool.start(worker)
        self.pool.waitForDone()
        self.conversion_finished.emit()
