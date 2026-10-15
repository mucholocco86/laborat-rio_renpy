"""One compact, reusable UI for standalone and Wells Manager use."""

from __future__ import annotations

import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path

from .core import WellsSdkError, run_operation


BG = "#222222"
FG = "#eeeeee"
BUTTON_BG = "#b5b5b5"


class WellsSdkPanel:
    def __init__(self, parent, *, register_button=None, on_busy=None,
                 on_status=None, on_log=None):
        self.parent = parent
        top = parent.winfo_toplevel()
        self.scheduler = top.master if isinstance(top, tk.Toplevel) and top.master else top
        self.register_button = register_button
        self.on_busy = on_busy
        self.on_status = on_status
        self.on_log = on_log
        self.busy = False
        self.action_buttons = []

        self.frame = tk.Frame(parent, bg=BG)
        self.frame.pack(fill="both", expand=True, padx=14, pady=12)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(3, weight=1)

        tk.Label(
            self.frame, text="WELLS SDK", bg=BG, fg="#ff1010",
            font=("Segoe UI", 16, "bold"),
        ).grid(row=0, column=0, sticky="w", pady=(0, 8))

        project_row = tk.Frame(self.frame, bg=BG)
        project_row.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        project_row.grid_columnconfigure(1, weight=1)
        tk.Label(project_row, text="Projeto do jogo:", bg=BG, fg=FG,
                 font=("Segoe UI", 9, "bold")).grid(row=0, column=0, padx=(0, 8))
        self.project_var = tk.StringVar(master=self.frame)
        tk.Entry(project_row, textvariable=self.project_var, relief="sunken").grid(
            row=0, column=1, sticky="ew", padx=(0, 8)
        )
        self.project_button = tk.Button(
            project_row, text="Selecionar...", command=self._choose_project,
            bg=BUTTON_BG, fg="#101010", relief="raised", bd=2,
            font=("Segoe UI", 9, "bold"),
        )
        self._register(self.project_button)
        self.project_button.grid(row=0, column=2)

        columns = tk.Frame(self.frame, bg=BG)
        columns.grid(row=2, column=0, sticky="ew")
        columns.grid_columnconfigure(0, weight=1, uniform="sdk_columns")
        columns.grid_columnconfigure(1, weight=1, uniform="sdk_columns")
        self._build_generate(columns)
        self._build_extract(columns)

        footer = tk.Frame(self.frame, bg=BG)
        footer.grid(row=3, column=0, sticky="nsew", pady=(10, 0))
        footer.grid_columnconfigure(0, weight=1)
        footer.grid_rowconfigure(1, weight=1)
        self.status_var = tk.StringVar(master=self.frame, value="Pronto.")
        tk.Label(footer, textvariable=self.status_var, bg=BG, fg=FG,
                 anchor="w", font=("Segoe UI", 9)).grid(row=0, column=0, sticky="ew", pady=(0, 4))
        self.log = tk.Text(
            footer, height=5, bg="#2b2b2b", fg=FG, insertbackground="white",
            relief="solid", bd=1, font=("Consolas", 8), state="disabled", wrap="word",
        )
        self.log.grid(row=1, column=0, sticky="nsew")

    def _register(self, button):
        self.action_buttons.append(button)
        if self.register_button:
            self.register_button(button)

    def _build_generate(self, parent):
        box = tk.LabelFrame(parent, text="Gerar traduções", bg=BG, fg=FG,
                            font=("Segoe UI", 10, "bold"), padx=10, pady=8)
        box.grid(row=0, column=0, sticky="nsew", padx=(0, 6))
        box.grid_columnconfigure(0, weight=1)
        tk.Label(box, text="Idioma/localização:", bg=BG, fg=FG,
                 anchor="w").grid(row=0, column=0, sticky="ew")
        # Match the Ren'Py launcher default; users can enter any locale ID.
        self.generate_language = tk.StringVar(master=self.frame, value="english")
        tk.Entry(box, textvariable=self.generate_language).grid(row=1, column=0, sticky="ew", pady=(2, 8))
        self.empty_var = tk.BooleanVar(master=self.frame, value=True)
        tk.Checkbutton(
            box, text="Gerar strings vazias", variable=self.empty_var,
            bg=BG, fg=FG, activebackground=BG, activeforeground=FG,
            selectcolor="#333333", anchor="w",
        ).grid(row=2, column=0, sticky="ew", pady=(0, 8))
        self.generate_button = self._action_button(
            box, "Gerar traduções", lambda: self._start("generate")
        )
        self.generate_button.grid(row=3, column=0, sticky="ew")

    def _build_extract(self, parent):
        box = tk.LabelFrame(parent, text="Extrair diálogos", bg=BG, fg=FG,
                            font=("Segoe UI", 10, "bold"), padx=10, pady=8)
        box.grid(row=0, column=1, sticky="nsew", padx=(6, 0))
        box.grid_columnconfigure(0, weight=1)
        tk.Label(box, text="Idioma (None = idioma padrão):", bg=BG, fg=FG,
                 anchor="w").grid(row=0, column=0, sticky="ew")
        self.extract_language = tk.StringVar(master=self.frame, value="None")
        tk.Entry(box, textvariable=self.extract_language).grid(row=1, column=0, sticky="ew", pady=(2, 6))
        tk.Label(box, text="Formato:", bg=BG, fg=FG, anchor="w").grid(row=2, column=0, sticky="ew")
        self.format_var = tk.StringVar(master=self.frame, value="tab")
        ttk.Combobox(box, textvariable=self.format_var, values=("tab", "txt"),
                     state="readonly", width=12).grid(row=3, column=0, sticky="w", pady=(2, 4))
        self.include_strings_var = tk.BooleanVar(master=self.frame, value=False)
        self.strip_tags_var = tk.BooleanVar(master=self.frame, value=False)
        self.escape_var = tk.BooleanVar(master=self.frame, value=False)
        for row, label, variable in (
            (4, "Incluir todas as strings traduzíveis", self.include_strings_var),
            (5, "Remover tags do texto", self.strip_tags_var),
            (6, "Escapar aspas e caracteres especiais", self.escape_var),
        ):
            tk.Checkbutton(
                box, text=label, variable=variable, bg=BG, fg=FG,
                activebackground=BG, activeforeground=FG,
                selectcolor="#333333", anchor="w",
            ).grid(row=row, column=0, sticky="ew")
        self.extract_button = self._action_button(
            box, "Extrair diálogos", lambda: self._start("extract")
        )
        self.extract_button.grid(row=7, column=0, sticky="ew", pady=(6, 0))

    def _action_button(self, parent, text, command):
        button = tk.Button(
            parent, text=text, command=command, height=1,
            bg=BUTTON_BG, fg="#101010", activebackground="#c5c5c5",
            activeforeground="#000000", relief="raised", bd=2,
            font=("Segoe UI", 9, "bold"),
        )
        self._register(button)
        return button

    def _choose_project(self):
        selected = filedialog.askdirectory(title="Selecione a pasta raiz do jogo Ren'Py")
        if selected:
            self.project_var.set(selected)

    def _set_local_controls(self, enabled):
        state = "normal" if enabled else "disabled"
        for button in self.action_buttons:
            try:
                button.configure(state=state)
            except tk.TclError:
                pass

    def _append_log(self, message):
        try:
            self.log.configure(state="normal")
            self.log.insert("end", message.rstrip() + "\n")
            self.log.see("end")
            self.log.configure(state="disabled")
        except tk.TclError:
            pass
        if self.on_log:
            self.on_log(message)

    def _start(self, operation):
        if self.busy:
            return
        project = self.project_var.get().strip()
        if not project:
            messagebox.showinfo("Wells SDK", "Selecione a pasta raiz do jogo.", parent=self.frame)
            return
        if operation == "generate":
            options = {
                "language": self.generate_language.get(),
                "empty_strings": self.empty_var.get(),
            }
        else:
            options = {
                "language": self.extract_language.get(),
                "dialogue_format": self.format_var.get(),
                "include_strings": self.include_strings_var.get(),
                "strip_tags": self.strip_tags_var.get(),
                "escape_special": self.escape_var.get(),
            }

        self.busy = True
        self._set_local_controls(False)
        self.status_var.set("Executando comando do Ren'Py...")
        self._append_log(f"Iniciando: {operation} | Projeto: {project}")
        if self.on_busy:
            self.on_busy(True)
        if self.on_status:
            self.on_status("Status: Wells SDK está processando o projeto...")

        def worker():
            try:
                result = run_operation(project, operation, **options)
                error = None
            except Exception as exc:
                result, error = None, exc
            try:
                self.scheduler.after(0, lambda: self._finish(operation, result, error))
            except tk.TclError:
                pass

        threading.Thread(target=worker, daemon=True).start()

    def _finish(self, operation, result, error):
        self.busy = False
        try:
            if not self.frame.winfo_exists():
                if self.on_busy:
                    self.on_busy(False)
                if self.on_status:
                    self.on_status("Status: Operação Wells SDK finalizada.")
                return
        except tk.TclError:
            if self.on_busy:
                self.on_busy(False)
            return
        self._set_local_controls(True)
        if self.on_busy:
            self.on_busy(False)
        if error is not None:
            self.status_var.set("Falha ao executar a operação.")
            self._append_log(f"ERRO: {error}")
            if self.on_status:
                self.on_status("Status: Erro no Wells SDK.")
            messagebox.showerror("Wells SDK", str(error), parent=self.frame)
            return

        output_text = result.stdout.strip()
        error_text = result.stderr.strip()
        if output_text:
            self._append_log(output_text[-4000:])
        if error_text:
            self._append_log(error_text[-4000:])

        if result.returncode == 0:
            self.status_var.set(f"Concluído. Saída esperada: {result.output_path}")
            self._append_log(f"Concluído. Código de saída: 0. Saída: {result.output_path}")
            if self.on_status:
                self.on_status(f"Status: Operação Ren'Py concluída: {result.output_path}")
        else:
            details = error_text or output_text or "O engine terminou com erro sem mensagem adicional."
            self.status_var.set(f"Ren'Py terminou com erro ({result.returncode}).")
            self._append_log(f"Falha. Código de saída: {result.returncode}.")
            if self.on_status:
                self.on_status("Status: Erro na operação Ren'Py.")
            messagebox.showerror(
                "Wells SDK", f"O Ren'Py retornou código {result.returncode}.\n\n{details[-3000:]}",
                parent=self.frame,
            )


def build_panel(parent, *, register_button=None, on_busy=None,
                on_status=None, on_log=None):
    """Build the same two-column panel in standalone or Wells Manager."""
    return WellsSdkPanel(
        parent, register_button=register_button, on_busy=on_busy,
        on_status=on_status, on_log=on_log,
    )

