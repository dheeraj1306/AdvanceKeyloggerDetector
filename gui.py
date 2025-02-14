import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QMessageBox
from process_monitor import detect_suspicious_processes
from keyboard_hook import detect_keyboard_hook

class KeyloggerDetectorGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.detections = []  # List to store detected keyloggers

    def initUI(self):
        self.setWindowTitle("Advanced Keylogger Detection Tool")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.result_text = QTextEdit(self)
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        self.scan_button = QPushButton("Scan for Keyloggers", self)
        self.scan_button.clicked.connect(self.run_detection)
        layout.addWidget(self.scan_button)

        self.export_button = QPushButton("Export Report", self)
        self.export_button.clicked.connect(self.export_report)  # Ensure it's connected
        layout.addWidget(self.export_button)

        self.setLayout(layout)

    def run_detection(self):
        self.result_text.clear()
        self.detections = []  # Reset detections list

        # Run keylogger detection methods
        self.result_text.append("[INFO] Running keylogger detection...\n")

        suspicious_processes = detect_suspicious_processes()
        if suspicious_processes:
            self.result_text.append("[WARNING] Suspicious processes detected:")
            for process in suspicious_processes:
                self.result_text.append(f"  - {process}")
                self.detections.append(process)
        else:
            self.result_text.append("[SAFE] No suspicious processes found.")

        keyboard_hooks = detect_keyboard_hook()
        if keyboard_hooks:
            self.result_text.append("\n[WARNING] Keyboard hook detected!")
            self.detections.append("Keyboard Hook Detected")
        else:
            self.result_text.append("\n[SAFE] No keyboard hook detected.")

    def export_report(self):
        if not self.detections:
            QMessageBox.warning(self, "No Data", "No keyloggers detected to export.")
            return

        try:
            report_path = os.path.join(os.getcwd(), "keylogger_report.txt")
            with open(report_path, "w") as report_file:
                report_file.write("\n".join(self.detections))
            
            QMessageBox.information(self, "Success", f"Report saved: {report_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to export report: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KeyloggerDetectorGUI()
    window.show()
    sys.exit(app.exec_())
