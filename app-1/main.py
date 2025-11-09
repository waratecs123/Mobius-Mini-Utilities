import customtkinter as ctk
from PIL import Image, ImageTk, ImageOps
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import json
import threading
from pathlib import Path
import shutil
import platform
import subprocess
import sys


class ImageOptimizer:
    def __init__(self):
        self.supported_formats = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp']
        self.current_language = "русский"
        self.selected_files = []
        self.current_os = platform.system().lower()

        self.languages = {
            "русский": {
                "title": "Möbius - Оптимизатор Изображений",
                "select_files": "Выбрать файлы",
                "select_folder": "Выбрать папку",
                "output_folder": "Папка для сохранения:",
                "browse": "Обзор",
                "quality": "Качество:",
                "max_width": "Макс. ширина:",
                "max_height": "Макс. высота:",
                "format": "Формат:",
                "optimize": "Оптимизировать",
                "progress": "Прогресс:",
                "files_selected": "файлов выбрано",
                "optimization_complete": "Оптимизация завершена!",
                "select_output_folder": "Выберите папку для сохранения",
                "no_files_selected": "Файлы не выбраны",
                "no_output_folder": "Выберите папку для сохранения",
                "compression_level": "Уровень сжатия:",
                "maintain_metadata": "Сохранять метаданные",
                "overwrite_existing": "Перезаписывать существующие",
                "preserve_structure": "Сохранять структуру папок",
                "advanced_settings": "Расширенные настройки",
                "status_ready": "Готов к работе",
                "status_processing": "Обработка...",
                "status_complete": "Завершено",
                "file_size": "Размер файла",
                "original": "Исходный",
                "optimized": "Оптимизированный",
                "savings": "Экономия",
                "language": "Язык:",
                "basic_settings": "Основные настройки",
                "results": "Результаты",
                "show_advanced": "Показать расширенные",
                "hide_advanced": "Скрыть расширенные",
                "processing_files": "Обработка файлов...",
                "error_processing": "Ошибка при обработке",
                "total_savings": "Общая экономия",
                "files_processed": "Файлов обработано",
                "estimated_time": "Примерное время",
                "remaining": "осталось",
                "cancel": "Отмена",
                "paused": "Приостановлено",
                "resume": "Продолжить",
                "os_specific": self.get_os_specific_text("русский")
            },
            "english": {
                "title": "Möbius - Image Optimizer",
                "select_files": "Select Files",
                "select_folder": "Select Folder",
                "output_folder": "Output Folder:",
                "browse": "Browse",
                "quality": "Quality:",
                "max_width": "Max Width:",
                "max_height": "Max Height:",
                "format": "Format:",
                "optimize": "Optimize",
                "progress": "Progress:",
                "files_selected": "files selected",
                "optimization_complete": "Optimization Complete!",
                "select_output_folder": "Select output folder",
                "no_files_selected": "No files selected",
                "no_output_folder": "Select output folder",
                "compression_level": "Compression Level:",
                "maintain_metadata": "Maintain Metadata",
                "overwrite_existing": "Overwrite Existing",
                "preserve_structure": "Preserve Folder Structure",
                "advanced_settings": "Advanced Settings",
                "status_ready": "Ready",
                "status_processing": "Processing...",
                "status_complete": "Complete",
                "file_size": "File Size",
                "original": "Original",
                "optimized": "Optimized",
                "savings": "Savings",
                "language": "Language:",
                "basic_settings": "Basic Settings",
                "results": "Results",
                "show_advanced": "Show Advanced",
                "hide_advanced": "Hide Advanced",
                "processing_files": "Processing files...",
                "error_processing": "Error processing",
                "total_savings": "Total savings",
                "files_processed": "Files processed",
                "estimated_time": "Estimated time",
                "remaining": "remaining",
                "cancel": "Cancel",
                "paused": "Paused",
                "resume": "Resume",
                "os_specific": self.get_os_specific_text("english")
            },
            "中文": {
                "title": "Möbius - 图像优化器",
                "select_files": "选择文件",
                "select_folder": "选择文件夹",
                "output_folder": "输出文件夹:",
                "browse": "浏览",
                "quality": "质量:",
                "max_width": "最大宽度:",
                "max_height": "最大高度:",
                "format": "格式:",
                "optimize": "优化",
                "progress": "进度:",
                "files_selected": "个文件已选择",
                "optimization_complete": "优化完成!",
                "select_output_folder": "选择输出文件夹",
                "no_files_selected": "未选择文件",
                "no_output_folder": "请选择输出文件夹",
                "compression_level": "压缩级别:",
                "maintain_metadata": "保留元数据",
                "overwrite_existing": "覆盖现有文件",
                "preserve_structure": "保留文件夹结构",
                "advanced_settings": "高级设置",
                "status_ready": "准备就绪",
                "status_processing": "处理中...",
                "status_complete": "完成",
                "file_size": "文件大小",
                "original": "原始",
                "optimized": "优化后",
                "savings": "节省",
                "language": "语言:",
                "basic_settings": "基本设置",
                "results": "结果",
                "show_advanced": "显示高级",
                "hide_advanced": "隐藏高级",
                "processing_files": "处理文件中...",
                "error_processing": "处理错误",
                "total_savings": "总节省",
                "files_processed": "已处理文件",
                "estimated_time": "预计时间",
                "remaining": "剩余",
                "cancel": "取消",
                "paused": "已暂停",
                "resume": "继续",
                "os_specific": self.get_os_specific_text("中文")
            },
            "español": {
                "title": "Möbius - Optimizador de Imágenes",
                "select_files": "Seleccionar Archivos",
                "select_folder": "Seleccionar Carpeta",
                "output_folder": "Carpeta de Salida:",
                "browse": "Examinar",
                "quality": "Calidad:",
                "max_width": "Ancho Máx:",
                "max_height": "Alto Máx:",
                "format": "Formato:",
                "optimize": "Optimizar",
                "progress": "Progreso:",
                "files_selected": "archivos seleccionados",
                "optimization_complete": "¡Optimización Completada!",
                "select_output_folder": "Seleccionar carpeta de salida",
                "no_files_selected": "No hay archivos seleccionados",
                "no_output_folder": "Seleccione carpeta de salida",
                "compression_level": "Nivel de Compresión:",
                "maintain_metadata": "Mantener Metadatos",
                "overwrite_existing": "Sobrescribir Existentes",
                "preserve_structure": "Preservar Estructura",
                "advanced_settings": "Configuraciones Avanzadas",
                "status_ready": "Listo",
                "status_processing": "Procesando...",
                "status_complete": "Completado",
                "file_size": "Tamaño del Archivo",
                "original": "Original",
                "optimized": "Optimizado",
                "savings": "Ahorro",
                "language": "Idioma:",
                "basic_settings": "Configuraciones Básicas",
                "results": "Resultados",
                "show_advanced": "Mostrar Avanzadas",
                "hide_advanced": "Ocultar Avanzadas",
                "processing_files": "Procesando archivos...",
                "error_processing": "Error al procesar",
                "total_savings": "Ahorro total",
                "files_processed": "Archivos procesados",
                "estimated_time": "Tiempo estimado",
                "remaining": "restante",
                "cancel": "Cancelar",
                "paused": "Pausado",
                "resume": "Continuar",
                "os_specific": self.get_os_specific_text("español")
            }
        }

        self.load_settings()
        self.setup_ui()

    def get_os_specific_text(self, language):
        """Возвращает OS-специфичный текст"""
        os_texts = {
            "русский": {
                "windows": " (Windows)",
                "linux": " (Linux)",
                "darwin": " (macOS)",
                "current_os": f"Текущая ОС: {self.get_os_name('русский')}",
                "os_features": self.get_os_features_text("русский")
            },
            "english": {
                "windows": " (Windows)",
                "linux": " (Linux)",
                "darwin": " (macOS)",
                "current_os": f"Current OS: {self.get_os_name('english')}",
                "os_features": self.get_os_features_text("english")
            },
            "中文": {
                "windows": " (Windows)",
                "linux": " (Linux)",
                "darwin": " (macOS)",
                "current_os": f"当前系统: {self.get_os_name('中文')}",
                "os_features": self.get_os_features_text("中文")
            },
            "español": {
                "windows": " (Windows)",
                "linux": " (Linux)",
                "darwin": " (macOS)",
                "current_os": f"SO Actual: {self.get_os_name('español')}",
                "os_features": self.get_os_features_text("español")
            }
        }
        return os_texts.get(language, os_texts["english"])

    def get_os_name(self, language):
        """Возвращает название ОС на нужном языке"""
        os_names = {
            "русский": {"windows": "Windows", "linux": "Linux", "darwin": "macOS"},
            "english": {"windows": "Windows", "linux": "Linux", "darwin": "macOS"},
            "中文": {"windows": "Windows", "linux": "Linux", "darwin": "macOS"},
            "español": {"windows": "Windows", "linux": "Linux", "darwin": "macOS"}
        }
        return os_names[language].get(self.current_os, "Unknown")

    def get_os_features_text(self, language):
        """Возвращает текст с особенностями ОС"""
        features = {
            "русский": {
                "windows": "• Оптимизировано для Windows\n• Поддержка Windows пути\n• Интеграция с проводником",
                "linux": "• Оптимизировано для Linux\n• Поддержка Unix путей\n• Интеграция с файловыми менеджерами",
                "darwin": "• Оптимизировано для macOS\n• Поддержка macOS путей\n• Интеграция с Finder"
            },
            "english": {
                "windows": "• Optimized for Windows\n• Windows path support\n• Explorer integration",
                "linux": "• Optimized for Linux\n• Unix path support\n• File manager integration",
                "darwin": "• Optimized for macOS\n• macOS path support\n• Finder integration"
            },
            "中文": {
                "windows": "• 为 Windows 优化\n• Windows 路径支持\n• 资源管理器集成",
                "linux": "• 为 Linux 优化\n• Unix 路径支持\n• 文件管理器集成",
                "darwin": "• 为 macOS 优化\n• macOS 路径支持\n• Finder 集成"
            },
            "español": {
                "windows": "• Optimizado para Windows\n• Soporte rutas Windows\n• Integración con Explorer",
                "linux": "• Optimizado para Linux\n• Soporte rutas Unix\n• Integración con gestores de archivos",
                "darwin": "• Optimizado para macOS\n• Soporte rutas macOS\n• Integración con Finder"
            }
        }
        return features[language].get(self.current_os, "")

    def get_os_specific_defaults(self):
        """Возвращает настройки по умолчанию для каждой ОС"""
        defaults = {
            'windows': {
                'default_output': str(Path.home() / "Pictures" / "Optimized"),
                'file_dialog_options': {}
            },
            'linux': {
                'default_output': str(Path.home() / "Pictures" / "Optimized"),
                'file_dialog_options': {}
            },
            'darwin': {
                'default_output': str(Path.home() / "Pictures" / "Optimized"),
                'file_dialog_options': {}
            }
        }
        return defaults.get(self.current_os, defaults['windows'])

    def setup_os_specific_features(self):
        """Настраивает OS-специфичные особенности"""
        # Устанавливаем пути по умолчанию для каждой ОС
        os_defaults = self.get_os_specific_defaults()
        if not self.output_path_var.get():
            self.output_path_var.set(os_defaults['default_output'])

        # Создаем папку для вывода если не существует
        Path(os_defaults['default_output']).mkdir(parents=True, exist_ok=True)

    def load_settings(self):
        """Загружает настройки из файла"""
        try:
            if os.path.exists("settings.json"):
                with open("settings.json", "r", encoding="utf-8") as f:
                    settings = json.load(f)
                    self.current_language = settings.get("language", "русский")
        except:
            self.current_language = "русский"

    def save_settings(self):
        """Сохраняет настройки в файл"""
        try:
            settings = {
                "language": self.current_language,
                "last_os": self.current_os
            }
            with open("settings.json", "w", encoding="utf-8") as f:
                json.dump(settings, f, ensure_ascii=False, indent=2)
        except:
            pass

    def get_text(self, key):
        """Возвращает текст на текущем языке"""
        return self.languages[self.current_language].get(key, key)

    def setup_ui(self):
        """Настраивает пользовательский интерфейс"""
        # Настройка темы в зависимости от ОС
        self.setup_os_theme()

        # Создание главного окна
        self.root = ctk.CTk()
        self.root.title(self.get_text("title") + self.get_text("os_specific")[self.current_os])
        self.root.geometry("900x960")
        self.root.resizable(False, False)
        self.root.minsize(800, 600)

        # Создание основного фрейма
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.create_header()
        self.create_file_selection()
        self.create_settings()
        self.create_advanced_settings()
        self.create_progress_section()
        self.create_results()

        # Настройка OS-специфичных особенностей
        self.setup_os_specific_features()

        self.update_ui_language()

    def setup_os_theme(self):
        """Настраивает тему в зависимости от ОС"""
        if self.current_os == 'windows':
            ctk.set_appearance_mode("Dark")
            ctk.set_default_color_theme("blue")
        elif self.current_os == 'darwin':  # macOS
            ctk.set_appearance_mode("System")
            ctk.set_default_color_theme("blue")
        else:  # Linux
            ctk.set_appearance_mode("Dark")
            ctk.set_default_color_theme("green")

    def create_header(self):
        """Создает заголовок и выбор языка"""
        header_frame = ctk.CTkFrame(self.main_frame)
        header_frame.pack(fill="x", pady=(0, 20))

        # Заголовок
        title_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        title_frame.pack(side="left", padx=20, pady=15)

        self.title_label = ctk.CTkLabel(
            title_frame,
            text="Möbius",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        self.title_label.pack(anchor="w")

        self.subtitle_label = ctk.CTkLabel(
            title_frame,
            text="",  # Будет установлено в update_ui_language
            font=ctk.CTkFont(size=12)
        )
        self.subtitle_label.pack(anchor="w")

        # Информация об ОС
        self.os_info_label = ctk.CTkLabel(
            title_frame,
            text="",  # Будет установлено в update_ui_language
            font=ctk.CTkFont(size=10),
            text_color="gray"
        )
        self.os_info_label.pack(anchor="w")

        # Выбор языка
        language_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        language_frame.pack(side="right", padx=20, pady=15)

        self.language_label = ctk.CTkLabel(language_frame, text="")
        self.language_label.pack(side="left", padx=(0, 10))

        self.language_var = ctk.StringVar(value=self.current_language)
        self.language_combo = ctk.CTkComboBox(
            language_frame,
            values=list(self.languages.keys()),
            variable=self.language_var,
            command=self.change_language,
            width=120
        )
        self.language_combo.pack(side="left")

    def create_file_selection(self):
        """Создает секцию выбора файлов"""
        file_frame = ctk.CTkFrame(self.main_frame)
        file_frame.pack(fill="x", pady=(0, 15))

        # Кнопки выбора
        button_frame = ctk.CTkFrame(file_frame, fg_color="transparent")
        button_frame.pack(fill="x", padx=20, pady=15)

        self.select_files_btn = ctk.CTkButton(
            button_frame,
            text="",  # Будет установлено в update_ui_language
            command=self.select_files,
            width=120
        )
        self.select_files_btn.pack(side="left", padx=(0, 10))

        self.select_folder_btn = ctk.CTkButton(
            button_frame,
            text="",  # Будет установлено в update_ui_language
            command=self.select_folder,
            width=120
        )
        self.select_folder_btn.pack(side="left")

        # Информация о выбранных файлах
        self.file_info_label = ctk.CTkLabel(
            button_frame,
            text="",
            font=ctk.CTkFont(size=12)
        )
        self.file_info_label.pack(side="right")

        # Папка для сохранения
        output_frame = ctk.CTkFrame(file_frame, fg_color="transparent")
        output_frame.pack(fill="x", padx=20, pady=(0, 15))

        self.output_folder_label = ctk.CTkLabel(output_frame, text="")
        self.output_folder_label.pack(side="left")

        self.output_path_var = ctk.StringVar()
        self.output_entry = ctk.CTkEntry(
            output_frame,
            textvariable=self.output_path_var,
            placeholder_text=""
        )
        self.output_entry.pack(side="left", fill="x", expand=True, padx=(10, 10))

        self.browse_btn = ctk.CTkButton(
            output_frame,
            text="",
            command=self.select_output_folder,
            width=80
        )
        self.browse_btn.pack(side="right")

    def create_settings(self):
        """Создает секцию настроек"""
        self.settings_frame = ctk.CTkFrame(self.main_frame)
        self.settings_frame.pack(fill="x", pady=(0, 15))

        # Заголовок настроек
        self.settings_title_label = ctk.CTkLabel(
            self.settings_frame,
            text="",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.settings_title_label.pack(anchor="w", padx=20, pady=(15, 10))

        # Основные настройки в сетке
        grid_frame = ctk.CTkFrame(self.settings_frame, fg_color="transparent")
        grid_frame.pack(fill="x", padx=20, pady=(0, 15))

        # Качество
        self.quality_label = ctk.CTkLabel(grid_frame, text="")
        self.quality_label.grid(row=0, column=0, sticky="w", padx=(0, 10))
        self.quality_slider = ctk.CTkSlider(grid_frame, from_=10, to=100, number_of_steps=90, width=200)
        self.quality_slider.set(85)
        self.quality_slider.grid(row=0, column=1, padx=(0, 20))
        self.quality_value_label = ctk.CTkLabel(grid_frame, text="85%")
        self.quality_value_label.grid(row=0, column=2)

        # Максимальная ширина
        self.max_width_label = ctk.CTkLabel(grid_frame, text="")
        self.max_width_label.grid(row=1, column=0, sticky="w", padx=(0, 10), pady=(10, 0))
        self.width_var = ctk.StringVar(value="1920")
        self.width_entry = ctk.CTkEntry(grid_frame, textvariable=self.width_var, width=100)
        self.width_entry.grid(row=1, column=1, sticky="w", padx=(0, 20), pady=(10, 0))

        # Максимальная высота
        self.max_height_label = ctk.CTkLabel(grid_frame, text="")
        self.max_height_label.grid(row=2, column=0, sticky="w", padx=(0, 10), pady=(10, 0))
        self.height_var = ctk.StringVar(value="1080")
        self.height_entry = ctk.CTkEntry(grid_frame, textvariable=self.height_var, width=100)
        self.height_entry.grid(row=2, column=1, sticky="w", padx=(0, 20), pady=(10, 0))

        # Формат
        self.format_label = ctk.CTkLabel(grid_frame, text="")
        self.format_label.grid(row=3, column=0, sticky="w", padx=(0, 10), pady=(10, 0))
        self.format_var = ctk.StringVar(value="JPEG")
        self.format_combo = ctk.CTkComboBox(
            grid_frame,
            values=["JPEG", "PNG", "WEBP", "BMP", "TIFF"],
            variable=self.format_var,
            width=100
        )
        self.format_combo.grid(row=3, column=1, sticky="w", padx=(0, 20), pady=(10, 0))

        # Уровень сжатия
        self.compression_label = ctk.CTkLabel(grid_frame, text="")
        self.compression_label.grid(row=0, column=3, sticky="w", padx=(40, 10))
        self.compression_slider = ctk.CTkSlider(grid_frame, from_=1, to=9, number_of_steps=8, width=150)
        self.compression_slider.set(6)
        self.compression_slider.grid(row=0, column=4, padx=(0, 20))
        self.compression_value_label = ctk.CTkLabel(grid_frame, text="6")
        self.compression_value_label.grid(row=0, column=5)

        # Привязка событий
        self.quality_slider.configure(command=self.update_quality_label)
        self.compression_slider.configure(command=self.update_compression_label)

    def create_advanced_settings(self):
        """Создает секцию расширенных настроек"""
        self.advanced_frame = ctk.CTkFrame(self.main_frame)
        self.advanced_frame.pack(fill="x", pady=(0, 15))

        # Заголовок с возможностью свернуть/развернуть
        header_frame = ctk.CTkFrame(self.advanced_frame, fg_color="transparent")
        header_frame.pack(fill="x", padx=20, pady=10)

        self.advanced_title_label = ctk.CTkLabel(
            header_frame,
            text="",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.advanced_title_label.pack(side="left")

        # Переключатель видимости расширенных настроек
        self.advanced_visible = ctk.BooleanVar(value=False)
        self.advanced_toggle = ctk.CTkSwitch(
            header_frame,
            text="",
            variable=self.advanced_visible,
            command=self.toggle_advanced_settings
        )
        self.advanced_toggle.pack(side="right")

        # Расширенные настройки (изначально скрыты)
        self.advanced_content = ctk.CTkFrame(self.advanced_frame)
        self.advanced_content.pack(fill="x", padx=20, pady=(0, 15))
        self.advanced_content.pack_forget()  # Скрываем изначально

        # Чекбоксы расширенных настроек
        self.metadata_var = ctk.BooleanVar(value=True)
        self.metadata_checkbox = ctk.CTkCheckBox(
            self.advanced_content,
            text="",
            variable=self.metadata_var
        )
        self.metadata_checkbox.pack(anchor="w", pady=5)

        self.overwrite_var = ctk.BooleanVar(value=False)
        self.overwrite_checkbox = ctk.CTkCheckBox(
            self.advanced_content,
            text="",
            variable=self.overwrite_var
        )
        self.overwrite_checkbox.pack(anchor="w", pady=5)

        self.structure_var = ctk.BooleanVar(value=True)
        self.structure_checkbox = ctk.CTkCheckBox(
            self.advanced_content,
            text="",
            variable=self.structure_var
        )
        self.structure_checkbox.pack(anchor="w", pady=5)

    def create_progress_section(self):
        """Создает секцию прогресса и кнопку оптимизации"""
        self.progress_frame = ctk.CTkFrame(self.main_frame)
        self.progress_frame.pack(fill="x", pady=(0, 15))

        # Статус
        self.status_label = ctk.CTkLabel(
            self.progress_frame,
            text="",
            font=ctk.CTkFont(size=12)
        )
        self.status_label.pack(anchor="w", padx=20, pady=(15, 5))

        # Прогресс-бар
        self.progress_bar = ctk.CTkProgressBar(self.progress_frame)
        self.progress_bar.pack(fill="x", padx=20, pady=(0, 15))
        self.progress_bar.set(0)

        # Кнопка оптимизации
        self.optimize_btn = ctk.CTkButton(
            self.progress_frame,
            text="",
            command=self.start_optimization,
            height=40,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.optimize_btn.pack(fill="x", padx=20, pady=(0, 15))

    def create_results(self):
        """Создает секцию результатов"""
        self.results_frame = ctk.CTkFrame(self.main_frame)
        self.results_frame.pack(fill="both", expand=True)

        self.results_title_label = ctk.CTkLabel(
            self.results_frame,
            text="",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.results_title_label.pack(anchor="w", padx=20, pady=10)

        # Текстовое поле для результатов
        self.results_text = ctk.CTkTextbox(self.results_frame, wrap="word")
        self.results_text.pack(fill="both", expand=True, padx=20, pady=(0, 15))

    def update_quality_label(self, value):
        """Обновляет метку качества"""
        self.quality_value_label.configure(text=f"{int(float(value))}%")

    def update_compression_label(self, value):
        """Обновляет метку уровня сжатия"""
        self.compression_value_label.configure(text=f"{int(float(value))}")

    def toggle_advanced_settings(self):
        """Переключает видимость расширенных настроек"""
        if self.advanced_visible.get():
            self.advanced_content.pack(fill="x", padx=20, pady=(0, 15))
            # Обновляем текст переключателя
            self.advanced_toggle.configure(text=self.get_text("hide_advanced"))
        else:
            self.advanced_content.pack_forget()
            # Обновляем текст переключателя
            self.advanced_toggle.configure(text=self.get_text("show_advanced"))

    def change_language(self, choice):
        """Изменяет язык интерфейса"""
        self.current_language = choice
        self.update_ui_language()
        self.save_settings()

    def update_ui_language(self):
        """Обновляет весь интерфейс на выбранный язык"""
        # Обновляем заголовок окна
        self.root.title(self.get_text("title") + self.get_text("os_specific")[self.current_os])

        # Заголовок
        self.subtitle_label.configure(text=self.get_text("title").split("-")[1].strip())

        # Информация об ОС
        self.os_info_label.configure(text=self.get_text("os_specific")["current_os"])

        # Язык
        self.language_label.configure(text=self.get_text("language"))

        # Выбор файлов
        self.select_files_btn.configure(text=self.get_text("select_files"))
        self.select_folder_btn.configure(text=self.get_text("select_folder"))
        self.file_info_label.configure(text=f"{len(self.selected_files)} {self.get_text('files_selected')}")

        # Папка вывода
        self.output_folder_label.configure(text=self.get_text("output_folder"))
        self.output_entry.configure(placeholder_text=self.get_text("select_output_folder"))
        self.browse_btn.configure(text=self.get_text("browse"))

        # Основные настройки
        self.settings_title_label.configure(text=self.get_text("basic_settings"))
        self.quality_label.configure(text=self.get_text("quality"))
        self.max_width_label.configure(text=self.get_text("max_width"))
        self.max_height_label.configure(text=self.get_text("max_height"))
        self.format_label.configure(text=self.get_text("format"))
        self.compression_label.configure(text=self.get_text("compression_level"))

        # Расширенные настройки
        self.advanced_title_label.configure(text=self.get_text("advanced_settings"))
        self.metadata_checkbox.configure(text=self.get_text("maintain_metadata"))
        self.overwrite_checkbox.configure(text=self.get_text("overwrite_existing"))
        self.structure_checkbox.configure(text=self.get_text("preserve_structure"))

        # Обновляем текст переключателя расширенных настроек
        if self.advanced_visible.get():
            self.advanced_toggle.configure(text=self.get_text("hide_advanced"))
        else:
            self.advanced_toggle.configure(text=self.get_text("show_advanced"))

        # Прогресс
        self.status_label.configure(text=self.get_text("status_ready"))
        self.optimize_btn.configure(text=self.get_text("optimize"))

        # Результаты
        self.results_title_label.configure(text=self.get_text("results"))

        # Обновляем результаты если есть
        current_results = self.results_text.get(1.0, "end-1c")
        if current_results and self.get_text("optimization_complete") in current_results:
            # Переводим заголовок результатов
            lines = current_results.split('\n')
            if len(lines) > 0:
                new_results = self.get_text("optimization_complete") + "\n" + "=" * 40 + "\n"
                # Сохраняем остальную часть результатов (статистику)
                if len(lines) > 2:
                    new_results += "\n".join(lines[2:])
                self.results_text.delete(1.0, "end")
                self.results_text.insert(1.0, new_results)

    def select_files(self):
        """Выбор файлов для оптимизации"""
        files = filedialog.askopenfilenames(
            title=self.get_text("select_files"),
            filetypes=[
                ("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff *.webp"),
                ("All files", "*.*")
            ]
        )
        if files:
            self.selected_files = list(files)
            self.file_info_label.configure(text=f"{len(self.selected_files)} {self.get_text('files_selected')}")

    def select_folder(self):
        """Выбор папки с изображениями"""
        folder = filedialog.askdirectory(title=self.get_text("select_folder"))
        if folder:
            self.selected_files = []
            for format_ext in self.supported_formats:
                self.selected_files.extend(Path(folder).rglob(f"*{format_ext}"))
                self.selected_files.extend(Path(folder).rglob(f"*{format_ext.upper()}"))

            self.file_info_label.configure(text=f"{len(self.selected_files)} {self.get_text('files_selected')}")

    def select_output_folder(self):
        """Выбор папки для сохранения"""
        folder = filedialog.askdirectory(title=self.get_text("select_output_folder"))
        if folder:
            self.output_path_var.set(folder)

    def format_file_size(self, size_bytes):
        """Форматирует размер файла в читаемый вид"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.1f} TB"

    def optimize_image(self, input_path, output_path):
        """Оптимизирует одно изображение"""
        try:
            with Image.open(input_path) as img:
                # Сохраняем оригинальный размер
                original_size = os.path.getsize(input_path)

                # Конвертируем в RGB если нужно для JPEG
                if self.format_var.get() == "JPEG" and img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")

                # Получаем новые размеры
                try:
                    max_width = int(self.width_var.get()) if self.width_var.get() else 1920
                    max_height = int(self.height_var.get()) if self.height_var.get() else 1080
                except:
                    max_width, max_height = 1920, 1080

                # Изменяем размер если нужно
                if img.width > max_width or img.height > max_height:
                    img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)

                # Параметры сохранения
                save_kwargs = {}
                if self.format_var.get() == "JPEG":
                    save_kwargs = {
                        'quality': int(self.quality_slider.get()),
                        'optimize': True
                    }
                elif self.format_var.get() == "PNG":
                    save_kwargs = {
                        'compress_level': int(self.compression_slider.get()),
                        'optimize': True
                    }
                elif self.format_var.get() == "WEBP":
                    save_kwargs = {
                        'quality': int(self.quality_slider.get()),
                        'method': int(self.compression_slider.get())
                    }

                # Сохраняем изображение
                img.save(output_path, **save_kwargs)

                # Получаем размер оптимизированного файла
                optimized_size = os.path.getsize(output_path)

                return original_size, optimized_size

        except Exception as e:
            print(f"Error optimizing {input_path}: {str(e)}")
            return None, None

    def start_optimization(self):
        """Запускает процесс оптимизации в отдельном потоке"""
        if not hasattr(self, 'selected_files') or not self.selected_files:
            messagebox.showwarning(self.get_text("title"), self.get_text("no_files_selected"))
            return

        if not self.output_path_var.get():
            messagebox.showwarning(self.get_text("title"), self.get_text("no_output_folder"))
            return

        # Блокируем кнопку во время обработки
        self.optimize_btn.configure(state="disabled")
        self.status_label.configure(text=self.get_text("status_processing"))

        # Запускаем в отдельном потоке
        thread = threading.Thread(target=self.optimize_images)
        thread.daemon = True
        thread.start()

    def optimize_images(self):
        """Оптимизирует все выбранные изображения"""
        total_files = len(self.selected_files)
        processed_files = 0
        total_original_size = 0
        total_optimized_size = 0

        self.results_text.delete(1.0, "end")

        # Добавляем информацию об ОС в результаты
        os_info = f"{self.get_text('os_specific')['current_os']}\n"
        os_info += f"{self.get_text('os_specific')['os_features']}\n\n"
        self.results_text.insert("end", os_info)
        self.results_text.insert("end", f"{self.get_text('processing_files')}\n\n")

        for input_path in self.selected_files:
            try:
                input_path = Path(input_path)

                # Определяем путь для сохранения
                if self.structure_var.get() and len(self.selected_files) > 1:
                    # Сохраняем структуру папок
                    relative_path = input_path.relative_to(input_path.parents[-1])
                    output_path = Path(self.output_path_var.get()) / relative_path
                    output_path.parent.mkdir(parents=True, exist_ok=True)
                else:
                    # Просто сохраняем в указанную папку
                    output_path = Path(self.output_path_var.get()) / input_path.name

                # Изменяем расширение если нужно
                if self.format_var.get() != "ORIGINAL":
                    output_path = output_path.with_suffix(f".{self.format_var.get().lower()}")

                # Проверяем существование файла
                if output_path.exists() and not self.overwrite_var.get():
                    output_path = output_path.with_stem(f"{output_path.stem}_optimized")

                # Оптимизируем изображение
                original_size, optimized_size = self.optimize_image(input_path, output_path)

                if original_size and optimized_size:
                    total_original_size += original_size
                    total_optimized_size += optimized_size

                    savings = original_size - optimized_size
                    savings_percent = (savings / original_size) * 100

                    # Добавляем результат в текстовое поле
                    result_text = (
                        f"{input_path.name}:\n"
                        f"  {self.get_text('original')}: {self.format_file_size(original_size)}\n"
                        f"  {self.get_text('optimized')}: {self.format_file_size(optimized_size)}\n"
                        f"  {self.get_text('savings')}: {self.format_file_size(savings)} ({savings_percent:.1f}%)\n\n"
                    )

                    self.root.after(0, self.update_results, result_text)

            except Exception as e:
                error_text = f"{self.get_text('error_processing')} {input_path.name}: {str(e)}\n\n"
                self.root.after(0, self.update_results, error_text)

            processed_files += 1
            progress = processed_files / total_files
            self.root.after(0, self.update_progress, progress)

        # Показываем итоги
        total_savings = total_original_size - total_optimized_size
        total_savings_percent = (total_savings / total_original_size) * 100 if total_original_size > 0 else 0

        final_text = (
            f"\n{self.get_text('optimization_complete')}\n"
            f"========================================\n"
            f"{self.get_text('file_size')}:\n"
            f"  {self.get_text('original')}: {self.format_file_size(total_original_size)}\n"
            f"  {self.get_text('optimized')}: {self.format_file_size(total_optimized_size)}\n"
            f"  {self.get_text('savings')}: {self.format_file_size(total_savings)} ({total_savings_percent:.1f}%)\n"
            f"  {self.get_text('files_processed')}: {processed_files}\n"
        )

        self.root.after(0, self.finish_optimization, final_text)

    def update_results(self, text):
        """Обновляет текстовое поле с результатами"""
        self.results_text.insert("end", text)
        self.results_text.see("end")

    def update_progress(self, progress):
        """Обновляет прогресс-бар"""
        self.progress_bar.set(progress)

    def finish_optimization(self, final_text):
        """Завершает процесс оптимизации"""
        self.update_results(final_text)
        self.status_label.configure(text=self.get_text("status_complete"))
        self.optimize_btn.configure(state="normal")
        messagebox.showinfo(self.get_text("title"), self.get_text("optimization_complete"))

    def run(self):
        """Запускает приложение"""
        self.root.mainloop()


if __name__ == "__main__":
    # Инициализация и запуск приложения
    app = ImageOptimizer()
    app.run()