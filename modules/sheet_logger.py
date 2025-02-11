class SheetLogger:
    def log_aposta_status(self, aposta_row, status_data):
        """Adiciona log na própria linha da aposta na planilha"""
        sheet = self.get_sheet()
        log_column = 'Z'  # Coluna para logs
        current_logs = sheet[f"{log_column}{aposta_row}"].value
        new_log = f"{datetime.now()}: {status_data}"
        sheet[f"{log_column}{aposta_row}"] = f"{current_logs}\n{new_log}"
